---
title: 'profiles index'
template: coltrane/content.html
publish_date: 2024-07-30 20:20:01
---


{% directory_contents 'Profiles/components' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.slug}}</a></li>
    {% endfor %}
</ul>


{% directory_contents 'Profiles/personal_profile' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.slug}}</a></li>
    {% endfor %}
</ul>


{% directory_contents 'Profiles/traditions' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.slug}}</a></li>
    {% endfor %}
</ul>
