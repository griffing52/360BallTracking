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
