<Note that this project is based on https://github.com/dusty-nv/jetson-inference>
<Detail tutorial: https://github.com/cannonyao/jetson-car/blob/main/detail.doc>
<Demo video:https://www.youtube.com/watch?v=JWrtHfbwdeQ>
### Introduction:

Control the Jetson Nano-based car by recognizing traffic signs

### Hardware parts:

a) Material list:

    Jetson nano *1
    
       Motor *4
    
       Motor drive L298N *1
    
       Trolley floor *1
    
       Scissors *1
    
       power supply         
    
    b) Assembly process:
    
    First, drive the motor, the motor, and the nano board are connected as shown below

   <img width='800' height='400' src="https://github.com/cannonyao/jetson-car/blob/main/images/1.JPG"/>

	Then connect the camera and the power supply. The power supply uses two power banks. One power bank supplies power to the nano (5v power supply needs to be unplugged on the nano board), and the other power bank supplies power to the motor. The motor needs a 12v power supply. A 5v to 12v module can directly use the 12v trolley power supply to directly supply power to the nano board and the motor if possible.

   <img width='200' height='300' src="https://github.com/cannonyao/jetson-car/blob/main/images/2.JPG"/>

  <img width='300' height='400' src="https://github.com/cannonyao/jetson-car/blob/main/images/3.png"/>

### Driving part:

#### 	**first step:**

			Complete the following official jetson tutorials:

   https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md

   https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-collect-detection.md

#### 	The second step:

			1. After completing the above two steps, you should have obtained the model trained by yourself, and then replace the detectnet.py in the python\training\detection\ssd directory of this project with the detect.py of the original jetson inference project, and the car.py and command.txt is also copied into the ssd directory of the original project
	
			2.pip3 install Jetson.GPIO

#### 	third step:

			Open command.txt, replace the label path and model path in the command, and then open the command line to the ssd directory, and the car can start to run

<img width='600' height='400' src="https://github.com/cannonyao/jetson-car/blob/main/images/4.png"/>
