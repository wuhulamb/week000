---
title:   "使用原生jekyll给博客加入多层级分类"
date:    "2024-11-15 17:06:00 +0800"
categories: "others blog"
---

博客慕多层级分类久矣，今天终于实现了！

## 目标

- 有一个像[这样]({{ "category/" | relative_url }})的汇总所有category的展示页面
- 每个category页面输出所有对应的posts，类似[这样]({{ "category/week000/" | relative_url }})
- 每篇post在meta信息中输出所有category（一个或者两个）

## 思路

最初想建立类似文件夹的形式存放category.md文件（用于Front Matter写入目录title, permalink之类信息，构建category页面），category层级结构通过文件夹结构体现，类似以下这种：

```text
categories/
│
├── AAA/
│   ├── aaa.md
│   └── 111.md
│
├── BBB/
│   ├── bbb.md
│   └── 222.md
│
└── ...
```

<figure><figcaption>（存在亿点点问题的思路）</figcaption></figure>

但是很快发现问题，AAA目录的category.md文件放在哪里？

遂改变思路，将所有目录文件全放在 `categories/` 文件夹下，然后通过遍历该文件夹，设置条件逻辑找到想要的目录文件。

具体做法是使用两个循环分别遍历，第一个循环找top_level_category，第二个循环找sec_level_category，为了建立sec_level_category与top_level_category之间的关系，在sec_level_category.md文件Front Matter中加设了 `belong_to` 用来表示第二级目录与第一级目录的归属关系（当然每个category.md中还需要 `level` 来表示该目录的级别，不然怎么通过循环找top_level_category或是sec_level_category呢

最后每个category.md的Front Matter是：

```text
---
title: "blog"
permalink: /category/others/blog/
level: "2"
belong_to: "others"
---
```

<figure><figcaption>（这是<a href='{{ "category/others/blog/" | relative_url }}'>blog</a>的目录页文件，如果是一级目录， <code class="language-plaintext highlighter-rouge">level</code> 值为1 & 无 <code class="language-plaintext highlighter-rouge">belong_to</code> ）</figcaption></figure>

然后post的Front Matter是：

```text
---
title:   "使用原生jekyll给博客加入多层级分类"
date:    "2024-11-15 17:06:00 +0800"
categories: "others blog"
---
```

前面提到的category.md文件泛指目录页文件，下面是这些文件的名称：

```text
.
├── 0100week000.md
├── 0200literature.md
├── 0300idea.md
├── 0400diary.md
├── 0500others.md
└── 0501blog.md
```

Tips: <a href="https://jekyllrb.com/docs/posts/#tags-and-categories" target="_blank">jekyll支持blog多categories</a>，一篇博客可多个category，且支持使用 `site.categories[category_name]` 搜索名称为 `category_name` 的category下所有的posts

## 分类汇总页代码

- category页面输出对应posts，因为有jekyll的 `site.categories[category_name]` 所以就变的很简单了 :)
- post的meta信息展示也比较简单就不放了 :)

```text{% raw %}
<ul>
{% for top_page in site.pages %}
  {% assign top_found = false %}
  {% if top_page.path contains 'categories/' and top_page.level == '1' %}
    {% assign top_category = top_page.title %}
    {% assign top_category_url = top_page.url %}
    {% assign top_found = true %}
<li>
<a class="category-list-link" href="{{ top_category_url | relative_url }}">{{ top_category }}</a>
<span class="category-list-count">{{ site.categories[top_category].size }}</span>

{% if top_found %}
{% assign sec_found = false %}
{% for sec_page in site.pages %}
  {% if sec_page.path contains 'categories/' and sec_page.level == '2' and sec_page.belong_to == top_category and site.categories[sec_page.title].size > 0 %}
    {% assign sec_found = true %}
  {% endif %}
{% endfor %}

{% if sec_found %}
<ul>
  {% for sec_page in site.pages %}
    {% if sec_page.path contains 'categories/' and sec_page.level == '2' and sec_page.belong_to == top_category %}
      {% assign sec_category = sec_page.title %}
      {% assign sec_category_url = sec_page.url %}
<li>
<a class="category-list-link" href="{{ sec_category_url | relative_url }}">{{ sec_category }}</a>
<span class="category-list-count">{{ site.categories[sec_category].size }}</span>
</li>
    {% endif %}
  {% endfor %}
</ul>
{% endif %}
{% endif %}

</li>
  {% endif %}
{% endfor %}
</ul>
{% endraw %}```
