import cv2
import time

class MiniMap:
    def __init__():
        return

    def draw():
        return

class Warning:
    def __init__(self):
        self.i = 0
        self.text_frames = 40
        self.no_text_frames = 20
        return

    def draw(self, frame):
        self.frame = frame

        self.i+=1

        if self.i >+ self.text_frames:
            self.i = -self.no_text_frames

        if self.i < 0:
            return frame

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Warning Overheating"

        # get boundary of this text
        textsize = cv2.getTextSize(text, font, 1, 2)[0]

        # get coords based on boundary
        textX = (self.frame.shape[1] - textsize[0]) / 2
        textY = 40+textsize[1]
        # textY = (self.frame.shape[0] + textsize[1]) / 2

        # add text centered on image
        cv2.putText(self.frame, text, (int(textX), int(textY)), font, 1, (20, 20, 240), 2)
        
        

        return self.frame