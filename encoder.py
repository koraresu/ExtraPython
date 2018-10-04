#sha y crypto: puedes hacer un encoder tu mismo haciendo uso de la libreria base64, sha y crypto.
import hashlib
import base64
def convert_string_to_hash(word, algorithm=[]):
	word = str.encode(word)
	dictionary = {}
	for i in algorithm:
		try:
			dictionary[ i ] = getattr(hashlib, i)(word).hexdigest()
		except:
			pass
	return dictionary
t = input('Text:')
alg = input('algorithms:') # md5,sha1,sha256, sha3_256,shake_256,sha 
alg = alg.split(',')
print( convert_string_to_hash( t , alg ) )


