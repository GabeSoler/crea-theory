---
title: 'Directions Index'
order: 1
template: coltrane/content.html
active: disabled
publish_date: 2024-07-30 20:20:01
---
# Therapy General Directions

This section is to help you understand CreaTherapy therapy directions system in its core conceptual functioning.

## Sections
{% directory_contents 'Practice/general_directions' order_by='order' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>