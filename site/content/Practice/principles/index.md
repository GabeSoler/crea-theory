---
title: 'Principles Index'
order: 1
template: coltrane/content.html
active: disabled
publish_date: 2024-07-30 20:20:01
---
# Therapy Principles

This section is to help you understand CreaTherapy therapy principles system in its core conceptual functioning.

## Sections
{% directory_contents 'Practice/principles' order_by='order' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>