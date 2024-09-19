---
title: 'Practice index'
template: coltrane/content.html
publish_date: 2024-07-30 20:20:01
---


<h3>General Directions</h3>
{% directory_contents 'Practice/general_directions' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>

<h3>Therapeutic Principles</h3>
{% directory_contents 'Practice/principles' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>

<h3>Shadow Work</h3>
{% directory_contents 'Practice/shadow' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>

<h3>Symptoms to work with</h3>
{% directory_contents 'Practice/symptoms' as directory_contents %}
<a href="/Practice/symptoms/">Symptoms page</a>
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>