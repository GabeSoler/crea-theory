---
title: Personal Profile Index
order: 1
template: coltrane/content.html
active: ok
publish_date: 2024-07-30 20:20:01
---
# Personal Profile

This section is to help you understand CreaTherapy Personal Profile system in its core conceptual functioning.

# care profile
First, we need to explore your style of care, and for that, I have four areas you may want to think about:
[Therapist/care positions](Profiles/personal_profile/therapy_positions.md)

- Acceptance: do you feel that acceptance is predominant?
- Challenge: do you feel challenging others helps them more?
- Propositive: do you like proposing options and actions?
- Follower: do you prefer to follow others in their rhythm?

From those four, I combine them to form another four types or therapeutic positions:

- Compassionate: championed by person centre, follows and accepts. 
- Inquisitive: championed by psychodynamic, follows and challenges.
- Playful: championed by Gestalt, proposes and accepts.
- Changer: championed by CBT, challenges and proposes. 

To be clear, these can be seen as types and positions. As types, we have a preferred way of approaching care. As positions, we move between them, as sometimes a situation calls for one or the other. 

This allows us to pinpoint your direction as a therapist while giving you plenty of space to explore different positions and nuances between approaches. 

The other two parts of the test also give us some clues about where you are in your process.

## growth path
[Growth Path](Profiles/personal_profile/deepth_path.md)

These four positions come from a more ontological question, asking where parts of reality are more attractive and how you approach reality. 

- Intensive: it refers to the more fluid parts of our experience, like our affections, dreams, and metaphors. 
- Extensive: refers to the concrete reality, which is stable and tridimensional. 
- Divider: refers to your tendency to divide problems to deal with them. 
- Container: refers to your tendency to hold complex problems to deal with them.

I have come up with names for the four positions that these create. They also mark where you feel more comfortable. The names are mostly to make things easier to remember and associate. 

- Carer: extensive and container, sees objects in the world and wants to protect and respect them. Here again person centre appears as an example. 
Dreamer: Extensive, container, feels, mixes, and follows metaphors, living between fantasy and reality. Jungian analysis shines here. 
- Sage: intensive and divider, more in the ethereal, but looking for the right concept and model for everything. Wilber is a good example here. 
- Explorer: Extensive and divider in the world, tries to understand in action, and learns techniques to operate on things. CBT and evidence-based. 

# Tradition/individuation

[Tradition/individuation](Profiles/personal_profile/individuation_tradition.md)

This group of questions aim to help you see how you feel about a therapy tradition. Here again, I made four questions for you:

- belonging: you want to be part of something bigger and belong to a community. 
- individuation: you want to find yourself and explore who you are more deeply.
- becoming: you want to explore and flow, follow your curiosity, and let the path guide you.
- development: you want to grow and reach new levels of maturity and understanding.

These four create four new groups:
- Artist: individuation and becoming, focusing on themselves and exploring as things emerge. 
- Warrior: individuation and development, focus on themselves, growing and improving.
- Lider/group: belonging and becoming. You would like to be guided by a leader who puts people together on a path focusing on connection. 
- Coach/team: belonging and development. You would like to be part of a team where all your skills are used, and someone helps you improve (or you being that person). 

In this case, I believe we move between these as we grow. But I prefer if the path follows: Group, Artist, Warrior, Team. Because belonging to a group gives you grounding and a sense of purpose. The artist helps you find who you are. The warrior to polish your skills, and the Team now puts those skills into something big. 


## Sections
{% directory_contents 'Profiles/personal_profile' order_by='order' as directory_contents %}
<ul>
{% for content in directory_contents %}
    <li><a href="/{{content.slug}}/">{{content.title}}</a></li>
    {% endfor %}
</ul>