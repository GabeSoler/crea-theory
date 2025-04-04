---
title: Traditions and individuation
order: 3
template: coltrane/group-nav.html
active: ok
publish_date: 2024-07-30 20:20:01
---
Traditions are relevant for our development
They organise our knoledge and our values, give us belonging and a path of steps to grow. 


{% directory_contents 'pages/ind_trad/' order_by='order' as directory_contents %}
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