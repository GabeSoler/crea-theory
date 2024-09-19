---
title: 'growth index'
template: coltrane/content.html
publish_date: 2024-07-30 20:20:01
---

<h3>Mastery</h3>
{% directory_contents '/Growth/mastery' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>

