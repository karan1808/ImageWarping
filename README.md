# ImageWarping
Creates a real time warped video output from webcam input.


Threading is used to obtain higher FPS(frames per second).

Accessing webcam/USB camera using the cv2.VideoCapture  function and the .read()  method is a blocking operation. The main thread of our Python script is completely blocked (i.e., “stalled”) until the frame is read from the camera device and returned to our script.

We can improve our FPS simply by creating a new thread that does nothing but poll the camera for new frames while our main thread handles processing the current frame.

We can increase our FPS by as much as 379% due to reduction in latency.

In order to accomplish this FPS increase/latency decrease, we have moved the reading of frames from a webcam or USB device to an entirely different thread, totally separate from our main Python script.

For a detailed explanation please refer:https://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
