# read_census_excel.py - tabulates county population and census tracts

import openpyxl
import pprint

print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

# TODO: Fill in county data with each county's population and tracts
print('Reading rows...')

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet[f'B{str(row)}'].value
    county = sheet[f'C{str(row)}'].value
    population = sheet[f'D{str(row)}'].value

    # Make sure the state and county dicts already exist
    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts': 0, 'population': 0})

    # Each row represents one census tract, so increment by one
    county_data[state][county]['tracts'] += 1
    # Increase county population by tract population
    county_data[state][county]['population'] += int(population)

print('Writing results...')

with open('census_2010.py', 'w') as result_file:
    result_file.write('all_data = ' + pprint.pformat(county_data))

print('Done.')

