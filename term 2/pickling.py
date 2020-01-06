import pickle, shelve, math

variety = ["sweet", "bread and butter", "dill"]
shape = ['whole','spear','chips']
brands =['claussen', 'heinz','vlassic']
##
##f = open("pickles.dat", "wb")
##pickle.dump(variety, f)
##pickle.dump(shape, f)
##pickle.dump(brands, f)
##f = open("pickles.dat", 'rb')
##variety = pickle.load(f)
##shape = pickle.load(f)
##brands = pickle.load(f)
##
##print(variety)
##print(shape)
##print(brands)
##
##f.close()

s = shelve.open("pickles.dat")
s["variety"] = ['sweet', 'bread and butter', 'dill']
s["shape"] = ['whole', 'spear', 'chips,]
