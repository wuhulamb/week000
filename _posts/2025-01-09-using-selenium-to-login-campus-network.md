---
title:      "使用selenium模拟浏览器登录校园网"
date:       "2025-01-09 10:49:00 +0800"
categories: "others"
---

校园网采用无感知认证，登录一次后自动添加MAC地址，下次登录可以直接连接。而有一次校园网不是很稳定，服务器断网了，我从校园网的控制界面下线了服务器，然后又手动重启（ **`关闭 & 打开`** 服务器的电源），这时候发现服务器还是连不上校园网，打开无感知认证一看，之前保存的服务器MAC地址清除了。以往为了添加这个MAC地址，需要去实验室借用显示器，打开图形界面，从浏览器里登录校园网进行认证，总之非常麻烦。所以当时后悔莫及，真是手欠，为什么要点那个下线呢。

因为不想再跑实验室借显示器打开图形界面从浏览器登录校园网认证，所以考虑通过命令行终端登录校园网的办法。

还因为自己对网络知之甚少，抓包、逆向难度过高，所以果断选择使用selenium模拟浏览器登录的方法。

借助GPT，使用selenium并不困难，相关代码已存档<a href="https://github.com/wuhulamb/lzu_net_login" target="_blank">GitHub</a>，这里主要讲讲调试过程。

最大的问题是，如果服务器连接的是手机的热点与电脑通信，那一旦连校园网，ssh隧道就会断开，而脚本运行失败，就意味着服务器失联，然后又得手动重启（ **`关闭 & 打开`** 服务器的电源）。没错，所以最后是**连着校园网进行调试**的。既然已经能连上校园网了为什么还要再折腾呢？为了~~那个脚本程序不白写~~学习使用selenium。（虽然也不全是自己写的[手动狗头]）

总之，我抱着一定要在服务器上成功运行的坚定意志开始了我的调试。

## Windows上先跑起来

这里虽然和调试无关，却非常关键，一代目脚本诞生在这里。

## Linux上设置开机执行自定义脚本

为了图简单，我用的是crontab。

```text
# 编辑crontab
crontab -e
```

```text
# 写入开机要执行的命令
@reboot bash /path/to/script.sh
```

删除全部定时任务的命令是：

```text
crontab -r
```

## 重启 x N次

<figure>
<img src="https://image.baidu.com/search/down?url=https://wx3.sinaimg.cn/large/008kbRJbly1hxenv9x8qrj31fj0sa4ih.jpg" alt="lzu_net_test.jpg">
<figcaption>测试 x N次</figcaption>
</figure>

这是调试花费时间最多的环节。每次重启完，我都会紧张又期待地看着校园网控制台，希望看到一台新机器的连入，但希望总是落空。然后，就去控制台把服务器MAC地址添加进来，等待服务器自动连接。（没错，无感知认证可以手动添加MAC地址，而我却仍然坚定地想让服务器模拟浏览器自动登录）

当然，每次重启完，我都会去看脚本运行的日志，将报错记录扔给GPT，我也逐渐感觉到问题的所在。selenium模拟浏览器运行是通过一个驱动程序打开浏览器完成的，加载网页的时候，网页响应的时间往往比程序运行的时间长。这意味着有时候网页还没有发过来，程序已经往后运行了，而后面的程序是和网页相关的，它找不到网页就会报错。还有就是，selenium打开浏览器初始化速度比较慢，需要等待一段时间。

所以，最后解决办法就是在Python代码中加入 `time.sleep()`

（调试过程中，我还曾在script.sh脚本中加入过 `sleep 30` ，结果影响到后面的Python代码运行了，日志文件完全没变？！后来就把sleep放到Python代码里面，然后就很成功地登录上了）

<figure>
<img src="https://image.baidu.com/search/down?url=https://wx2.sinaimg.cn/large/008kbRJbly1hxenv9wa9hj31hc0scdtr.jpg" alt="lzu_net_py.jpg">
<figcaption>开机后脚本成功运行！</figcaption>
</figure>

## （补充）ARM64的Linux下载安装chromedriver

chromedriver需要和本地的chrome版本匹配，下面附上官方不同版本的chromedriver下载地址：

- 版本在114及以下：<a href="http://chromedriver.storage.googleapis.com/index.html" target="_blank">http://chromedriver.storage.googleapis.com/index.html</a>
- 最新版：<a href="https://googlechromelabs.github.io/chrome-for-testing/" target="_blank">https://googlechromelabs.github.io/chrome-for-testing/</a>
- GitHub：<a href="https://github.com/GoogleChromeLabs/chrome-for-testing" target="_blank">https://github.com/GoogleChromeLabs/chrome-for-testing</a>

但是很快我发现没有ARM64的版本（Linux64是x86_64的Linux），然后在<a href="https://github.com/electron/electron/releases" target="_blank">electron</a>找到了编译好的ARM64的chromedriver。

Linux可以先查看一下chrome的版本：

```text
chromium-browser --version
```

然后在上述GitHub项目中寻找对应版本的chromedriver（没错，我就是一页一页往下翻看更新说明找到的！）

## （彩蛋）哪里用到了X11 Forwarding

前面的一篇[介绍X11转发]({{ "p/using-x11-forwarding-to-open-GUI-program-via-ssh/" | relative_url }})的博客说到因为要使用浏览器登录认证身份联网，所以需要用到X11转发，解决ssh连接使用图形程序的问题。实际在没有登录上校园网时，ssh也连接不上，自然也用不到X11转发，但是在调试过程为了确认**不是因为浏览器版本导致界面显示不同而报错**确实用到了X11转发。
