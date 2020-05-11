from yelpapi import YelpAPI
import argparse
from pprint import pprint
# from  jsonmerge import merge
import json
import csv
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

argparser = argparse.ArgumentParser(description='Example Yelp queries using yelpapi. '
                                                'Visit https://www.yelp.com/developers/v3/manage_app to get the '
                                                'necessary API keys.')
argparser.add_argument('api_key', type=str, help='Yelp Fusion API Key')
args = argparser.parse_args()

yelp_api = YelpAPI(args.api_key)

"""
    Example search by location text and term. 
    
    Search API: https://www.yelp.com/developers/documentation/v3/business_search
"""
# print('***** 5 best food places in San Francisco, CA *****\n{}\n'.format("yelp_api.search_query(term='food,restaurants', "
                                                                             # "location='san francisco, ca', sort_by='rating', "
                                                                             # "limit=5)"))
# zipcode = [94102,94103,94104,94105,94107,94108,94109,94110,94111,94112,94114,94115,94116,94117,94118,94121,94122,94123,94124,94127,94128,94129,94130,94131,94132,94133,94134,94143,94158,94188]
responselist = []
result = {}
with open('Output.csv', 'rb') as csvfile:
	business_curr = csv.reader(csvfile, delimiter=',')
	count = 0
	for row in business_curr:
		response = yelp_api.search_query(term=row[1], location=row[3], limit=1)
		with open(row[0]+'.json', 'w') as f:
			json.dump(response, f)	