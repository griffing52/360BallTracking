import cairo
import numpy as np


class BallCount:
    def __init__(self, img_width, img_height):  
        self.name = name
        self.count = 0
        self.margin = 15
        self.radius = 30
        self.center = (img_width - self.margin - self.radius, img_height - self.margin - self.radius)

    piip
    def draw(self, frame):
        cv2.circle(self.frame, self.center, self.radius, (70,70,70), 3)
        cv2.circle(self.frame, self.center, self.radius, (38,38,38), 3)
        cv2.circle(self.frame, self.center, int(self.radius*0.08), (38,38,38), -1) 

w = 300
h = 300

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, w, h)
ctx = cairo.Context (surface)

# Draw out the triangle using absolute coordinates
ctx.move_to (w/2, h/3)
ctx.line_to (2*w/3, 2*h/3)
ctx.rel_line_to (-1*w/3, 0)
ctx.close_path()
ctx.set_source_rgb (0, 0, 0)  # black
ctx.set_line_width(15)
ctx.stroke()

buf = surface.get_data()
array = np.ndarray (shape=(w,h,4), dtype=np.uint8, buffer=buf)