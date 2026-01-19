import pickle

class A: 
    pass
pickle.dump(A(),open('c.pkl','wb'))
print('Never unpickle data from untrusted source')