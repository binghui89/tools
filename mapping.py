# Including all future techs
tech_map = {
    'ENGACC05':     'NGA',
    'ENGACT05':     'NGA',    
    'ENGAACC':      'NGA',
    'ENGAACT':      'NGA',
    'ENGACCR':      'NGA',
    'ENGACTR':      'NGA',
    'ENGASTMR':     'NGA',
    'ENGACCCCS':    'NGA',
    'ECOALSTM':     'COA',    
    'ECOALIGCC':    'COA',
    'ECOALIGCCS':   'COA',
    'ECOALOXYCS':   'COA',
    'ECOASTMR':     'COA',
    'ECOALSTM_b':   'COA',    
    'ECOALIGCC_b':  'COA',
    'ECOALIGCCS_b': 'COA',
    'ECOASTMR_b':   'COA',
    'ECOALSTMCCS':  'COA',
    'EDSLCCR':      'OIL',
    'EDSLCTR':      'OIL',
    'ERFLSTMR':     'OIL',
    'EURNALWR':     'NUC',
    'EURNALWR15':   'NUC',
    'EBIOIGCC':     'BIO',
    'EBIOSTMR':     'BIO',
    'EGEOBCFS':     'GEO',
    'EGEOR':        'GEO',
    'ESOLPVCEN':    'SOL',
    'ESOLSTCEN':    'SOL',
    'ESOLTHR':      'SOL',
    'ESOLPVR':      'SOL',
    'ESOLPVDIS':    'SOL',
    'EWNDR':        'WND',
    'EWNDON':       'WND',     
    'EWNDOFS':      'WND',
    'EWNDOFD':      'WND',
    'EHYDCONR':     'HYD',
    'EHYDREVR':     'PUM', # Pumped hydro
    'EMSWSTMR':     'BIO',
    'ELFGICER':     'BIO',
    'ELFGGTR':      'BIO',
    'EHYDGS':       'GSR',
    'EE':           'EE',
    'EURNSMR':      'NUC',
    }

emis_map = {
    'E_FGD_COABH_N':                'SO2 control',
    'E_FGD_COABH_R':                'SO2 control',
    'E_FGD_COABM_N':                'SO2 control',
    'E_FGD_COABM_R':                'SO2 control',
    'E_FGD_COABL_N':                'SO2 control',
    'E_FGD_COABL_R':                'SO2 control',
    'E_LNBSNCR_COAB_R':             'NOx control',
    'E_LNBSNCR_COAB_N':             'NOx control',
    'E_LNBSCR_COAB_R':              'NOx control',
    'E_LNBSCR_COAB_N':              'NOx control',
    'E_LNB_COAB_R':                 'NOx control',
    'E_LNB_COAB_N':                 'NOx control',
    'E_SCR_COAB_R':                 'NOx control',
    'E_SCR_COAB_N':                 'NOx control',
    'E_SNCR_COAB_R':                'NOx control',
    'E_SNCR_COAB_N':                'NOx control',
    'E_CCR_COAB':                   'CO2 control',
    'E_CCR_COALIGCC_N':             'CO2 control',
    'E_CCR_COALSTM_N':              'CO2 control',
    'E_CCR_NGAACC_N':               'CO2 control',
    }

# http://www.rapidtables.com/web/color/RGB_Color.htm
color_map = {
    'NGA':         [0.7, 0.7, 0.7],
    'COA':         [0.0, 0.0, 0.0],
    'OIL':         [1.0, 0.0, 0.0],
    'NUC':         [0.6, 0.0, 0.8],
    'BIO':         [0.0, 1.0, 0.0],
    'GEO':         [1.0, 0.5, 0.3],
    'SOL':         [1.0, 1.0, 0.0],
    'WND':         [0.0, 0.0, 1.0],
    'HYD':         [0.4, 0.6, 0.9],
    'PUM':         [0.4, 0.6, 0.9],
    'GSR':         [1.0, 0.0, 0.0],
    'CO2 control': 'black',
    'NOx control': [0.5, 0.0, 0.0],
    'SO2 control': 'green',
    'EE':          'white',
    'other':       [1.0, 1.0, 1.0]
    }

edge_map = {
    'NGA':         [0.7, 0.7, 0.7],
    'COA':         [0.0, 0.0, 0.0],
    'OIL':         [1.0, 0.0, 0.0],
    'NUC':         [0.6, 0.0, 0.8],
    'BIO':         [0.0, 1.0, 0.0],
    'GEO':         [1.0, 0.5, 0.3],
    'SOL':         [1.0, 1.0, 0.0],
    'WND':         [0.0, 0.0, 1.0],
    'HYD':         [0.4, 0.6, 0.9],
    'PUM':         [0.4, 0.6, 0.9],
    'GSR':         [1.0, 0.0, 0.0],
    'CO2 control': 'black',
    'NOx control': [0.5, 0.0, 0.0],
    'SO2 control': 'green',
    'EE':          'black',
    'other':       [1.0, 1.0, 1.0]
    }

hatch_map = {
    'NGA':   None,
    'COA':   None,
    'OIL':   None,
    'NUC':   None,
    'BIO':   None,
    'GEO':   None,
    'SOL':   None,
    'WND':   None,
    'HYD':   None,
    'PUM':   '++',
    'GSR':   None,
    'EE':    '//',
    'other': '++'
    }

category_map = {
    'Bioenergy':          'BIO',
    'Coal':               'COA',
    'Oil':                'OIL',
    'EE':                 'EE',
    'Geothermal':         'GEO',
    'Hydro':              'HYD',
    'Pumped hydro':       'PUM',
    'Natural gas':        'NGA',
    'Solar PV':           'SOL',
    'Nuclear':            'NUC',
    'Wind':               'WND',
    'Emission reduction': 'Emission reduction',
    'other':              'other',
    }

color_map['Emission reduction'] = 'white'
edge_map['Emission reduction'] = 'black'
hatch_map['Emission reduction'] = None

# Break-even cost graphs
sen_color_map = {
    'IC':    [0.9, 0.9, 0.9],
    'L':     'black',
    'R':     'black',
    'H':     'black',
    'CPP-L': 'green',
    'CPP-R': 'green',
    'CPP-H': 'green',
    'cap-L': 'green',
    'cap-R': 'green',
    'cap-H': 'green',
}

sen_lstyle_map = {
    'IC':    None,
    'L':     '--',
    'R':     '-',
    'H':     'dotted',
    'CPP-L': '--',
    'CPP-R': '-',
    'CPP-H': 'dotted',
    'cap-L': '--',
    'cap-R': '-',
    'cap-H': 'dotted',
}

sen_marker_map = {
    'IC':    None,
    'L':     's',
    'R':     's',
    'H':     's',
    'CPP-L': 's',
    'CPP-R': 's',
    'CPP-H': 's',
    'cap-L': 's',
    'cap-R': 's',
    'cap-H': 's',
}
