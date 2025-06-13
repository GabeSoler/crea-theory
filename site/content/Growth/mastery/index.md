---
title: 'Mastery Index'
order: 1
template: coltrane/content.html
active: ok
publish_date: 2024-11-15 20:20:01
---
# Mastery System

This section is to help you understand CreaTherapy mastery system in its core conceptual functioning.

## Sections
{% directory_contents 'Growth/mastery' order_by='order' as directory_contents %}
<ul class="list-group">
{% for content in directory_contents %}
    <li class="list-group-item list-group-item-primary"><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>
