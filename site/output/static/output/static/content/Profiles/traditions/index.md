---
title: 'Big Traditions'
order: 2
template: coltrane/content.html
active: ok
publish_date: 2024-07-30 20:20:01
---
# Philosophy:
The philosophical layer is the more abstract plane of any practice. It addresses the notions of reality, knowledge production, and ethics. We all have some assumptions about these three areas, but it is quite helpful to make them explicit and to see if there are like-minded people in the field.


{% directory_contents 'pages/philosophies/' order_by='order' as directory_contents %}
<ul>
{% for content in  directory_contents %}
    <div class="card">
    <div class="card-header display-5">{{content.title|title}} {{content.emoji}}</div>
    <div class="card-body p-4 m-2">
    <div class="card-text m-2"><b>Description: </b>{{content.description}}</div>
    <div class="card-text m-2"><b>Example: </b>{{content.example}}</div>
    <div class="card-text m-2"><b>Traditions: </b>{{content.traditions}}</div>
    </div>
    </div>
    {% endfor %}
</ul>