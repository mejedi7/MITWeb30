import json
from opensea import OpenseaAPI
from tokentype import TokenType

class NFTCollection :

    def __init__(self) :
        self.tokentype = TokenType.NOTERC
        self.contract_addresses = []
        self.attribute_dict = {}

    def populate_from_opensea(self, os_collection_slug) :
        api = OpenseaAPI(apikey="")
        self.attribute_dict[ 'os_collection_info' ] = api.collection(collection_slug=os_collection_slug)

        ## Populate the schema for the collection first as this will drive further decision making
        schema = self.attribute_dict[ 'os_collection_info' ][ 'collection' ][ 'primary_asset_contracts' ][0][ 'schema_name' ]

        match schema:
            case 'ERC20':
                self.tokentype = TokenType.ERC20
            case 'ERC721':
                self.tokentype = TokenType.ERC721
            case 'ERC1155':
                self.tokentype = TokenType.ERC1155
            case _:
                self.tokentype = TokenType.NOTERC



    def print_os_info(self):
        print( json.dumps( self.attribute_dict[ 'os_collection_info' ], indent=2) )

    def get_tokentype(self):
        return self.tokentype
