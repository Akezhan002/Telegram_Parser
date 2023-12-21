import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0
)
data = {
  "title": "New_Post",
  "content": "Some_Content",
  "likes": 12
}
print(redis_client.set(name="Posts", value="{\n  \"title\": \"{New_Post}\",\n  \"content\": \"Some_Content\",\n  \"likes\": 12\n}"))
print(json.loads(redis_client.get(name="Posts")))


redis_client.close()