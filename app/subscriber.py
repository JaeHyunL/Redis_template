import redis
import threading

# Connect to Redis Server

r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

# # Subscribe to a channel
# pubsub = r.pubsub()
# pubsub.subscribe("my_channel")


# # Function to handle message recevied from Redis Pub/Sub
# def handle_message(message):
#     print(f"Message received: {message['data']}")


# # Start a separate thread to listen for message
# def listen_for_message():
#     for message in pubsub.listen():
#         if message["type"] == "message":
#             handle_message(message)


# thread = threading.Thread(target=listen_for_message)
# thread.start()

# PSub
pattern = "my_*"
pubsub = r.pubsub()
pubsub.psubscribe(pattern)


# Start a separate thread to listen for message
def listen_for_pmessage():
    for message in pubsub.listen():
        if message["type"] == "pmessage":
            print(
                f"Pattern: {message['pattern']}, Channel: {message['channel']}, Message: {message['data']}"
            )


thread = threading.Thread(target=listen_for_pmessage)
thread.start()
