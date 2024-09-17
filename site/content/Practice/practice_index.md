---
title: 'Practice index'
template: coltrane/content.html
publish_date: 2024-07-30 20:20:01
---
<a href="/Practice/symptoms/">Symptoms page</a>

{% directory_contents 'Practice/general_directions' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.slug}}</a></li>
    {% endfor %}
</ul>


{% directory_contents 'Practice/principles' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.slug}}</a></li>
    {% endfor %}
</ul>


{% directory_contents 'Practice/shadow' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.slug}}</a></li>
    {% endfor %}
</ul>

{% directory_contents 'Practice/symptoms' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.slug}}</a></li>
    {% endfor %}
</ul>