# exc1
Exercise 1 for KTH formula, run on ros melodic, ubuntu18.04

$ mkdir -p ~/kthfsdv/src
$ cd ~/kthfsdv/
#then install the exc1 fold into the src fold
$ catkin build

#remember to add source in the terminal of fold kthfsdv by
<br>
$ source ./devel/setup.bash

'''
when running the publisher and subscriber
'''
#open a terminal and input:
$ rosrun publisher talker.py

#the open another terminal and input:
$ rosrun receiver listener.py

#to check results
$ rostopic echo result
