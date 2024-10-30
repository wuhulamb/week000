---
layout: page
title:  "Category"
permalink: /category/
---

{% for c in site.categories %}
  {% assign my_counter = 0 %}
  {% for p in site.posts %}
    {%- if p.my_category == c.title -%}
      {% assign my_counter = my_counter | plus: 1 %}
    {%- endif -%}
  {% endfor %}
<h3><a href="{{ c.url | relative_url }}">{{ c.title }}（{{ my_counter }}）</a></h3>
{% endfor %}

