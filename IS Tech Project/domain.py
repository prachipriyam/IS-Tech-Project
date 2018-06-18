#Code for domain retrieval of entered url
from urllib.parse import urlsplit
url = input ('Enter url: ')
base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
print(base_url) 
