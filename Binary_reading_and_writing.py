import pickle
f = open("pick.dat", 'wb')
pickle.dump(11, f)
pickle.dump("this is a line", f)
pickle.dump([1,2,3,4], f)
f.close()

#reading data
f = open('pick.dat', 'rb')
pickle.load(f)
pickle.load(f)
pickle.load(f)

f.close()