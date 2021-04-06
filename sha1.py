import hashlib
str = "Definitely my original name"
result = hashlib.sha1(str.encode())
print(result.hexdigest())
