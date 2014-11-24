import oauth2 as oauth
import urllib2 as urllib
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = "pqQSGDYC9TlXYxT6mgjb3si4F"
api_secret = "YspqL96gk3AEKcE5230TrbYahz28RHdtVW3UrTwMlV2QAcKvEK"
access_token_key = "18301790-nvMfMrm0PYvDYfnaYHSehYEfZtZDkC2IaJ7OQrPZI"
access_token_secret = "P3b3K5LMfSWH1QiwgNrD0ewtAlgeFOb2wrGCO83OVIzvl"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
#
#   Cities={"Hyderabad":"17.593743,78.206172,17.237332,78.673091",
#  "Banglore":"13.147981,77.342548,13.147981,77.342548",
# "Newyork":"40.883413,-74.288367,40.583716,-73.725318",     
# "London":"51.738328,-0.606970,51.311118,0.392786",
# "Mumbai":"19.272273,72.783700,18.999818,72.925149",    
# "San fracisco":"37.835560,-122.495965,37.711270,-122.272118", 
# "Paris":"48.892503,2.248183,48.822932,2.483702",
# "sydney":"-33.438976,150.614815,-34.137468,151.095467", 
# "Chicago":"42.014586,-87.960122,41.635948,-87.490456",
# "Manchester":"53.536363,-2.410360,53.411305,-2.056051"}
#
#
# To get place ids by giving lattitude and longitudes for a city
#   url = "https://api.twitter.com/1.1/geo/search.json?lat=17.3660&long=78.4760&accuracy=50000&max_results=100000&granularity=city"
#
#
# To get tweets by giving place id and dates
      url = "https://api.twitter.com//1.1/search/tweets.json?q=place:243cc16f6417a167 since:2014-11-16 until:2014-11-17&lang=en&result_type=mixed&count=100"
      parameters = []
      response = twitterreq(url, "GET", parameters)
    #   temp = json.loads(response.strip())
    #   print temp
      for line in response:
    #       if len(line) > 2:
            temp = json.loads(line.strip())
            statuses = temp["statuses"]
            t = ""
            for status in statuses:
                t += str(status) +"\n"
            print t
            with open('statuses.json', 'w') as outfile:
#                 for status in statuses:
                json.dump(statuses, outfile)


if __name__ == '__main__':
  fetchsamples()
