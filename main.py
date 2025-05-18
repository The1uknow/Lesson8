#max = lambda a, b: (a if a > b else b)
#print(max(3, 8))

# p = lambda a: a*4
# print(p(2))

import requests

i = 'https://icanhazip.com/'
print(requests.get(i).text)

#