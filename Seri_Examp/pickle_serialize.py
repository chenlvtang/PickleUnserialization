import pickle
import pickletools

class Chenlvtang:
    name = ""
    id = 123
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def printf(self):
        print("Hello")

if __name__ == "__main__":
    chen = Chenlvtang("chenlvtang", 8003119052)
    
    #file
    # with open("seri_test", "wb") as file:
    #     pickle.dump(chen, file) #serialize
    # with open("seri_test", "rb") as file:
    #     c = pickle.load(file) #unserialize
    #     c.printf()

    #bytes
    seri_test =  pickle.dumps(chen, 0)
    print("String Serialize:  \n")
    print(seri_test)
    pickletools.dis(seri_test)
    # c = pickle.loads(seri_test)