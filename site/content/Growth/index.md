---
title: 'growth index'
template: coltrane/content.html
active: ok
publish_date: 2024-07-30 20:20:01
---
This space aims to help you think about your professional growth in a way that is not dissociated from your personal one. Psychotherapy is a strange profession that has a circular quality: our growth impacts work and work impact or growth. This phrase applies to any work, but only in therapy we see those effects on a daily basis and in a way that our same identity may be challenge. 

<h3><a href="/Growth/mastery/">Mastery</a></h3>
{% directory_contents '/Growth/mastery' order_by='order' as directory_contents %}
<ul class="list-group">
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li class="list-group-item list-group-item-primary"><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>

<h3><a href="/Growth/shadow/">Shadow Work</a></h3>
{% directory_contents 'Growth/shadow' order_by='order' as directory_contents %}
<ul class="list-group">
{% for content in  directory_contents %}
    {% if content.active != 'disabled' %}
    <li class="list-group-item list-group-item-primary"><a href="/{{content.slug}}/"
    >{{content.title}}
    </a></li>
    {% endif %}
    {% endfor %}
</ul>