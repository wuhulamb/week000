---
title:      "你好，世界！再见，GFW！"
date:       "2024-12-07 16:53:00 +0800"
categories: "others"
---

<figure>
<img src="https://image.baidu.com/search/down?url=https://wx2.sinaimg.cn/large/008kbRJbly1hwcg7le4rfj31fj0s7q7g.jpg" alt="hello-google.jpg">
<figcaption>hello Google!</figcaption>
</figure>

<figure>
<img src="https://image.baidu.com/search/down?url=https://wx3.sinaimg.cn/large/008kbRJbly1hwcg7ldypij31fk0s7jw0.jpg" alt="hello-gpt.jpg">
<figcaption>hello ChatGPT!</figcaption>
</figure>

> 前提条件：有一台可以访问外网的机器

使用Azure云服务器尝试ping了一下google.com，可以ping通，然后curl了google的首页，也可以打印，立即想到可以做一个vps访问全世界！

然后就翻出了之前收藏的shadowsocks资料，开干！

## 1. 服务器安装shadowsocks-libev

```text
sudo apt update
sudo apt install shadowsocks-libev
```

## 2. shadowsocks-libev配置文件

下面是config.json配置文件

```text
{
    "server":"0.0.0.0",
    "server_port":1234,
    "local_port":443,
    "password":"xxxx",
    "timeout":600,
    "method":"aes-256-gcm"
}
```

配置好后使用 `ss-server -c config.json` 命令运行

需要注意的是，"server"要填写**0.0.0.0**，表示服务器处于listening状态

## 3. 安装客户端

先根据配置文件填入基本信息，再从任务栏右键客户端打开全局代理

<figure>
<img src="https://image.baidu.com/search/down?url=https://wx2.sinaimg.cn/large/008kbRJbly1hwch0csuo6j30ce0cwn2d.jpg" alt="ss-client.jpg">
<figcaption>打开全局代理</figcaption>
</figure>

然后，就可以自由访问全世界了！

