import redis

r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

# cleanup the sorted set named 'leaderboard'
r.delete("leaderboard")

# Add a member to the sorted set
r.zadd("leaderboard", {"alice": 100, "Bob": 200, "Carol": 150, "Tom": 300})


# Remove a memeber from the sorted set
r.zerm("leaderboard", "Carol")


# Retrieve the score of a member
alice_score = r.zscore("leaderboard", "Alice")
print("Alice's Score:", alice_score)


# Get the number of memebers in the sorted set
leaderboard_size = r.zcard("leaderboard")
print("Number of members in the leaderboard:", leaderboard_size)
# Number of members in the leaderboard: 3

# Count the number of members with scores between 120 and 200
members_in_range_count = r.zcount("leaderboard", 120, 200)
print(members_in_range_count)
# Number of members with scores between 120 and 200

# Count the number of members with score between 120 and 200(exclusive)
members_in_range_count = r.zcount("leaderboard", 120, "(200")
# Number of members with scores between 120 and 200(exclusive): 0
