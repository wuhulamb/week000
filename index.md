---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: home
pagination: 
  enabled: true
---

<p>Hi, 这里是wuhulamb的新站点.</p>

<p>为记录周报而建，所以叫week000.<br>可以记录 <code class="language-plaintext highlighter-rouge">999 * 7 / 365 ≈ 19 年</code> 😅.</p>

<p>简洁是这个站点最大的特点，但是功能应有尽有 ٩(๑˃̵ᴗ˂̵๑)۶ .</p>

<p>&nbsp;</p>

<h2 id="writing" style="color: #2bbc8a;">Writing</h2>

<ul class="post-list">
{%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
{% for post in paginator.posts %}
<li>
<span class="post-meta">{{ post.date | date: date_format }}</span>
<h3><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
</li>
{% endfor %}
</ul>

<div class="pagination">
{% if paginator.previous_page %}
<a href="{{ paginator.previous_page_path | relative_url }}"><i class="fa-solid fa-angle-left"></i></a>
{% endif %}
<span class="page-number">Page {{ paginator.page }} of {{ paginator.total_pages }}</span>
{% if paginator.next_page %}
<a href="{{ paginator.next_page_path | relative_url }}"><i class="fa-solid fa-angle-right"></i></a>
{% endif %}
</div>
      
