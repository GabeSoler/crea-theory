---
title: 'Components Index'
order: 1
template: coltrane/content.html
active: ok
publish_date: 2024-07-30 20:20:01
---
# Therapy Components

This section is to help you understand CreaTherapy components system in its core conceptual functioning.

## Sections
{% directory_contents 'Profiles/components' order_by='order' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>