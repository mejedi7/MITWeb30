from Historic_Crypto import HistoricalData
import re

class ETHHistory :
    def __init__(self) :
        ## Capture all-time ETH history on a day granularity
        self.eth_data_frame = HistoricalData('ETH-USD', 86400, '2016-10-14-00-00').retrieve_data()
#       self.eth_data_frame = HistoricalData('ETH-USD', 86400, '2022-08-01-00-00').retrieve_data()
#       self.eth_dict = self.eth_data_frame.to_dict('index')

    def get_eth_value_on_date( self, date ) :
        ## Date input must be yyyy-mm-dd
        if( re.fullmatch( "^\d\d\d\d-\d\d-\d\d$", date ) ) :
            return self.eth_data_frame.loc[ date ,"close" ] 
        else :
            print( "Incorrect Date Format, must be yyyy-mm-dd" )

#   def print_eth_history( self ) :
#       for timestamp in self.eth_dict.keys() :
#           close_value = self.eth_dict[ timestamp ][ 'close' ]
#           print( f'{timestamp} => {close_value}')
