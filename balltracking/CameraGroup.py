class CameraGroup:
    # TODO multiple arguments? args...
    def __init__(self, *cameras):
        self.cameras = []
        self.add_camera(cameras)
        return
    
    def add_camera(self, *cameras):
        for camera in cameras:
            self.cameras.append(amera)

    def add_pipeline(self, pipeline):
        for camera in self.cameras:
            camera.add_pipeline(pipeline)

    def save_video(self, boolean):
        for camera in self.cameras:
            camera.save_video(boolean)

    def add_key_callback(self, key, callback):
        for camera in self.cameras:
            camera.add_key_callback(key, callback)

    def get_object_poses(self):
        return [camera.get_object_poses() for camera in self.cameras]

    def start(self):
        for camera in self.cameras:
            camera.start()