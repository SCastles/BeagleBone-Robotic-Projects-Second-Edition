from flask import Flask
from flask import render_template, request
import time
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('robot.html')

@app.route('/left_side')
def left_side():
    data1="LEFT"
    os.system("/usr/debian/rc_motor/rc_wheeled_auto " + str(90) + " " + str(0))
    return 'true'
@app.route('/right_side')
def right_side():
   data1="RIGHT"
   os.system("/usr/debian/rc_motor/rc_wheeled_auto " + str(-90) + " " + str(0))
   return 'true'
@app.route('/up_side')
def up_side():
   data1="FORWARD"
   os.system("/usr/debian/rc_motor/rc_wheeled_auto " + str(0) + " " + str(1))
   return 'true'

@app.route('/down_side')
def down_side():
   data1="BACK"
   os.system("/usr/debian/rc_motor/rc_wheeled_auto " + str(180) + " " + str(1))
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   os.system("/usr/debian/rc_motor/rc_wheeled_auto " + str(0) + " " + str(0))
   return  'true'

if __name__ == "__main__":
 print "Start"
 app.run(host='0.0.0.0',port=5010)

