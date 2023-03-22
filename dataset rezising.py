import PIL
import os
import os.path
from PIL import Image

f = r' ' # mention the file path inside the single quotes
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((512,512))
    img.save(f_img)