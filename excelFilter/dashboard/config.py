FOLLOWUP_CONFIG = {
    'TABLE_COLUMNS': [
        'PCC Code No.',
        'Sub Code',
        'Name of Caller',
        'Email Address',
        'Date of Email',
        'Referred to Agency',
        'Date Sent to Agency',
        'Date Evaluated',
        'AO/E-SENDER/DATA ENCODER',
        'ACTION OFFICER',
        'DATE OF INDORSEMENT'],
    'DATE_FIELDS': [5, 7, 8, 11], # Date of Email, Date Sent to Agency, Date Evaluated, DATE OF INDORSEMENT
    'DATA_START_ROW': 8, # Row where data starts in the excel file
    'NON_EMPTY_COL': 5, # Column in the excel file that can not be empty
    'HIDDEN_COLUMNS': [6, 9, 10, 11],
    'FILTER_FIELDS': {
        'DATE_OF_EMAIL_COL': 5,
        'DATE_EVALUATED_COL': 8,
        'AO_E_SENDER_DATA_ENCODER': 9,
        'NATURE_OR_CONCERN_COL': 0,
        'REFERRED_TO_AGENCY_COL': 0,
    }
}

FOR_FILE_CONFIG = {
    'TABLE_COLUMNS': [
        'Item No.',
        'Code No.',
        'Sub Code',
        'Name of Caller',
        'Email Address',
        'Date of Email',
        'For File',
        'Date Evaluated',
        'AO/E-SENDER/DATA ENCODER'],
    'DATE_FIELDS': [6, 7, 8], # Date of Email, Date Sent to Agency, Date Evaluated
    'DATA_START_ROW': 8,  # Row where data starts in the excel file
    'NON_EMPTY_COL': 6,  # Column in the excel file that can not be empty
    'HIDDEN_COLUMNS': [7, 8 ,9 ,10 ,11],
    'FILTER_FIELDS': {
        'DATE_OF_EMAIL_COL': 6,
        'DATE_EVALUATED_COL': 8,
        'AO_E_SENDER_DATA_ENCODER': 9,
        'NATURE_OR_CONCERN_COL': 0,
        'REFERRED_TO_AGENCY_COL': 0,
    }
}

INITIAL_CONFIG = {
    'TABLE_COLUMNS': [
        'PCC Code No.',
        'Sub Code',
        'Name of Caller',
        'Email Address',
        'Date of Email',
        'Nature/Concern',
        'Referred to Agency',
        'Date Sent to Agency',
        'Ack.',
        'Date Evaluated',
        'AO/E-SENDER/DATA ENCODER',
        'Action Officer',
        'Date of Endorsement',
        'Status',
        'Date of Email Reply'],
    'DATE_FIELDS': [5, 8, 10, 13, 15], # Date of Email, Date Sent to Agency, Date Evaluated, DATE OF INDORSEMENT, Date of Email Reply
    'DATA_START_ROW': 8,  # Row where data starts in the excel file
    'NON_EMPTY_COL': 5,  # Column in the excel file that can not be empty
    'HIDDEN_COLUMNS': [10,11],
    'FILTER_FIELDS': {
        'DATE_OF_EMAIL_COL': 5,
        'DATE_EVALUATED_COL': 10,
        'AO_E_SENDER_DATA_ENCODER': 11,
        'NATURE_OR_CONCERN_COL': 6,
        'REFERRED_TO_AGENCY_COL': 7,
    }
}

EMAIL_REPLIES_CONFIG = {
    'TABLE_COLUMNS': [
        'Item No.',
        'Name of Caller',
        'Code No.',
        'Agency',
        'Email Address of Reply',
        'Signatory',
        'Date of  Email',
        'Date Received',
        'Date Encoded',
        'For Ack/ For Sending to Client/ Ack from Agency/ For File/CC Only/To PCC',
        'Reason/s',
        'Evaluator/Sender/ Encoder'],
    'DATE_FIELDS': [7, 8, 9], # Date of Reply, Date Received, Date Encoded
    'DATA_START_ROW': 6,  # Row where data starts in the excel file
    'NON_EMPTY_COL': 7,  # Column in the excel file that can not be empty
    'HIDDEN_COLUMNS': [],
    'FILTER_FIELDS': {
        'DATE_OF_EMAIL_COL': 7,
        'DATE_EVALUATED_COL': 0,
        'DATE_ENCODED_COL': 9,
        'EVALUATOR_OR_SENDER_ENCODER': 12,
        'NATURE_OR_CONCERN_COL': 0,
        'REFERRED_TO_AGENCY_COL': 0,
    }
}

REFERRED_TO_AGENCY_LIST = [
    'DSWD', 'DOH', 'DOJ', 'PHIL ARMY'
]

NATURE_OR_CONCERN_LIST = [
    'MED A', 'MED B', 'MED C', 'LEGAL',
    'IRC A', 'IRC B'
]

DATA_CONTROLLER_LIST = [
    # [INITIALS,    INITIAL_WITH_LASTNAME,      FULLNAME,               DESIGNATION],       PROFILE_PIC
    ['AAA',         'AAAngelo',                 'Andrew A. Angelo',     'Officer 1',        'AAA.jpg'],
    ['BBBB',        'BBBlue',                   'Bon B. Blue',          'Officer 2',        'BBB.jpg'],
    ['CCC',         'CCChocolate',              'Cherry C. Chocolate',  'Officer 3',        'CCC.jpg'],
    ['DDD',         'DDDarrymore',              'Drew D. Darrymore',    'Officer 4',        'DDD.jpg'],
    ['GARRY',         'GGGanda',                'Gigi G. Ganda',        'Officer 5',        'DDD.jpg'],
]

