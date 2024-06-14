import json
import redis
import time

redis_conn = redis.Redis(
    host='localhost',
    port=6379,
    charset="utf-8",
    decode_responses=True
    )
# while True:
# data = {"message": "Hello from Sender! 3", "timestamp": time.time()}
data = { "to" : "deneme@hotmail.com", "subject" : "Deneme Baslik", "body" : "<b>Selam</b>" }
json_data = json.dumps(data)
print("sending3..")
# JSON verisini Redis'e gönder
redis_conn.publish("channel", json_data)

    # time.sleep(60)
