import os
from PIL import Image

# Rename images files by keeping only the number
def rename_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".png"):
            # keep only the number and the extension
            new_name = filename.split("-")[-1]
            # rename the file
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

# rename_files("generated")


# Create a gif from a folder of images
def create_gif(folder, gif_name):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".png"):
            images.append(filename)
    final_output = [str(i)+".png" for i in sorted([int(num.split('.')[0]) for num in images])]
    print(final_output)
    frames = [Image.open(f"{folder}/{image}") for image in final_output[:340]]
    frames[0].save(gif_name, format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=200,
                   loop=0)


create_gif("generated", "BirdGAN.gif")
