import os
import shutil
from glob import glob

path = 'test_data/*'

classes = []
classes.extend(glob(path))

def create_test_train_folders(p):
    for f in ['train', 'test']:
        try:
            os.mkdir(os.path.join(p, f))
        except:
            print("Couldn't create folder:", f, "at:", f)

def move_images(p, train_pros=0.5):
    images = []
    images.extend(glob(os.path.join(p, '*.jpg')))

    train_img_amt = int(len(images) * train_pros)

    for i in range(train_img_amt):
        shutil.move(images[i], os.path.join(c, 'train'))

for c in classes:
    create_test_train_folders(c)
    move_images(c)
