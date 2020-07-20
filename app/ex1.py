from app import app
import redis
from rq import Queue
from flask import request, Flask
import time

r = redis.Redis()
q = Queue(connection=r)

def background_task(n):
  delay = 2
  print("Task Running")
  print(f"Simulating {delay} seconds delay")

  time.sleep(delay)

  print(len(n))

  print("Task Complete")

  return len(n)

@app.route("/task")
def add_task():
  if request.args.get("n"):
    job = q.enqueue(background_task, request.args.get("n"))

    q_len = len(q)

    return f"Task {job.id} added to queue at {job.enqueued_at}. {q_len} tasks in the queue"

  return "No value for n"

