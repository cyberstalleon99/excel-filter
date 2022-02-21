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

@register.filter(name='file_display_name')
def file_display_name(value, arg):
    if arg == "email-followup":
        return 'FOLLOWUP'
    if arg == "email-file":
        return 'FOR FILE'
    if arg == "email-initial":
        return 'INITIAL'
    if arg == "email-replies":
        return 'REPLY'
    return value

@register.filter(name='button_style')
def button_style(value, arg):
    if arg == "email-followup":
        return 'btn-primary'
    if arg == "email-file":
        return 'btn-success'
    if arg == "email-initial":
        return 'btn-danger'
    if arg == "email-replies":
        return 'btn-info'
    return value
