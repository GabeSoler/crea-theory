---
title: Therapeutic Positions
order: 1
template: coltrane/group-nav.html
active: ok
publish_date: 2024-07-30 20:20:01
---

# Therapeutic Positions

Caring or therapeutic positions aim to show the complexities of our caring and how we can move and be more open to different ways of work. It also help us to see our prefered positions and therefore style.

This model unpacks some of the most important elements of our psychotherapy landscape. Yes, even more than the components and philosophy.

![positions]({% static 'images/profiles/positions-circle.png' %})

Each of the positions can be balanced, or polarised. When it gets polarised we can see ourseves in a shadow side of our care, represented in the circle. 

{% directory_contents 'pages/positions/' order_by='order' as directory_contents %}
<ul>
{% for content in  directory_contents %}
    <div class="card">
    <div class="card-header display-5">{{content.title|title}}</div>
    <div class="card-body p-4 m-2">
    <div class="card-image"><img class="img-thumbnail col-3 rounded" 
    src="{% static content.image %}"></div>
    <div class="card-text m-2"><b>Description: </b>{{content.description}}</div>
    <div class="card-text m-2"><b>Shadow: </b>{{content.shadow}}</div>
    <div class="card-text m-2"><b>Traditions: </b>{{content.traditions}}</div>
    <div class="card-text m-2"><b>Authors: </b>{{content.authors}}</div>
    </div>
    </div>
    {% endfor %}
</ul>




