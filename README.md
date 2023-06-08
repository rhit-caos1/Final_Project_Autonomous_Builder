# Final Project: Robot Traintrack Builder

## **In Porgress** 

## 1. 3D part Generation
The 3D part generation function is a pure python file which utilize solid2 package to generate a 3d scad model and contvert it to stl file. The details are in the readme in 3dpartgen folder.

## 2. Camera Stream from Turtlebot
The turtlebot will use Apriltags to navigate in the workspace. 

Currently, there are some problem with the video stream from turtlebot. The raw image data comes from ros node cannot be read on computer. Only compressed on can work on the specific node on computer. Expect to process the video directly on turtlebot and send essential Apriltag information to computer to eleminate the video stream problem.

There are two testing ros2 package which can be used to transfer image information from Turtlebot to Computer.

Package `img_transform` is a ros package for computer to read image data from robot. It ustilize `cv_bridge` and `image_transform` package to achieve the function. It subscribe to the compressed It directl build on computer.

Package `turtulebot_control` is the ros package read the camera reading and send the data from turtlebot to computer. It ustilize `cv_bridge` and `image_transform` package to achieve the function. It publish 4 different image type and one is compressed message. To build the package on turtlebot, see part F of https://nu-msr.github.io/navigation_site/homework/homework2.html


