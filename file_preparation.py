import os

###Put inside of your project 

##MUST BE STRUCTURE
"""
/porject_name
    filepreparation.py
    /dataset
        /images
            /train

            /val
        labels/
            /train
            
            /val
    /files
"""


# Set your new directory structure
dataset_dir = 'dataset'  
files_dir = "files"
images_dir = os.path.join(dataset_dir, 'images')

# Create train.txt and val.txt paths
train_txt_path = os.path.join(files_dir, 'train.txt')
val_txt_path = os.path.join(files_dir, 'val.txt')

# List training and validation images from the respective directories
train_images_dir = os.path.join(images_dir, 'train')
val_images_dir = os.path.join(images_dir, 'val')

# Get list of image filenames for training and validation sets
train_images = [f for f in os.listdir(train_images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
val_images = [f for f in os.listdir(val_images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Write the train image paths
with open(train_txt_path, 'w') as train_file:
    for image in train_images:
        train_file.write(os.path.join(train_images_dir, image) + '\n')

# Write the val image paths
with open(val_txt_path, 'w') as val_file:
    for image in val_images:
        val_file.write(os.path.join(val_images_dir, image) + '\n')

print("train.txt and val.txt created successfully!")

#Init the counter
i=0
#Create classes.names file by reading content from existing class.txtfile
with open(files_dir+"/classes.names","w+") as cls, \
     open(files_dir+"/classes.txt","r") as text:
    #Iterate through individual lines in classes txt and write in classes.names
    for l in text:
        cls.write(l)
        i+=1

print("Classes.names created succesfully")


#Create image data.data like index to all the necessary data
with open("image_data.data","w") as data:
    #Write number of classes
    data.write("classes = " + str(i) + "\n")

    #Write fully qualified data of train.txt file
    data.write("train = " + train_txt_path + "\n")

    #Write fully qualified path of the test.txt file
    data.write("test = " + val_txt_path + "\n")

    #Write fully qualified path of the classes.names file
    data.write("names = " + files_dir + "/" + "classes.names" + "\n")

    #Specify folder path to save traine model weights
    data.write('backup = backup')

print("image_data.data created succesfully")
