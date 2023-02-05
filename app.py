import time
import random
from flask import Flask, render_template, jsonify, redirect, url_for

app = Flask(__name__)
counter = 0

timer_running = False


@app.route('/')
def render_home():
    return render_template('index.html')


@app.route('/start_tracking')
def start_tracking():
    return render_template('counter.html')


@app.route('/get_time')
def get_time():
    """
    Being invoked automatically with ajax requests
    Updates the global variable counter that tracks usage
    return the counter value to client
    """
    global counter
    counter = random.randint(1, 20) # where we implement the timer functionality
    return jsonify({"counter": counter})


@app.route('/restart')
def restart():
    """
    Invoked by finished break button from the front-end
    if we want to pause the tracker, this is where we should do it
    restart the tracker
    """
    return redirect(url_for('start_tracking'))


def _reset_timer():
    global SCREEN_TIME
    SCREEN_TIME = 0
    print('reset timer to 0')


if __name__ == '__main__':
    app.run()
