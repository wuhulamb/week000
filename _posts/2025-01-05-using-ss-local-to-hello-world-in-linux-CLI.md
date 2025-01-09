---
title:      "Linux命令行使用ss-local问候世界你好"
date:       "2025-01-05 21:22:00 +0800"
categories: "others"
---

需要安装的工具是shadowsocks-libev（服务端ss-server和客户端ss-local都包含在里面），安装命令可参考[你好，世界！再见，GFW！]({{ "p/hello-world/" | relative_url }})

## 原理

```text
client <---> ss-local <--[encrypted]--> ss-remote <---> target
```

本地计算机将请求先转发给127.0.0.1:1080，ss-local接收请求，再转发给代理服务器（配置文件中的server），代理服务器代转请求后，再把数据返回到ss-local，ss-local再把数据传给127.0.0.1:1080，本地计算机再从这里读取数据。

## ss-local配置文件

```text
{
    "server":"xxxx",
    "server_port":xxx,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"xxxxx",
    "timeout":20,
    "method":"aes-256-gcm"
}
```

运行命令为：

```text
ss-local -c config.json
```

## 设置ALL_PROXY环境变量

```text
export ALL_PROXY=socks5://127.0.0.1:1080
```

## 不用记得删除ALL_PROXY，关掉代理

```text
unset ALL_PROXY
```

