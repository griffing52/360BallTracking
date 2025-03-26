import galimi as gg

from Pipelines import *
from UI import *

# pipeline = BallDetection()
pipeline = HubDetection()

# frontcam = Camera(0, "front", exposure=-3)
frontcam = gg.Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi", "front", exposure=-3)
# frontcam = Camera(0, "front", captureapi=cv2.CAP_DSHOW)


g = gg.Graphics()
g.add_element(MiniMap(480))
# g.add_element(Warning("Warning Overheating"))
# g.add_element(Warning("Warning Low Battery"))
frontcam.add_graphics(g)

camGroup = gg.CameraGroup(frontcam)

print("Adding pipelines")
camGroup.add_pipeline(pipeline)

# hubcam.add_pipeline(HubDetection())

camGroup.add_key_callback(ord('v'), lambda this: this.save_video(not(this.is_saving_video)))
camGroup.add_key_callback(ord('s'), lambda this: this.snapshot())
camGroup.add_key_callback(ord('c'), lambda this: this.save_camera_settings())

# camera.add_update_func(lambda this: entry.forceSetDoubleArray())

print("Starting!")
camGroup.start()


