#!/usr/bin/python3

import sys
import json

import pygsheets

from eth_history import ETHHistory

## Parse Command Line Arguments
debug = 0
live = 0

for argument in sys.argv[1:] :
    if( argument == '--debug' ) :
        debug = 1
    if( argument == '--live' ) :
        live = 1

## Load the Ethereum History up to now. We will keep this object around to help populate USD pricing for our collections
#eth_hist_obj = ETHHistory()

## Load the MIT Web 30 Tradesheet from the Google API
tradesheet_filename = 'Web 3.0 Trade Sheet Dev'

if(live) : tradesheet_filename = 'Web 3.0 Trade Sheet'

print( tradesheet_filename )

google_drive_connection = pygsheets.authorize()

## Now that we have the input data sheet open, we need to iterate down it using the tags to pull in our desired collections
input_worksheet_title = 'Input Data'
input_worksheet_data_row = 2
input_worksheet_data_column = 'A'

input_worksheet_parse_begin = 'BEGIN PARSE'
input_worksheet_parse_end = 'END PARSE'

bluechips_worksheet_title = 'Blue Chips'
inventory_worksheet_title = 'Inventory List'

spreadsheet = google_drive_connection.open(tradesheet_filename)
input_worksheet = spreadsheet.worksheet_by_title(input_worksheet_title)

## Collection tags begin at cell A2 and progress down until we get to the end
while( 1 ) :
    formatted_string = f"{input_worksheet_data_column:s}{input_worksheet_data_row:d}"

    cell_value = input_worksheet.get_value(formatted_string)

    if( cell_value ) :
        if( debug ) :
            print( cell_value )

        input_worksheet_data_row += 1
    else :
        break
