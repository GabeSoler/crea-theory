---
title: 'approach index'
template: coltrane/content.html
publish_date: 2024-07-30 20:20:01
---

<h3><a href="/Approach/creatherapy/">CreaTherapy</a></h3>
{% directory_contents 'Approach/creatherapy' order_by='order' as directory_contents %}
<ul>
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>

<h3><a href="/Approach/context/">Context</a></h3>
{% directory_contents 'Approach/context' order_by='order' as directory_contents %}
<ul>
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>


