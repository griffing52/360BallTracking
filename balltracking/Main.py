from Pipeline import *
from Camera import Camera
from CameraGroup import CameraGroup

pipeline = BallDetection()

hubcam = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub")
frontcam = Camera(0, "front")
backcam = Camera(1, "back", captureapi=cv2.CAP_DSHOW)
# backCam = Camera(1, "back")


camGroup = CameraGroup(frontcam, backcam, hubcam)

print("Adding pipelines")
camGroup.add_pipeline(pipeline)

camGroup.add_key_callback(ord('v'), lambda this: this.save_video(not(this.is_saving_video)))
camGroup.add_key_callback(ord('s'), lambda this: this.snapshot())

# camera.add_update_func(lambda this: entry.forceSetDoubleArray())

print("Starting!")
camGroup.start()


