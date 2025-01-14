---
title:      "使用Ubuntu的第一天是装...字体？"
date:       "2025-01-14 21:12:00 +0800"
categories: "计算机"
---

今天是使用Ubuntu的第一天，安装了很多东西，但花了最多时间去~~找~~安装的是字体？！

Ubuntu上已经预安装了许多开源字体（以<a href="https://en.wikipedia.org/wiki/Noto_fonts" target="_blank">Noto</a>为最多），但是当下载完WPS打开前段时间做的PPT时，看到了一大片豆腐块状东西...（而且打开WPS的时候报错了！

（可以使用 `fc-list` 命令查看已经安装的字体文件，也可以在Ubuntu的搜索界面搜 Fonts ，用图形界面查看）

```text
fc-list | less
```

## 下载

然后我就在互联网上四处奔波找字体文件，在GitHub上找到了<a href="https://github.com/dv-anomaly/ttf-wps-fonts" target="_blank">ttf-wps-fonts</a>和<a href="https://github.com/adobe-fonts" target="_blank">Adobe Fonts</a>，<a href="https://packages.debian.org/sid/fonts/ttf-mscorefonts-installer" target="_blank">微软的英文字体</a>可以使用apt安装：

```text
sudo apt install ttf-mscorefonts-installer
```

微软的中文字体没有找到打包好的，就得自己去网上一个一个搜了（不过也可以找一台windows薅下来

## 安装

使用 `apt install` 的字体文件就不用管啦，后面刷新一下就可以了，下面主要针对自己下载的字体文件，介绍如何安装。

fontconfig会扫描特定目录，检查字体，如（ `/usr/share/fonts/` 和 `/home/user/.fonts/` 等，可以使用下面的命令查看有哪些目录：

```text
fc-cache -v | less
```

这些目录都可以放字体文件，或者放子目录。我是把零散下载的字体文件放在了 `/home/user/.fonts/` 这里，把 ttf-wps-fonts 放到了 `/usr/share/fonts/wps-office/` 这里（新建了 wps-office 文件夹）

`/home/user/.fonts/` 只能user用户使用， `/usr/share/fonts/wps-office/` 为系统所有用户可用（不过作为个人PC的单用户使用似乎影响不大？）

## 刷新缓存

刷新缓存后就可以在 `fc-list` 中找到下载的字体了。

```text
fc-cache -fv  # -f选项强制重新生成最新的缓存文件；-v选项是显示任务进度
```
