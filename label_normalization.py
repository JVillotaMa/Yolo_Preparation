import os
from PIL import Image

# Define your classes and map them to indices
class_mapping = {
    'Dog': 0,
    'Cat': 1
}

# Function to normalize bounding box coordinates
def normalize_bbox(bbox, img_width, img_height):
    x_min, y_min, x_max, y_max = bbox
    x_center = (x_min + x_max) / 2.0 / img_width
    y_center = (y_min + y_max) / 2.0 / img_height
    width = (x_max - x_min) / img_width
    height = (y_max - y_min) / img_height
    return x_center, y_center, width, height

# Directory containing your images and labels
dataset_dir = 'dataset/images/train'  # Update this to your dataset path

# Process each label file
for file in os.listdir(dataset_dir):
    if file.endswith('.txt'):
        label_path = os.path.join(dataset_dir, file)
        
        # Get the corresponding image file to extract dimensions
        image_file = file.replace('.txt', '.jpg')  # Adjust if your image extension differs
        image_path = os.path.join(dataset_dir, image_file)

        # Check if the image exists
        if not os.path.isfile(image_path):
            print(f"Warning: Image {image_file} not found for label {file}. Skipping.")
            continue
        
        # Open the label file
        with open(label_path, 'r') as f:
            lines = f.readlines()
        
        # Get image dimensions
        img = Image.open(image_path)
        img_width, img_height = img.size
        
        # Prepare to write the new label file
        new_label_path = os.path.join(dataset_dir, file)  # Overwrite the original label file

        with open(new_label_path, 'w') as out_f:
            for line in lines:
                parts = line.strip().split()
                class_name = parts[0]
                bbox = list(map(float, parts[1:]))
                
                # Convert class name to class index
                class_index = class_mapping.get(class_name)
                if class_index is None:
                    print(f"Warning: Class '{class_name}' not recognized. Skipping.")
                    continue
                
                # Normalize bounding box
                x_center, y_center, width, height = normalize_bbox(bbox, img_width, img_height)
                
                # Write in YOLO format: <class_index> <x_center> <y_center> <width> <height>
                out_f.write(f"{class_index} {x_center} {y_center} {width} {height}\n")

print("Label conversion and normalization complete!")
