# Self-Driving-RC-Car
This is a project where I modify an RC car to avoid obstacles and stay between lanes.
Currently, I have modified an RC car so it can be controlled from a laptop. 

RC Car Front | RC Car Back
:----:|:----:
![](https://github.com/bartchr808/Self-Driving-RC-Car/blob/master/Images/RC%20Car%20Front.png) | ![](https://github.com/bartchr808/Self-Driving-RC-Car/blob/master/Images/RC%20Car%20Back.png)

**RC Car Controller**
![](https://github.com/bartchr808/Self-Driving-RC-Car/blob/master/Images/RC%20Controller.png)


## Steering Strategies
I plan on having two different strategies that I will use to teach the car
to drive.

1. Train a Convolutional Neural Network (CNN) using labelled video data
2. Find the center of the pair of lanes, and tell the car to center itself at that point.
This can be done by looking at the distances to each lane from the center of the camera feed.

Both techniques will use various computer vision techniques such as grayscaling, 
[Gaussian Blur](https://en.wikipedia.org/wiki/Gaussian_blur),
[Canny Edge Detection](https://en.wikipedia.org/wiki/Canny_edge_detector), and 
[Hough Transformation](https://en.wikipedia.org/wiki/Hough_transform).

I'm expected the simpler approach, i.e. \#2, being a better solution to driving between
lanes than the CNN approach, i.e. \#1, due to the simplicity of it. However, if I want to
do any stop sign detection, I will recuire a CNN, but I can use transfer learning to
reuse an existing model that has been designed to do this already.

## Next Steps
My next steps are to go through recorded videos and label them that I can then use to feed
into a convolutional neural network so it can learn steering inputs. Below are some GIFs
of the training data recordings (before any preprocessing was done):


![](https://github.com/bartchr808/Self-Driving-RC-Car/blob/master/Images/stop_sign.gif)
![](https://github.com/bartchr808/Self-Driving-RC-Car/blob/master/Images/short_right.gif)
![](https://github.com/bartchr808/Self-Driving-RC-Car/blob/master/Images/long_straight.gif)
![](https://github.com/bartchr808/Self-Driving-RC-Car/blob/master/Images/long_right.gif)
