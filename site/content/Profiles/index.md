---
title: 'profiles index'
template: coltrane/content.html
active: ok
publish_date: 2024-10-07 20:20:01
---
The profile system is designed to help you navigate a plural and process base learning. The web app saves each entry so you can have a sense of change as you learn and ponder differently your positions and knowledge.

It is composed of three parts, one that aims to see an impression of your style and position regarding care, others and what matters more for you in relations to therapy.

The second, the components, it is to help you develop practical theories and track how you knowledgeable you are feeling in those relevant areas of human life.

The third is about reality and how do you engage with it, what matters for you at a deeper level, how do you think knowledge is better created, how do you think life is better explainer.

Please explore, question and wonder *with* the concepts I am offering. Have a look to the [WebApp](https://crea-therapy.com/) if you please.

> You can see two examples: [Jung](/authors/jung/profile/) , [Freud](/authors/freud/profile/)


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
