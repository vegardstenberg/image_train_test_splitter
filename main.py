import os
import shutil
from glob import glob

path = 'test_data/*'

classes = []
classes.extend(glob(path))

def create_test_train_folders(p): #making test and train folder for given path, meant to be used in subdir's
    for f in ['train', 'test']:
        try:
            os.mkdir(os.path.join(p, f))
        except:
            print("Couldn't create folder:", f, "at:", f)

def move_images(p, test_pros=0.5):
    images = []
    images.extend(glob(os.path.join(p, '*.jpg'))) #accessing all the images

    test_img_amt = int(len(images) * test_pros) #calculating the amount of test images based on test_pros

    for i in range(test_img_amt): #moving images into the test folder
        shutil.move(images[i], os.path.join(c, 'test'))
        images.pop(i) #removing the image from the list, since we do not need it

    for img in images: #moving the rest of the images to train folder
        shutil.move(img, os.path.join(c, 'train'))

for c in classes: #goes through all the folders/classes
    create_test_train_folders(c)
    move_images(c)
