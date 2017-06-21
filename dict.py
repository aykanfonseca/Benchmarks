import timeit

# Shows that dictionaries are drastically faster than lists.
a = timeit.timeit('tmp=[]; tmp.append(True); x=tmp[0]', number = 20000000)
b = timeit.timeit('tmp={}; tmp[0]=True; x=tmp[0]', number = 20000000)

print(a)
print(b)

print("Speed up: " + str(((a / b) - 1) * 100) + "%")
