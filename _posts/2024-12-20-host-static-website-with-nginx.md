---
title:      "nginx部署静态网站"
date:       "2024-12-20 22:59:00 +0800"
categories: "计算机"
---

昨天打开学校邮箱找材料的时候突然发现<a href="https://education.github.com/pack" target="_blank">GitHub学生包</a>申请成功了（十天前的邮件 ...），所以今天就迫不及待地申请了<a href="https://nc.me/" target="_blank">Namecheap</a>的域名耍耍（GitHub学生包可以免费申请namecheap域名使用一年）。随即把本站的初始域名 `https://week000.pages.dev/` 换成了 `https://week000.wuhulamb.me/` （在namecheap的控制台加入一条CNAME映射；在CloudFlare的站点自定义域名添加映射）

当然，有了域名和服务器，自然会想把服务托管到自己的服务器上（不然服务器不就浪费了吗）。我比较熟的是静态网站（因为这个最简单），所以想实现的是通过namecheap的域名能直接访问服务器上的静态网站资源（之前一直使用Github Pages或者CloudFlare的托管服务）

查了一些资料终于折腾出来了，具体做法如下。

## 1. 在域名服务商加入A记录

A记录：将域名映射到ipv4

映射完成后需要一两分钟解析，可以通过 `nslookup` 命令查询域名的ip。

```text
nslookup test.wuhulamb.me         # 使用本机的DNS服务器查询ip
nslookup test.wuhulamb.me 8.8.8.8 # 使用Google的DNS服务器查询ip
```

## 2. 配置服务器nginx

### 2.1 安装nginx

```text
sudo apt update
sudo apt install nginx
```

安装完成后，浏览器输入ip地址会显示欢迎页面（Azure云服务器需要设置network入站规则开放80端口）

### 2.2 nginx配置文件

在 `/etc/nginx/` 下有nginx的配置文件， `/etc/nginx/sites-enabled` 有一个 `default` 的链接文件，指向 `/etc/nginx/sites-available/default` ，这两个文件即默认配置文件，也是欢迎页的配置文件，所以我们给具体站点创建配置文件时，也需要在这两个目录下对应创建。

```text
sudo vim /etc/nginx/sites-available/test.wuhulamb.me
sudo ln -s /etc/nginx/sites-available/test.wuhulamb.me /etc/nginx/sites-enabled/
```

test.wuhulamb.me配置文件可以仿照default来写

```text
server {
    listen 80;
    root   /home/user/xxx/test.wuhulamb.me;
    server_name test.wuhulamb.me;
    index index.html index.htm index.nginx-debian.html;
}
```

root后面的路径即静态网站资源的存放路径，server_name填写设置的域名（nginx根据域名判断访问什么资源），index后面填首页的文件

配置完成后需要重启nginx服务使其生效：

```text
sudo systemctl restart nginx
```

### 2.3 （重要）修改/etc/nginx/nginx.conf的user

/etc/nginx/nginx.conf文件默认user为www-data，如果不修改，访问会出现403 forbidden，原因是www-data没有访问网站资源的权限，修改成网站资源所属的用户即可。

需要说明的是：默认情况下nginx的Master Process用户是root，由它创建的Worker Process用户是www-data。
