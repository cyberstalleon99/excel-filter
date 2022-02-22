from django.shortcuts import render
from . import utils, config

def genericView(request, menu_slug):
    if menu_slug == 'email-followup':
        return _emailForActionFollowUp(request, menu_slug)
    elif menu_slug == 'email-file':
        return _emailForActionForFile(request, menu_slug)
    elif menu_slug == 'email-initial':
        return _emailForActionInitial(request, menu_slug)
    elif menu_slug == 'email-replies':
        return _emailReplies(request, menu_slug)

def index(request):
    context = {
        'dashboard_active': 'active',
        'dashboard_overall_summary_today': utils.get_dashboard_overall_summary_today(request),
        'dashboard_controller_summary_today': utils.get_dashboard_controller_summary_today(request),
        'controller_total_today': utils.get_controller_total_today(request)
    }

    return render(request, 'dashboard/dashboard.html', context=context)

def _emailForActionFollowUp(request, menu_slug):
    context = {
        'page_title': 'For Followup',
        'sub_title': 'FOR FOLLOWUP',
        'followup_active': 'active',
        'date_fields': config.FOLLOWUP_CONFIG['DATE_FIELDS']
    }
    context = utils.update_context(request, menu_slug, context)
    return render(request, 'dashboard/generic.html', context=context)

def _emailForActionForFile(request, menu_slug):
    context = {
        'page_title': 'For File',
        'sub_title': 'FOR FILE',
        'for_file_active': 'active',
        'date_fields': config.FOR_FILE_CONFIG['DATE_FIELDS']
    }
    context = utils.update_context(request, menu_slug, context)
    return render(request, 'dashboard/generic.html', context=context)

def _emailForActionInitial(request, menu_slug):
    context = {
        'page_title': 'Initial',
        'sub_title': 'INITIAL',
        'initial_active': 'active',
        'date_fields': config.INITIAL_CONFIG['DATE_FIELDS']
    }
    context = utils.update_context(request, menu_slug, context)
    return render(request, 'dashboard/generic.html', context=context)

def _emailReplies(request, menu_slug):
    context = {
        'page_title': 'Email Replies',
        'sub_title': 'EMAIL REPLIES',
        'email_replies_active': 'active',
        'date_fields': config.EMAIL_REPLIES_CONFIG['DATE_FIELDS']
    }
    context = utils.update_context(request, menu_slug, context)
    return render(request, 'dashboard/generic.html', context=context)




