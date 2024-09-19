---
title: 'approach index'
template: coltrane/content.html
publish_date: 2024-07-30 20:20:01
---

<h3>CreaTherapy</h3>
{% directory_contents 'Approach/creatherapy' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>

<h3>Context</h3>
{% directory_contents 'Approach/context' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>


