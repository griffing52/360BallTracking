# from Pipeline import *
# from Camera import Camera
# from CameraGroup import CameraGroup
# from Graphics import Graphics

import galimi as gg

pipeline = BallDetection()

# C:\Users\username\AppData\Local\Microsoft\WindowsApps\python3.9.exe

hubcam = gg.Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub")
# hubcam = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub")
# hubcam2 = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "hub2")
frontcam = gg.Camera(0, "front", exposure=-3)
backcam = gg.Camera(1, "back", exposure=-7)
sidecam = gg.Camera(2, "side", exposure=-7)
# sidecam = Camera(3, "side", exposure=-7)
# rightcam = Camera(2, "side", exposure=-7, captureapi=cv2.CAP_DSHOW)
# frontcam = Camera(0, "front", captureapi=cv2.CAP_DSHOW)
# backcam = Camera(1, "back", captureapi=cv2.CAP_DSHOW)
# sidecam = Camera(2, "side", captureapi=cv2.CAP_DSHOW)

camGroup = gg.CameraGroup(frontcam, backcam, sidecam, hubcam)
# camGroup = CameraGroup(frontcam, backcam, sidecam, rightcam)
camGroup.add_graphics(Graphics())

print("Adding pipelines")
camGroup.add_pipeline(pipeline)

hubcam.add_pipeline(HubDetection())

camGroup.add_key_callback(ord('v'), lambda this: this.save_video(not(this.is_saving_video)))
camGroup.add_key_callback(ord('s'), lambda this: this.snapshot())
camGroup.add_key_callback(ord('c'), lambda this: this.save_camera_settings())

# camera.add_update_func(lambda this: entry.forceSetDoubleArray())

print("Starting!")
camGroup.start()


