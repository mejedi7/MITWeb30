#!/usr/bin/python3

from tokentype import TokenType
from nftcollection import NFTCollection

my_nft_collection = NFTCollection()

my_nft_collection.populate_from_opensea('proof-collective')

assert (my_nft_collection.get_tokentype() == TokenType.ERC721), "Error on TokenType"
#print( my_nft_collection.get_tokentype() )
