from PIL import Image
import numpy as np


def preprocess():
    img = Image.open("./tshirt.jpg").convert("L")
    img = img.resize((28, 28))
    img_np = np.array(img) / 255.0
    img_np = img_np[:, :, np.newaxis]
    print(img_np.shape)
    return img_np

def get_bounding_box(img):
    thresh = 0.9
    width, height = img.size
    img_np = np.array(img) / 255.0
    print(img_np)
    # determine top
    x = 0
    y = 0
    top = 0
    found = False
    vals = []
    while x < height:
        while y < width:
            if img_np[x][y] not in vals:
                vals.append(img_np[x][y])
            if img_np[x][y] < thresh:
                found = True
                break
            y += 1
        if found:
            print("found")
            top = x
            break
        x += 1
    print(vals)
    x = 0
    y = 0
    left = 0
    found = False
    while y < width:
        while x < height:
            if img_np[x][y] < thresh:
                found = True
                break
            x += 1
        if found:
            left = y
            break
        y += 1
    x = 0
    y = width - 1
    right = 0
    found = False
    while y >= 0:
        while x < height:
            if img_np[x][y] < thresh:
                found = True
                break
            x += 1
        if found:
            right = y
            break
        y -= 1
    x = height - 1
    y = 0
    bottom = 0
    found = False
    while x >= 0:
        while y < width:
            if img_np[x][y] < thresh:
                found = True
                break
            y += 1
        if found:
            bottom = x
            break
        x -= 1
    return left, top, right, bottom



preprocess()