from turtle import Turtle

MOVE_DISTANCE = 20
LEFT = 90
RIGHT = 270
X_COR_START = 350
PADDLE_SIZE = 5
Y_COR_START = 0


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.pu()
        self.color("white")
        self.goto(x=0, y=-260)
        self.shapesize(stretch_len=PADDLE_SIZE, stretch_wid=1)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.setx(new_x)

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.setx(new_x)

# TODO Control with mouse


# Mouse wheel
# self.connect('scroll-event', self.on_scroll)
# def on_scroll(self, widget, event):
#     """ handles on scroll event"""
#
#    # Handles zoom in / zoom out on Ctrl+mouse wheel
#    accel_mask = Gtk.accelerator_get_default_mod_mask()
#    if event.state & accel_mask == Gdk.ModifierType.CONTROL_MASK:
#      direction = event.get_scroll_deltas()[2]
#      if direction > 0:  # scrolling down -> zoom out
#         self.set_zoom_level(self.get_zoom_level() - 0.1)
#      else:
#         self.set_zoom_level(self.get_zoom_level() + 0.1)