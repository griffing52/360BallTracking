from Pipeline import *
from Camera import Camera

pipeline = BallDetection()

# camera = Camera("C:/Users/griff/Documents/Programming/Python/OpenCV/filename4.avi")
camera = Camera()
camera.add_pipeline(pipeline)

camera.add_key_callback(ord('v'), lambda this: this.save_video(not(this.is_saving_video)))
camera.add_key_callback(ord('s'), lambda this: this.snapshot())

# camera.add_update_func(lambda this: entry.forceSetDoubleArray())

camera.start()


