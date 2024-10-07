---
title: 'Model Index'
order: 1
template: coltrane/group-nav.html
publish_date: 2024-07-30 20:20:01
---
# CreaTherapy Model Description

This section is to help you understand CreaTherapy in its core conceptual functioning.

## Sections
{% directory_contents 'Approach/creatherapy' order_by='order' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>
