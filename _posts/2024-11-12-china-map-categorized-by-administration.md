---
title:       "突然发现自己可以画很好看的地图了"
date:        "2024-11-12 11:50:00 +0800"
categories:  "others"
---

<figure>
<img src="https://image.baidu.com/search/down?url=https://wx1.sinaimg.cn/large/008kbRJbly1hvjappxabwj31wx1wxqif.jpg" alt="china-map-categorized-by-administration.jpg">
<figcaption>使用weibo作为图床，原图存档github仓库</figcaption>
</figure>

## Data

- 中国行政区划边界坐标数据爬取自高德地图API
- 行政编码最初用的是<a href="https://www.mca.gov.cn/n156/n186/index.html" target="_blank">民政部网站</a>数据，后来发现高德地图API里也有就直接用了

## ArcMap & Photoshop

地图使用ArcMap制作（地理坐标系: WGS_1984 -> 投影坐标系: Asia Lambert Conformal Conic Projection），最后右下角南海界线使用Photoshop绘制

## weibo图床 & baidu图片缓存

`<img>` 标签的 `src` 是 `https://image.baidu.com/search/down?url=https://wx1.sinaimg.cn/large/008kbRJbly1hvjappxabwj31wx1wxqif.jpg`

