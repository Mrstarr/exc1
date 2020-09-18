# exc1
Exercise 1 for KTH formula, run on ros melodic, ubuntu18.04

$ mkdir -p ~/kthfsdv/src <br>
$ cd ~/kthfsdv/ <br>
#then install the exc1 fold into the src fold
$ catkin build <br>

#remember to add source in the terminal of fold kthfsdv by
<br>
$ source ./devel/setup.bash

'''
when running the publisher and subscriber
'''
#open a terminal and input:<br>
$ rosrun publisher talker.py

#the open another terminal and input:<br>
$ rosrun receiver listener.py

#to check results<br>
$ rostopic echo result
