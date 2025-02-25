import redis
import time

r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

stream_key = "mystream"

r.delete(stream_key)

# Custom Message ID to start the stream
custom_message_id = "1000-0"

# Add the first message with the custom message ID
first_message = {"field1": "value1", "field2": "value2"}
r.xadd(stream_key, first_message, id=custom_message_id)

# Add more messages to the stream (subsequent message will have auto-generated IDs)
messages = [
    {"field1": "value3", "field2": "value4"},
    {"field1": "value5", "field2": "value6"},
]

for message in messages:
    r.xadd(stream_key, message)


stream_entries = r.xread({stream_key: "0"}, count=10)
for stream, messages in stream_entries:  # type: ignore
    for message_id, fields in messages:
        print(f"Message ID: {message_id}, Fields: {fields}")

# Get the length of the stream
stream_length = r.xlen(stream_key)
print(f"Length of stream '{stream_key}': {stream_length}")
