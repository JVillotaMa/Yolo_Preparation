import os
import shutil


# Set your source directories
source_images_dir = 'path/to/your/images'
source_labels_dir = 'path/to/your/labels'

# Set your new directory structure
new_dataset_dir = 'path/to/your/new_dataset'
new_images_dir = os.path.join(new_dataset_dir, 'images')
new_labels_dir = os.path.join(new_dataset_dir, 'labels')

# Create new directories for train and validation sets
os.makedirs(os.path.join(new_images_dir, 'train'), exist_ok=True)
os.makedirs(os.path.join(new_images_dir, 'val'), exist_ok=True)
os.makedirs(os.path.join(new_labels_dir, 'train'), exist_ok=True)
os.makedirs(os.path.join(new_labels_dir, 'val'), exist_ok=True)

# Get a list of all images and labels
all_images = [f for f in os.listdir(source_images_dir) if os.path.isfile(os.path.join(source_images_dir, f))]
all_labels = [f for f in os.listdir(source_labels_dir) if os.path.isfile(os.path.join(source_labels_dir, f))]

# Check that images and labels match
if len(all_images) != len(all_labels):
    raise ValueError("The number of images and labels do not match.")


# Split the dataset into 80% training and 20% validation
split_ratio = 0.8
split_index = int(len(all_images) * split_ratio)

train_images = all_images[:split_index]
val_images = all_images[split_index:]

# Move files to the new directories
for image in train_images:
    shutil.move(os.path.join(source_images_dir, image), os.path.join(new_images_dir, 'train', image))
    shutil.move(os.path.join(source_labels_dir, image.replace('.jpg', '.txt')), os.path.join(new_labels_dir, 'train', image.replace('.jpg', '.txt')))

for image in val_images:
    shutil.move(os.path.join(source_images_dir, image), os.path.join(new_images_dir, 'val', image))
    shutil.move(os.path.join(source_labels_dir, image.replace('.jpg', '.txt')), os.path.join(new_labels_dir, 'val', image.replace('.jpg', '.txt')))

print("Dataset restructuring completed!")
