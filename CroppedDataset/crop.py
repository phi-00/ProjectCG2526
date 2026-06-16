from PIL import Image
import os

input_folder = "Images"
output_folder = "DatasetReal"

# Final Size
crop_size = (3000, 3000)

# Create Output Folder
os.makedirs(output_folder, exist_ok=True)

valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        img = Image.open(input_path)

        width, height = img.size

        # Coordinates for crop 
        left = (width - crop_size[0]) // 2
        top = (height - crop_size[1]) // 2
        right = left + crop_size[0]
        bottom = top + crop_size[1]

        if width < 3000 or height < 3000:
            print(f"Ignored : {filename}")
            continue

        cropped_img = img.crop((left, top, right, bottom))

        cropped_img.save(output_path)

        print(f"Image cropped: {filename}")

print("Done")