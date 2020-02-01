
function rosInit(ros_master_uri='') {

    if(ros_master_uri == ''){
	    ros_master_uri = 'ws://' + location.hostname + ':9090'
    }

    console.log('ROS master URI: ' + ros_master_uri)
    ros = new ROSLIB.Ros({
	    url : ros_master_uri
    });

    // Once connected, setup the ROS network
    ros.on('connection', function() {
        console.log('Connected to websocket server!');
        setupRosNetwork()
    });

    // If unable to connect or the connection closes, refresh the page
    // to try to reconnect
    ros.on('error', function(error) {
        console.log('Error connecting to websocket server: ', error);
        reload_page_to_retry_connecting();
    });
    ros.on('close', function() {
        console.log('Connection to websocket server closed.');
        reload_page_to_retry_connecting();
    });
}

function reload_page_to_retry_connecting(wait_seconds=2) {
    sleep(wait_seconds).then( function () {
        document.location.reload(true);
    });
}

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds*1000));
}

function setupRosNetwork() {
    listener = new ROSLIB.Topic({
        ros : ros,
        name : 'topic',
        messageType : 'std_msgs/String'
    });
    listener.subscribe(updateText);

    publisher = new ROSLIB.Topic({
        ros : ros,
        name : 'response',
        queue_size: 1,
        messageType: 'std_msgs/String'
    });
    document.getElementById("submit").onclick = submitResponse

    setText("ROS network setup!")
}

function updateText(msg) {
    var my_str = msg.data
    setText(my_str)
}

function setText(str) {
    var text = document.getElementById("text")
    text.innerHTML = str
    console.log("Set value to '" + str + "'");
}

function submitResponse() {
    var value = document.getElementById("input").value;
    console.log("User entered '" + value + "'");

    publisher.publish({data: value});
    document.getElementById("input").value = '';
}
