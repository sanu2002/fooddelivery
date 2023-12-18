import  requests


# url='http://127.0.0.1:8000/admin/vendor/vendor/3/change/'
# url='http://127.0.0.1:8000/admin/vendor/vendor/3/change/'
url='http://127.0.0.1:8000/admin/vendor/vendor/3/change/'


get_response=requests.post(url)

print(get_response.headers)
print(get_response)