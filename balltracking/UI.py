import cv2

class MiniMap:
    def __init__(self, img_height):
        self.balls = []
        self.margin = 15 # pixels
        self.radius = 60 # pixels
        self.center = (self.radius+self.margin, img_height-self.radius-self.margin)

    def draw(self, frame):

        cv2.circle(frame, self.center, self.radius, (70,70,70), -1)
        cv2.circle(frame, self.center, self.radius, (38,38,38), 3)
        cv2.circle(frame, self.center, int(self.radius*0.08), (38,38,38), -1)
        return frame