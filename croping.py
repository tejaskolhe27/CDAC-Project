import os
import shutil
import random
from PIL import Image

def generate_labels(rows, columns):
    labels = []
    for i in range(rows):
        for j in range(columns):
            label = f"label_{i}_{j}"
            labels.append(label)
    return labels

def move_images_to_fixed_folders(image_folder, output_root_folder, rows, columns):
    labels = generate_labels(rows, columns)

    # Create output root folder if it doesn't exist
    os.makedirs(output_root_folder, exist_ok=True)

    # Loop through each image in the image folder
    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)

        # Choose a random label from the fixed set
        random_label = random.choice(labels)

        # Create a folder with the chosen label if it doesn't exist
        output_folder = os.path.join(output_root_folder, random_label)
        os.makedirs(output_folder, exist_ok=True)

        # Move the image to the labeled folder
        output_path = os.path.join(output_folder, image_name)
        shutil.copy(image_path, output_path)

# Example usage
image_folder = "all"
output_root_folder = "output"
rows = 13
columns = 19

move_images_to_fixed_folders(image_folder, output_root_folder, rows, columns)
