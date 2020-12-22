# image_train_test_splitter
A simple tool for splitting your image database.

## Usage
1. Run the main.py file with ```python main.py```
2. First you will be asked to provide a full path to your dataset. (e.g. 'C:\Users\Vegard\Documents\dataset')
3. Then you will be asked to provide a percent of images you would like to be for testing. This will have to be a value between 0 and 1 (e.g. 0.3)
4. If your information is correct the program will now move all your images into a test and training folder based on your spesifications.

## File structure before application
```bash
--dataset
  --category1
    --image1.jpg
    --image2.jpg
  --category2
    --image3.jpg
    --image4.jpg
```
The structure is important.
You can of course have as many categories as you want and the names are irrelevant as long as they aren't 'train' or 'test'.
It supportes all images of type: .png, .jpeg, .jpg

## Closing
Pull requests are welcome. You are free to use this for everything you want without permission.
