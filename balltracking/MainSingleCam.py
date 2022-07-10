from Pipeline import *
from Camera import Camera
from CameraGroup import CameraGroup
from Graphics import Graphics
from UI import *

pipeline = BallDetection()

# hubcam = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub")
# hubcam = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub")
# hubcam2 = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub2")
frontcam = Camera(0, "front", exposure=-3)
# frontcam = Camera(0, "front", captureapi=cv2.CAP_DSHOW)

graphic = Graphics("front")
graphic.add_element(Warning())

frontcam.add_graphics(graphic)

camGroup = CameraGroup(frontcam)

print("Adding pipelines")
camGroup.add_pipeline(pipeline)

# hubcam.add_pipeline(HubDetection())

camGroup.add_key_callback(ord('v'), lambda this: this.save_video(not(this.is_saving_video)))
camGroup.add_key_callback(ord('s'), lambda this: this.snapshot())
camGroup.add_key_callback(ord('c'), lambda this: this.save_camera_settings())

# camera.add_update_func(lambda this: entry.forceSetDoubleArray())

print("Starting!")
camGroup.start()


