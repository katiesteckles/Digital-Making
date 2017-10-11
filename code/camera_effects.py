from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview()

# Add an annotation to the top of the image
camera.annotate_text_size = 50
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello World "

# The next line applies effects; try setting none, negative,
# solarize, sketch, denoise, emboss, oilpaint, hatch, gpen,
# pastel, watercolor, film, blur, saturation, colorswap,
# washedout, posterise, colorpoint, colorbalance, cartoon
camera.image_effect = 'sketch'

# Pause for a few seconds to show the image
sleep(5)

# Take a frame
camera.capture('/home/pi/Desktop/image.jpg')

# Here's a neat thing - this tries all the image effects in sequence
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(2)

# Tidy up so we get the screen back when the script is finished.
camera.stop_preview()
