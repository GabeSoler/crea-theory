---
title: 'approach index'
template: coltrane/content.html
publish_date: 2024-07-30 20:20:01
---

<h3><a href="/Approach/creatherapy/">CreaTherapy</a></h3>
{% directory_contents 'Approach/creatherapy' order_by='order' as directory_contents %}
<ul class="list-group">
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li class="list-group-item list-group-item-primary"><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>



