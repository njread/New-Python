from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

location = input("what city are you looking for a resteraunt ")

def busines_locatons(term, location):
	auth = Oauth1Authenticator(
	    consumer_key="mUp8NqSZCv9WvRZZb2yVcw",
	    consumer_secret="oofNJJKjpU4HVOCksIOeknjT1nM",
	    token="tGdfkcrrJY6rL_8o_KmGkF9zy0PwTVaW",
	    token_secret="anbTo3CXxHdZMOTP5L-VV9L2EoU"
	)

	client = Client(auth)


	params = {
	    'term': 'food',
	    'lang': 'en',
	    
	}
	

	response = client.search(location, ** params)

	for business in response.businesses:
	    print(business.name)
	    
busines_locatons(location, "resteraunt")