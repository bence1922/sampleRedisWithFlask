from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/healthz')
def healthz():
    return "ok"

@app.route('/alert')
def increment():
    redis.incr('counter')
    return "Counter was succesfully incremented!"

@app.route('/counter')
def printCounter():
    counter = str(redis.get('counter'),'utf-8')
    return {
        "counter" : counter,
    }

@app.route('/version')
def printShortCommitHash():
    return {
        "shortCommitHash":os.getenv('GIT_COMMIT'),
    }
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)