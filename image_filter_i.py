# This program reads an image file e.g. adesdesk_logo.jpg,
# it splits the read image into its component RGB bands
# and generates five channels of varying intensities of this image
# this body of code can be refactored to collapse all five "for loops" into one
# I have done this elsewhere, but I maintain a copy of this code still,
# as a remembrance of what I came up with, in an assignment during my earliest days of learning python programming.
# Yours truly, adesdesk


import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw

image=Image.open("adesdesk_logo.jpg")
image=image.convert('RGB')

enhancer=ImageEnhance.Brightness(image)
images=[]
font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 90)
shades = (0.1, 0.3, 0.5, 0.7, 0.9)
labels = []
counter = 0

for x in range(5):
    for i in range(1, 10):
        if i == 1:
            init_shade = image.split()
            new_shade = init_shade[x].point(lambda v:v*(i/10))
            init_shade[x].paste(new_shade)
            new_img = Image.merge(image.mode, init_shade)
            images.append(new_img)
            labels.append("channel {} intensity {}".format(x, (i/10)))
            
        elif i == 3:
            init_shade = image.split()
            new_shade = init_shade[x].point(lambda v:v*(i/10))
            init_shade[x].paste(new_shade)
            new_img = Image.merge(image.mode, init_shade)
            images.append(new_img)
            labels.append("channel {} intensity {}".format(x, (i/10)))

        elif i == 5:
            init_shade = image.split()
            new_shade = init_shade[x].point(lambda v:v*(i/10))
            init_shade[x].paste(new_shade)
            new_img = Image.merge(image.mode, init_shade)
            images.append(new_img)
            labels.append("channel {} intensity {}".format(x, (i/10)))

        elif i == 7:
            init_shade = image.split()
            new_shade = init_shade[x].point(lambda v:v*(i/10))
            init_shade[x].paste(new_shade)
            new_img = Image.merge(image.mode, init_shade)
            images.append(new_img)
            labels.append("channel {} intensity {}".format(x, (i/10)))

        elif i == 9:
            init_shade = image.split()
            new_shade = init_shade[x].point(lambda v:v*(i/10))
            init_shade[x].paste(new_shade)
            new_img = Image.merge(image.mode, init_shade)
            images.append(new_img)
            labels.append("channel {} intensity {}".format(x, (i/10)))      
    
    
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*5,first_image.height*5))
x=0
y=0

for img in images:
    pic = ImageDraw.Draw(img)
    pic.text((0, images[0].height - 60), labels[counter], font = font)
    counter +=1
    contact_sheet.paste(img, (x, y) )
    
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)