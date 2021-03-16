import pickle
mylist = [1, 2, 3, 4]
service = pickle.dumps(mylist)
print(service)