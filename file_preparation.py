import os
image_path = "" #Path where the images are placed
os.chdir(image_path)

path_list = []
#Go through all the images file in the directory

for current_dir, dirs, files in os.walk("."):
    for f in files:
        if f.endswith('.jpg'):
            #Prepare file path to write into path.txt
            file_loc = image_path + "/" + f
            path_list.append(file_loc+"\n")

#Take the first 20% of the paths to test the model
path_list_test = path_list[:int(len(path_list)*0.2)]
path_list = path_list[int(len(path_list)*0.2):]


#Create train.txt and write 80% of data inside (paths)
with open('train.txt','w') as train:
    for i in path_list:
        train.write(i)

#Create test.txt and write 80% of data inside (paths)
with open('test.txt','w') as test:
    for i in path_list_test:
        test.write(i)


#Init the counter
i=0
#Create classes.names file by reading content from existing class.txtfile
with open(image_path+"/"+"classes.names","w") as cls, \
     open(image_path+"/"+"classes.txt","r") as text:
    #Iterate through individual lines in classes txt and write in classes.names
    for l in text:
        cls.write(l)
        i+=1

#Create image data.data like index to all the necessary data
with open(image_path+"/"+"image_data.data","w") as data:
    #Write number of classes
    data.write("classes = " + str(i) + "\n")

    #Write fully qualified data of train.txt file
    data.write("train = " + image_path + "/" + "train.txt" + "\n")

    #Write fully qualified path of the test.txt file
    data.write("test = " + image_path + "/"+ "test.txt"+ "\n")

    #Write fully qualified path of the classes.names file
    data.write("test = " + image_path + "/"+ "classes.names"+ "\n")

    #Specify folder path to save traine model weights
    data.write('backup = backup')