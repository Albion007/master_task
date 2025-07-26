from flask import Flask, request
import logging
import sys

app = Flask(__name__)

# Konfigurimi i logimit që shkon në stdout (që lexohen nga Cloud Logging Agent)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('flask-app')

@app.route('/')
def home():
    logger.info("Accessed home page.")
    return 'Hello from Flask on port 3000!!'

@app.route('/hello/<name>')
def hello(name):
    logger.info(f"Greeting user: {name}")
    return f'Hello, {name}!'

@app.route('/error')
def error():
    logger.error("Simulated error occurred!")
    return "Something went wrong!", 500

@app.route('/log-test')
def log_test():
    logger.debug("This is a DEBUG log")
    logger.info("This is an INFO log")
    logger.warning("This is a WARNING log")
    logger.error("This is an ERROR log")
    return "Log levels tested! Check Cloud Logging."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
