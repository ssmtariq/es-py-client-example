# import the Elasticsearch low-level client library
from elasticsearch import Elasticsearch

# Create Elasticsearch client
# domain name, or server's IP address, goes in the 'hosts' list
elastic_client = Elasticsearch(hosts=["http://192.168.5.86:9200"], headers={"Content-type": "application/json"})

# User makes a request on client side
user_request = "stdout"

# Take the user's parameters and put them into a Python
# dictionary structured like an Elasticsearch query:
# query_body = {"query":{"match":{"spanID":{"query":"3092576b6348ee13","type":"phrase"}}}}
query_body = {"query":{"match_all":{}}}

# call the client's search() method, and have it return results
print ("Request starts...")
result = elastic_client.search(index="jaeger-span-2022-04-11", body=query_body)
# resp = elastic_client.get(index="jaeger-span-2022-04-11", id="71tRGYABxhXkmNJK2rMi")

# headers={"kbn-version":"4.5.4"

# see how many "hits" it returned using the len() function
# print ("Response: ", resp)
print ("total hits:", len(result["hits"]["hits"]))
