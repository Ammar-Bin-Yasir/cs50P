import sys
from PIL import Image, ImageOps

# Check if the user provided the correct input eg: #.py #.png/jpg #.png/jpg
if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif not (sys.argv[1].endswith(".png") or sys.argv[1].endswith(".jpg")) or not (sys.argv[2].endswith(".png") or sys.argv[2].endswith(".jpg")):
    print("Invalid output")
    sys.exit(1)
else:
    try:
        # Open and resize the input image
        with Image.open(sys.argv[1]) as img:
            img = ImageOps.fit(img, (600, 600))

            # Open the shirt image
            with Image.open("shirt.png") as shirt:
                # Paste the shirt image onto the resized input image
                img.paste(shirt, (0, 0), shirt)

                # Save the final image
                img.save(sys.argv[2])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)
