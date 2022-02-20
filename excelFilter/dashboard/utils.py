import openpyxl
from pathlib import Path
from datetime import datetime

from . import config

DATASOURCE_PATH = Path(Path.home(), 'Documents', 'djangoprojects', 'excel-filter', 'datasource')

config_map = {
    'email-followup': config.FOLLOWUP_CONFIG,
    'email-file': config.FOR_FILE_CONFIG,
    'email-initial': config.INITIAL_CONFIG,
    'email-replies': config.EMAIL_REPLIES_CONFIG,
}

def get_file_data(menu_slug):
    file_data = {}
    file_config = config_map[menu_slug]
    if menu_slug == 'email-followup':
        file_data['rows'] = _get_data('A.xlsx', file_config['DATA_START_ROW'], file_config['NON_EMPTY_COL'])
        file_data['cols'] = file_config['TABLE_COLUMNS']
    elif menu_slug == 'email-file':
        file_data['rows'] = _get_data('B.xlsx', file_config['DATA_START_ROW'], file_config['NON_EMPTY_COL'])
        file_data['cols'] = file_config['TABLE_COLUMNS']
    elif menu_slug == 'email-initial':
        file_data['rows'] = _get_data('C.xlsx', file_config['DATA_START_ROW'], file_config['NON_EMPTY_COL'])
        file_data['cols'] = file_config['TABLE_COLUMNS']
    elif menu_slug == 'email-replies':
        file_data['rows'] = _get_data('D.xlsx', file_config['DATA_START_ROW'], file_config['NON_EMPTY_COL'])
        file_data['cols'] = file_config['TABLE_COLUMNS']
    return file_data

def update_context(menu_slug, context):
    file_data = get_file_data(menu_slug)
    context['rows'] = file_data['rows']
    context['cols'] = file_data['cols']
    context['data_controller_list'] = config.DATA_CONTROLLER_LIST
    context['nature_or_concern_list'] = config.NATURE_OR_CONCERN_LIST
    context['filter_columns'] = _get_filter_columns(menu_slug)
    return context

def get_dashboard_overall_summary_today():
    dashboard_summary = {}
    for key, file_config in config_map.items():
        today_rows = []
        rows = get_file_data(key)['rows']
        if key == 'email-replies':
            date_col = file_config['FILTER_FIELDS']['DATE_ENCODED_COL'] - 1
        else:
            date_col = file_config['FILTER_FIELDS']['DATE_OF_EMAIL_COL'] - 1
        for row in rows:
            if datetime.now().date() == row[date_col].date():
                today_rows.append(row)
        dashboard_summary[key] = today_rows
    return dashboard_summary

def get_dashboard_controller_summary_today():

    # structure = {
    #       'AAA': [[controller_info], {
    #           'email-followup': [rows],
    #           'email-file': [rows],
    #           'email-initial': [rows],
    #           'email-replies': [rows],
    #       }]
    #       'BBB': [[controller_info], {
    #           'email-followup': [rows],
    #           'email-file': [rows],
    #           'email-initial': [rows],
    #           'email-replies': [rows],
    #       }]
    # }
    controller_overall_summary_today = {}
    dashboard_summary = get_dashboard_overall_summary_today()
    for controller in config.DATA_CONTROLLER_LIST:
        controller_initials = controller[0]
        controller_summary = {}
        for key, rows in dashboard_summary.items():
            controller_rows = []
            for row in rows:
                if key == 'email-replies':
                    controller_col = config_map[key]['FILTER_FIELDS']['EVALUATOR_OR_SENDER_ENCODER'] - 1
                else:
                    controller_col = config_map[key]['FILTER_FIELDS']['REMARKS_COL'] - 1
                if controller_initials in _get_controller_list(row[controller_col]):
                    print(key, controller_initials, row)
                    print('--------------------------')
                    controller_rows.append(row)
            controller_summary[key] = controller_rows
        controller_overall_summary_today[controller_initials] = [controller, controller_summary]
    return controller_overall_summary_today

def get_controller_total_today():
    temp = get_dashboard_controller_summary_today()
    sums = []
    _sum = ''
    for key, values in temp.items():
        _sum = 0
        for key1, file_rows in values[1].items():
            _sum += len(file_rows)
        sums.append(_sum)
    return sums

# PRIVATE METHODS

def _get_controller_list(row_controller_str):
    return row_controller_str.split('/')

def _get_filter_columns(menu_slug):
    filter_columns = {}
    if menu_slug == 'email-followup':
        filter_columns = config.FOLLOWUP_CONFIG['FILTER_FIELDS']
    elif menu_slug == 'email-file':
        filter_columns = config.FOR_FILE_CONFIG['FILTER_FIELDS']
    elif menu_slug == 'email-initial':
        filter_columns = config.INITIAL_CONFIG['FILTER_FIELDS']
    elif menu_slug == 'email-replies':
        filter_columns = config.EMAIL_REPLIES_CONFIG['FILTER_FIELDS']
    return filter_columns

def _get_active_sheet(xlsx_file):
    xlsx_file_dir = DATASOURCE_PATH / xlsx_file
    wb_obj = openpyxl.load_workbook(xlsx_file_dir)
    sheet = wb_obj.active
    return sheet

def _get_data(file_name, data_row_start, non_empty_col):
    sheet = _get_active_sheet(file_name)
    rows = []
    for i, row in enumerate(sheet.iter_rows(values_only=True)):
        # Check if Value of Date of Email is not empty
        if i >= data_row_start - 1 and sheet.cell(i + 1, non_empty_col).value is not None:
            rows.append(row)
    return rows


