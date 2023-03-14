# pip install Pillow

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

fontSize = 18 # Default font size

# Open IMAGE
try:
    img_path = input('Enter Image path (enter for default):- ') or 'img'
    
    if img_path == "img": # default image
        img = Image.open('imgEdit/card.png')
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)

        # Custom font style and font size
        open_font = input("Enter font path (enter for default):- ") or "myfont"
    
        if open_font == "myfont": # default font
            font_size = input("Font size :- (enter for default)") or fontSize

            if font_size == fontSize: # default size
                myFont = ImageFont.truetype('imgEdit/AnnieUseYourTelescope.ttf', fontSize)
            else: # Custom size
                font_size = int(font_size)
                myFont = ImageFont.truetype('imgEdit/AnnieUseYourTelescope.ttf', font_size)

        else: # Custom font
            open_font.replace("\\", "/")
            font_size = input("Font size :- (enter for default)") or fontSize
        
            if font_size == fontSize: # default size
                myFont = ImageFont.truetype(open_font, fontSize)
            else: # Custom size
                font_size = int(font_size)
                myFont = ImageFont.truetype(open_font, font_size)
        
        # Add Text to an image x/y
        x = input("X :- ")
        y = input("Y :- ")
        x = int(x)
        y = int(y)
        # text = input("Enter text :- ")
        text = open('imgEdit\\text.txt').read()

        I1.text((x, y), text, font=myFont, fill =(0, 0, 0)) # change color 0, 0, 0 by default black color set

        # Display edited image
        img.show()
 
        # Save the edited image
        img.save("card2.png")


    else: # Custom Image
        img_path.replace("\\", "/")
        img2 = Image.open(f'{img_path}')
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img2)

        # Custom font style and font size
        open_font = input("Enter font path :- (enter for default)") or "myfont"
    
        if open_font == "myfont": # default font
            font_size = input("Font size (enter for default):- ") or fontSize

            if font_size == fontSize: # Default size
                myFont = ImageFont.truetype('imgEdit/AnnieUseYourTelescope.ttf', fontSize)
            else: # Custom size
                font_size = int(font_size)
                myFont = ImageFont.truetype('imgEdit/AnnieUseYourTelescope.ttf', font_size)

        else: # Custom font
            open_font.replace("\\", "/")
            font_size = input("Font size (enter for default):- ") or fontSize
        
            if font_size == fontSize: # Default size
                myFont = ImageFont.truetype(open_font, fontSize)
            else: # Custom size
                font_size = int(font_size)
                myFont = ImageFont.truetype(open_font, font_size)

        # Add Text to an image x/y
        x = input("X :- ")
        y = input("Y :- ")
        x = int(x)
        y = int(y)
        # text = input('''Enter text :- ''')
        text = open('imgEdit\\text.txt').read()

        I1.text((x, y), text, font=myFont, fill =(0, 0, 0)) # change color 0, 0, 0 by default black color set

        # Display edited image
        img2.show()
 
        # Save the edited image
        img2.save("card2.png")

except Exception as e:
    print(e)

