from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def last_url(value:str,place=-1):
    place = int(place)
    value = value.strip()
    value = value.split("/")
    value = value[place]
    return value

@register.filter
@stringfilter
def url_section(value:str,until=-1):
    until = int(until)
    value = value.strip()
    value = value.split("/")
    values = value[0:until]
    url = "/"
    for v in values:
        part = f"{v}/"
        url += part
    return url


@register.inclusion_tag("tags/breadcrumb.html",takes_context=True)
def breadcrumb(context):
    url = context["slug"]
    url = str(url)
    broken_url = url.strip()
    broken_url = broken_url.split("/")
    url_dic = {}
    i = 0
    for u in broken_url:
        i += 1
        section = url_section(i)
        section_dic = {u:section}
        url_dic.update(section_dic)
    return url_dic


