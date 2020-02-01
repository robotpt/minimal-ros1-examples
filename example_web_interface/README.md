README
======

A minimal example of using a ROS publisher and subsciber with a web interface.  This example can establish a connection by refreshing the current page at a set time interval until a connection with the ROS web socket is established.  This makes it so that the order when the page is loaded doesn't matter with respect to the web socket being established or even the ROS core being launched. 

Setup
-----

Make sure that you have ROS1 installed on your system (see [here](http://wiki.ros.org/ROS/Installation)).

Install ROS bridge server.

```
sudo apt-get install ros-$ROS_DISTRO-rosbridge-server
```

Install a way of hosting the website.

``` 
sudo apt-get install nodejs npm
sudo npm install http-server -g
sudo ln -s /usr/bin/nodejs /usr/bin/node
```

Then to setup the project with your system paths, enter the following command.  Nothing is being compiled here so you don't need to run a build.

```
rospack profile
```

Running it
----------

Open three terminals.

In terminal one, start the web page:

```
roscd ros_minimal_web_interface/web
http-server
```

Then, open any of the links created with the `http-server` command in a web browser and put that link in the URL. You should see "Not connected to ROS websocket" as text in the web page once it's loaded.


In terminal two, launch the web socket.

```
roslaunch ros_minimal_web_iterface websocket.launch
```

The text should then change to say that the network is setup.  Congratulations, you're connected!


### Recieving messages on the webpage

To see that you can send messages to the page, try the following command:

```
rostopic pub /topic std_msgs/String "data: 'Will it work?'" -1
```

### Sending messages from the webpage

To test that you can recieve messages from the page, try opening up another terminal and typing the following:
```
rostopic echo /response
```

Then in the text box, enter something and click "Submit".  You should see that message in your terminal.
