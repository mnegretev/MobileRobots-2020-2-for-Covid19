#!/usr/bin/env python
#yolo
import rospy
import tf
import time 
import math
#from geometry_msgs.msg import PoseStamped	#geometry_msgs --> Twist||String

from std_msgs.msg import String

def callback(data):
    print "I heard ", str(data.data)
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/recognized", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()



"""
------------------------------------------------------------------------------------------------------------------
				PUBLICA A DONDE DEBE IR EL ROBOT
------------------------------------------------------------------------------------------------------------------
from geometry_msgs.msg import PoseStamped	#geometry_msgs --> Twist||String
def pos_robot():
	pub=rospy.Publisher('/move_base_simple/goal',PoseStamped, queue_size=20)
	rospy.init_node('where_to', anonymous=True)
	print "nodo creado con exito"
	obj=PoseStamped()
	while not rospy.is_shutdown():
		#angulo = raw_input("ingrese el aungulo: ")
		#angulo2 = float(angulo)
		#distancia = raw_input("ingrese la istancia: ")
		#distancia2 = float(distancia)
		
		obj.header.frame_id = "map"
		obj.header.stamp = rospy.Time.now()
		
		obj.pose.position.x=7.95961523056
		#pub.publish(obj)
		#time.sleep(1.5)
		obj.pose.position.y=0.785449028015
		#pub.publish(obj)
		obj.pose.orientation.w=1
		pub.publish(obj)
		time.sleep(2)
		
		#angulo = raw_input("ingrese el aungulo: ")
		#angulo2 = float(angulo)

		#obj.pose.position.x=0
		#obj.pose.position.y=0
		#obj.pose.orientation.w=0
		#pub.publish(obj)
		#time.sleep(1)
		
		#print 'el angulo es :' +str(angulo)
		#print 'la distancia es :' +str(distancia)



if __name__ =='__main__':
	try:
		pos_robot()
	except rospy.ROSInterruptException:
		pass




---------------------------------------------------------------------------------------------------------------------------------
							PUBLICADOR HOLA MUNDO PENDEJO
---------------------------------------------------------------------------------------------------------------------------------
import rospy
import tf
#from geometry_msgs.msg import PoseStamped #std_msgs-> String
from std_msgs.msg import String #std_msgs-> String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) #el nodo esta publicando al topico chater usando mensaje tipo String
    rospy.init_node('talker', anonymous=True)               #publica con el nombre de nodo talker
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():			    #construccion standar de rospy

	hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)			    #imprime el menaje a la pantalla, a rosout y el logfile del nodo
        pub.publish(hello_str)				    #construcion standar
        rate.sleep()					    #construccion standar

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

---------------------------------------------------------------------------------------------------------------------------------
"""


