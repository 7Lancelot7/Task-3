import hashlib

def getMD5Hash(s):
    return (hashlib.md5(s.encode()).hexdigest())
    
x=getMD5Hash('Insteresting reaction')
print(x)
ans = hashlib.sha3_256()
ans.update(b"Insteresting reaction")
print(ans.hexdigest())
