< 注意，此项目基于 https://github.com/dusty-nv/jetson-inference >

### 介绍：

通过识别交通标识控制基于Jetson Nano的小车

### 硬件部分：

a)    材料清单：

      Jetson nano      *1

      电机         *4

      电机驱动L298N    *1

      小车底板       *1

      剪刀         *1

      电源         

​    b)组装过程：

​		首先将电机驱动，电机，nano板按下图连接

   <img width='800' height='400' src="https://github.com/cannonyao/jetson-car/blob/main/images/1.JPG"/>

​	然后连接摄像头以及电源，电源使用两个充电宝，一个充电宝给nano供电（nano板使用5v电源需	要拔掉板上连帽），另一个充电宝给电机供电，电机需要12v电源，因此需要一个5v转12v模块，有	条件的可直接使用12v小车电源直接给nano板与电机供电。

   <img width='200' height='300' src="https://github.com/cannonyao/jetson-car/blob/main/images/2.JPG"/>

  <img width='300' height='400' src="https://github.com/cannonyao/jetson-car/blob/main/images/3.png"/>

### 驱动部分：

#### 	**第一步:**

​			完成以下jetson官方教程:

   https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md

   https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-collect-detection.md

#### 	第二步:

​			1.完成以上两步就应该已经得到了自己训练的模型，然后将本项目python\training\detection\ssd目录下的detectnet.py替换jetson inference 原项目的detect.py, 另外将的car.py与command.txt也复制进原项目的ssd目录下

​			2.pip3 install Jetson.GPIO

#### 	第三步:

​			打开command.txt,替换命令中的标签路径以及模型路径，然后打开命令行到ssd目录，小车就可以开始运行了

<img width='600' height='400' src="https://github.com/cannonyao/jetson-car/blob/main/images/4.png"/>

