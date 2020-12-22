#
# Developed by: Vegard Hansen Stenberg
# Developed at: 22.12.2020
#

import os
import shutil
from glob import glob

def create_test_train_folders(p): #making test and train folder for given path, meant to be used in subdir's
    for f in ['train', 'test']:
        try:
            os.mkdir(os.path.join(p, f))
        except:
            print("Couldn't create folder:", f, "at:", p)

def move_images(p, test_pros=0.3):
    images = []
    images.extend(glob(os.path.join(p, '*.jpg'))) #accessing all the images

    test_img_amt = int(len(images) * test_pros) #calculating the amount of test images based on test_pros

    for i in range(test_img_amt): #moving images into the test folder
        shutil.move(images[i], os.path.join(c, 'test'))
        images.pop(i) #removing the image from the list, since we do not need it

    for img in images: #moving the rest of the images to train folder
        shutil.move(img, os.path.join(c, 'train'))

if __name__ == '__main__':
    print()
    print(" Thank you for using this image train test splitter, developed by Vegard Hansen Stenberg. ")
    print()

    path = input("Please write your full path (e.g. 'C:\\Users\\Vegard\\Documents\\data') ")
    test_pros = float(input("How many percent of the images should be for testing? (e.g. '0.5') "))

    if path != "" and test_pros >= 0 and test_pros <= 1:
        path += '/*'

        classes = []
        classes.extend(glob(path))

        for c in classes: #goes through all the folders/classes
            create_test_train_folders(c)
            move_images(c, test_pros=float(test_pros))

    else:
        print("You have not provided allowed values, please try again.")
