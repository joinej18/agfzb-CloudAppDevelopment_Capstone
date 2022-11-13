import requests
import json
# import related models here
from .models import CarDealer
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        #Call get method of requests library with URL and parameters
        response = requests.get(url, params=kwargs, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
    except
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data
# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, **kwargs, json_payload)
    try: 
        response = requests.post(url, params=kwargs, json=json_payload)
    #return ?

# Create a get_dealers_from_cf method to get dealers from a cloud function
def get_dealer_reviews_from_cf(url, **kwargs):
    results = []
    id = kwargs.get("id")
    if id:
        json_result = get_request(url, id=id)
    else:
        json_result = get_request(url)

    if json_result:
        reviews = json_result["body"]["data"]

        for dealer_review in reviews:
            dealer_review = reviews["docs"][0]
            
            review_obj = DealerReview(dealership=dealer_review["dealership"],
                                   name=dealer_review["name"],
                                   purchase=dealer_review["purchase"],
                                   review=dealer_review["review"])
            if "id" in dealer_review:
                review_obj.id = dealer_review["id"]
            if "purchase_date" in dealer_review:
                review_obj.purchase_date = dealer_review["purchase_date"]
            if "car_make" in dealer_review:
                review_obj.car_make = dealer_review["car_make"]
            if "car_model" in dealer_review:
                review_obj.car_model = dealer_review["car_model"]
            if "car_year" in dealer_review:
                review_obj.car_year = dealer_review["car_year"]
            
            sentiment = analyze_review_sentiments(review_obj.review)
            print(sentiment)
            review_obj.sentiment = sentiment
            results.append(review_obj)

    return results
    
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers 
        
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in 'doc' object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results.review_obj.sentiment = analyze_review_sentiments(review_obj.review)

# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
def analyze_review_sentiments(text):
    params = dict()
  params["text"] = kwargs["text"]
  params["version"] = kwargs["version"]
  params["features"] = kwargs["features"]
  params["return_analyzed_text"] = kwargs["return_analyzed_text"]
  response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



