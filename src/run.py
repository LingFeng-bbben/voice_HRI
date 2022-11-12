#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String

lastTime = -1.

def callback(data):
    global lastTime
    rospy.loginfo(data.data)
    #10 seconds for timeout
    if time.time()-lastTime < 10:
        if data.data.find("to the kitchen") >0:
            pub.publish("OK. to the kitchen.")
        elif data.data.find("to the bath") >0:
            pub.publish("OK. to the bathroom.")
        elif data.data.find("to the living") >0:
            pub.publish("OK. to the living room.")
        else:
            pub.publish("I dont know what you are saying")
        lastTime = -1
    if data.data == "hi wheelchair":
        pub.publish("hi, say your command.")
        lastTime = time.time()


if __name__ == '__main__':
    try:
        rospy.init_node('voice_hri', anonymous=True)
        rospy.Subscriber('/speech_recognition/final_result',String, callback)
        pub = rospy.Publisher('/tts/phrase', String, queue_size=10)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass