from PIL import Image
import os

def crop_and_save(image_path, output_folder):
    # Open the image
    original_image = Image.open(image_path)

    # Get the dimensions of the original image
    width, height = original_image.size

    # Define the size of each cropped part
    crop_width = width // 12
    crop_height = height // 18

    # Create output folders if they don't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each row
    for i in range(12):
        # Loop through each column
        for j in range(18):
            # Calculate the coordinates for cropping
            left = i * crop_width
            upper = j * crop_height
            right = left + crop_width
            lower = upper + crop_height

            # Crop the image
            cropped_image = original_image.crop((left, upper, right, lower))

            # Save the cropped image to the output folder
            output_path = os.path.join(output_folder, f"part_{i}_{j}.png")
            cropped_image.save(output_path)

# Example usage
image_path = "1.jpg"
output_folder = "all"
crop_and_save(image_path, output_folder)
