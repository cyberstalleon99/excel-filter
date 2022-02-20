from django import template
register = template.Library()

@register.filter(name='ifinlist')
def ifinlist(value, list):
    return True if value in list else False

@register.filter(name='listvalue')
def listvalue(index, list):
    return list[index-1]

@register.filter
def toStr(integer):
    return str(integer)