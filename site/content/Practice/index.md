---
title: 'Practice Index'
order: 1
template: coltrane/content.html
active: ok
publish_date: 2024-11-18 20:20:01
---
# Practice Essays

Here I have written a few essays that aim to help you think between approaches without losing coherence. This are some sort of examples of my way of thinking and at teh same time useful reflections about psychotherapy practice. 

## Sections
{% directory_contents 'Practice/' order_by='order' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>
