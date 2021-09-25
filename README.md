<h1>python_tuya_doorsensor</h1>

<h2>Description of the project</h2>
This programm is a python workarround for a Tuya Door Sensor with the help of pushover! <br>
The Sensor.py constantly pings the door sensor. If it is awake and the ping is successful, it starts the Notify.py! <br>
Notify.py than sends a notification to pushover via pushover api

<h2>Project status</h2>
The project itself is complete and ready for use. I am open for improvments.

<h2>Requirements</h2>
Requirements for running the webui are:
- python (3.x.x) <br>
- pip (v3) or any other packetmanager <br>
- pythonping
- pushover
- pushover account with a valid api token

<h2>Installation</h2>
1. Download and Install Python. <br>
For windows go to (https://www.python.org/downloads/) <br>
For linux use <code> sudo apt-get install python3.x </code> <br>
2. Download and install pip-packetmanager <br>
3. Install pythonping <br>
For Windows <code> py -3 -m pip install pythonping </code> <br>
For Linux <code> pip3 install pythonping </code> <br>
4. Install pushover <br>
For Windows <code> py -3 -m pip install pushover </code> <br>
For Linux <code> pip3 install pushover </code> <br>
5. Make an pushover account and generate your apitoken and copy your account id
6. Insert your values in the Notify.py and also insert the ip of the motion sensor in the Sensor.py
7. Now run the Sensor.py - File
For Windows <code> py -3 Sensor.py </code> <br>
For Linux <code> python3 Sensor.py </code> <br>
8. Install and login in the pushover app. <br>

<h2>Additional notes:</h2>
- The tuya motion sensor needs to be connected to your homenetwork via the app
- afterwards you can block the internet connection of the sensor via your router
- In Sensor.py the ip needs to be inserted! In Notify.py the api-token for the set application needs to be inserted aswell the account id. <br>
- This can be done here https://pushover.net

