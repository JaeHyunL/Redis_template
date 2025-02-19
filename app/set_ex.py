import redis

r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

r.sadd("myset", 1, 1, 2, 3, 4, 5)
print(r.sismember("myset", 3))

r.srem("myset", 2, 4)
print(r.smembers("myset"))

print(r.scard("myset"))

r.sadd("set1", 1, 2, 3, 4)
r.sadd("set2", 3, 4, 5, 6)

intersection = r.sinter("set1", "set2")

intersection = r.sinter("set1", "set2")
print("intersection:", intersection)

# Set union
union = r.sunion("set1", "set2")
print("union:", union)

diff = r.sdiff("set1", "set2")
print("Difference:", diff)

# Compute the union of set1 and set2 and store the result in a new set named union_result
r.sunionstore("union_result", "set1", "set2")
print("UnionResult:", r.smembers("union_result"))

# Compute the difference between set1 and set2 and store the result in a new set named diff_result
r.sdiffstore("diff_result", "set1", "set2")
print("Difference Result", r.smembers("diff_result"))

# Compute the intersection of set1 and set2 and store the result in a new set named inter_result
r.sinterstore("inter_result", "set1", "set2")
print("interSection_result", r.smembers("inter_result"))
