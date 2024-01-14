from django import template
from itertools import groupby
from operator import itemgetter

register = template.Library()

@register.filter
def sort_skills(skills, order_list):
    order_dict = {name.lower(): index for index, name in enumerate(order_list)}
    skill_list = sorted(({'category': skill.category.name, 'skill': skill} for skill in skills), key=itemgetter('category'))
    skill_groups = [{'grouper': k, 'list': list(g)} for k, g in groupby(skill_list, key=itemgetter('category'))]
    return sorted(skill_groups, key=lambda group: order_dict.get(group['grouper'].lower(), 999))

@register.filter
def filter_skills(skills, filter):
    list_skills = filter.split(',')
    return sorted([skill for skill in skills if skill.name in list_skills], key=lambda skill: list_skills.index(skill.name))

@register.filter
def find_replace(string, find_replace=",|_"):
    find, replace = find_replace.split("|")
    return string.replace(find, replace)
