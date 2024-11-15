---
layout: page
title:  "Category"
permalink: /category/
---

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
