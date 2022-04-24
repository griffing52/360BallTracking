from Pipeline import *
from Camera import Camera
from CameraGroup import CameraGroup

pipeline = BallDetection()

# hubcam = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub")
# hubcam = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub")
# hubcam2 = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub2")
frontcam = Camera(0, "front", exposure=-6)
backcam = Camera(1, "back", exposure=-6)
# frontcam = Camera(0, "front", captureapi=cv2.CAP_DSHOW)
# backcam = Camera(1, "back", captureapi=cv2.CAP_DSHOW)
# sidecam = Camera(2, "side", captureapi=cv2.CAP_DSHOW)

camGroup = CameraGroup(frontcam, backcam)

print("Adding pipelines")
camGroup.add_pipeline(pipeline)

# hubcam.add_pipeline(HubDetection())

camGroup.add_key_callback(ord('v'), lambda this: this.save_video(not(this.is_saving_video)))
camGroup.add_key_callback(ord('s'), lambda this: this.snapshot())

# camera.add_update_func(lambda this: entry.forceSetDoubleArray())

print("Starting!")
camGroup.start()


