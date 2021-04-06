import hashlib
str = "Definitely my original name"
result = hashlib.md5(str.encode())
print(result.hexdigest())
