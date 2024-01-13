from django import template
from itertools import groupby
from operator import itemgetter
from django.utils.translation import get_language

register = template.Library()

@register.filter
def sort_skills(skills, order_list):
    order_dict = {name.lower(): index for index, name in enumerate(order_list)}
    skill_list = sorted(({'category': skill.category.name, 'skill': skill} for skill in skills), key=itemgetter('category'))
    skill_groups = [{'grouper': k, 'list': list(g)} for k, g in groupby(skill_list, key=itemgetter('category'))]
    return sorted(skill_groups, key=lambda group: order_dict.get(group['grouper'].lower(), 999))


@register.filter
def find_replace(string, find_replace=",|_"):
    find, replace = find_replace.split("|")
    return string.replace(find, replace)
