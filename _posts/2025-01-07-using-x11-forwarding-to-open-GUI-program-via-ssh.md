---
title:      "使用X11转发做到SSH连接Linux打开图形程序"
date:       "2025-01-07 19:41:00 +0800"
categories: "计算机"
---

假设你有一台没有显示器的机器（Linux系统），并且你只能通过SSH连接它。为了能够使用它，你认真学习了很多命令，然而就在你以为再也不需要什么图形界面的时候，你遇到了一个**必须使用浏览器登录认证身份联网**的问题（~~等有空补上这篇博客~~ 👉 [使用selenium模拟浏览器登录校园网]({{ "p/using-selenium-to-login-campus-network/" | relative_url }})）。

命令行再厉害，遇到浏览器，也只能认输，桌面才是最适合浏览器使用的环境。但是SSH怎么弄一个桌面出来？！

## X11 Forwarding

```text
X client (Linux) <---> X Server (Windows)
```

原理大概就是Linux上设置转发路径，将图形程序的数据转发给Windows显示。

## Linux设置DISPLAY环境变量

```text
export DISPLAY=192.168.23.46:0.0  # hostname填X Server的ip
# export DISPLAY=hostname:display_number.screen_number
```

测试用的图形程序：

```text
# Ubuntu/Debian
sudo apt update
sudo apt install x11-apps
```

## Windows安装X Server

推荐安装<a href="https://sourceforge.net/projects/xming/" target="_blank">Xming</a>（轻量且易用）

安装过程可以根据需要选择性安装（例如：已经可以通过终端SSH登录就不需要再安装Putty了）

安装完成后，**不要直接打开Xming**。打开XLaunch完成配置，它会自动打开Xming，运行服务器程序。

配置XLaunch只需要注意勾选No Access Control，其他默认即可。

<figure>
<img src="https://image.baidu.com/search/down?url=https://wx1.sinaimg.cn/large/008kbRJbly1hxcgv9ps7kj30ho0eg0vy.jpg" alt="XLaunch_config.jpg">
<figcaption>勾选No Access Control</figcaption>
</figure>

## 验证

在设置好DISPLAY环境变量的Linux命令行界面运行X11图形测试程序

```text
xeyes
```
