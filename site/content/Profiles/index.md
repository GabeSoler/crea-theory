---
title: 'profiles index'
template: coltrane/content.html
publish_date: 2024-07-30 20:20:01
--- 

<h3><a href="/Profiles/components/">Components</a></h3>
{% directory_contents 'Profiles/components' order_by='order' as directory_contents %}
<ul>
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>

<h3><a href="/Profiles/personal_profile/">Personal Profile</a></h3>
{% directory_contents 'Profiles/personal_profile' order_by='order' as directory_contents %}
<ul>
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>

<h3><a href="/Profiles/traditions/">Big Traditions</a></h3>
{% directory_contents 'Profiles/traditions' order_by='order' as directory_contents %}
<ul>
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>
