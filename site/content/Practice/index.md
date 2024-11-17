---
title: 'Practice index'
template: coltrane/content.html
active: disabled
publish_date: 2024-07-30 20:20:01
---


<h3><a href="/Practice/general_directions/">General Directions</a></h3>
{% directory_contents 'Practice/general_directions' order_by='order' as directory_contents %}
<ul>
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>

<h3><a href="/Practice/general_directions/">Therapeutic Principles</a></h3>
{% directory_contents 'Practice/principles' order_by='order' as directory_contents %}
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>



<h3><a href="/Practice/general_directions/">Symptoms to work with</a></h3>
{% directory_contents 'Practice/symptoms' order_by='order' as directory_contents %}
<a href="/Practice/symptoms/">Symptoms page</a>
<ul>
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>