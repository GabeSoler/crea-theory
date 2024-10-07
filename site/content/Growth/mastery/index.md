---
title: 'Mastery Index'
order: 1
template: coltrane/content.html
active: disabled
publish_date: 2024-07-30 20:20:01
---
# Mastery System

This section is to help you understand CreaTherapy mastery system in its core conceptual functioning.

## Sections
{% directory_contents 'Growth/mastery' order_by='order' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>
