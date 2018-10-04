#sha y crypto: puedes hacer un encoder tu mismo haciendo uso de la libreria base64, sha y crypto.


import base64
import hashlib
user_input = input("Enter string to encode")
result = base64.b64encode(hashlib.sha1(user_input))
print(result)