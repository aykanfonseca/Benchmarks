import timeit

# Partition is faster as it returns a tuple which Python reuses.
a = timeit.timeit('str("chocolate)".partition(")")[0])', number = 2000000)
# Split is slower as it returns a list.
b = timeit.timeit('str("chocolate)".split(")", 1)[0])', number = 2000000)

print(a)
print(b)

print("Speed up: " + str(((b / a) - 1) * 100) + "%")
