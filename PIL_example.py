from PIL import Image, ImageFilter  # imports the library

imageFile = "C:\\Users\\39231\\Pictures\\BitbucketTNW-1200x609.jpg"

original = Image.open(imageFile) # load an image from the hard drive
blurred = original.filter(ImageFilter.BLUR) # blur the image


original.show() # display both images

blurred.show()