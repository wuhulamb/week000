---
title:      "POI核密度=可达性？！毕业论文题目再修改😢"
date:       "2024-12-13 21:10:00 +0800"
categories: "研究idea"
---

自毕业论文换成校内老师后，happy了好几天。原本想扩展之前的一个校创，研究不同类型城市（兰州、西安、重庆）的公园绿地可达性，直到打开高德开发者平台看到可怜的POI搜索接口每天只有100次请求额度时，彻底放弃了该思路，并开始想自己有哪些数据。（当时甚至在想能不能用爬到的图书馆数据写毕业论文，后面觉得不太合适还是算了）

过了两天，我突然想到大一的时候为了研究城市核心区与边缘区爬过兰州市POI数据（当时高德POI搜索接口每日请求额度有2000！），但是依然不太清楚做什么，于是在知网搜POI相关文献。点开的第一篇就hits me，做的是餐饮服务POI的空间分布和便利性研究，这不正是我可以做的吗！

又查阅了一些文献，最终确定题目：

- 中文：基于POI数据的生活性服务业空间分布及可达性研究——以甘肃省兰州市为例
- 英文：Spatial distribution and accessibility evaluation of life service based on POI data: A case study of Lanzhou City, Gansu Province

然后花了一天时间就写好了开题报告（虽然写的字数只有不到1000字）。那时感觉毕业论文已经不再话下，一周跑数据，一周写论文就能搞定。

因为POI核密度分析比较简单，丢给ArcMap跑一下就可以，所以得到结果后感觉毕业论文已经做了一半了。继续做可达性分析时就不紧不慢，直到昨天晚上可达性结果跑出来了，用ArcMap一看，woc完蛋了！和核密度分析的结果一模一样？！那后面还要怎么讨论空间分布对可达性的影响？

<figure>
<img src="https://image.baidu.com/search/down?url=https://wx1.sinaimg.cn/large/008kbRJbly1hwjmxkc47bj30vu0mh10s.jpg" alt="kernel_density.jpg">
<figcaption>兰州市主城区餐饮POI核密度分析</figcaption>
</figure>

<figure>
<img src="https://image.baidu.com/search/down?url=https://wx3.sinaimg.cn/large/008kbRJbly1hwjmxkc4z9j30vu0mh7ek.jpg" alt="accessibility.jpg">
<figcaption>兰州市主城区餐饮POI可达性分析</figcaption>
</figure>

遂连夜改题，又翻出之前在知网找到的POI文献，最终确定题目：

- 中文：基于POI数据的兰州市生活性服务业空间格局研究
- 英文：Study on spatial pattern of consumer service industry in Lanzhou based on POI data

研究思路：

1. 兰州市各生活性服务业的空间分布（**POI核密度分析**）
2. 兰州市不同地区生活性服务业的功能多样性（**单元格信息熵**）
3. 兰州市不同地区的主导生活性服务业（**消除POI数量影响**：单元格各生活性服务业POI数量占该生活性服务业全部POI比例；**计算占比**：使用上一步计算的比例再计算单元格不同生活性服务业比例；**取最大比例**：取占比最大的生活性服务业为主导）
