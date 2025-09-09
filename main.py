import os
from moviepy import VideoFileClip

# Get the current script directory (root folder)
root_folder = os.path.dirname(os.path.abspath(__file__))

# Define input and output folder paths relative to the script's directory
input_folder = os.path.join(root_folder, 'gifs')
output_folder = os.path.join(root_folder, 'webm_output')

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".gif"):
        gif_path = os.path.join(input_folder, filename)
        webm_filename = os.path.splitext(filename)[0] + ".webm"
        webm_path = os.path.join(output_folder, webm_filename)

        # Load the GIF
        clip = VideoFileClip(gif_path)

        # Write to WebM format
        clip.write_videofile(webm_path, codec="libvpx", audio=False)
        print(f"Converted {filename} to {webm_filename}")

        # Close the clip to release resources
        clip.close()

print("Conversion complete!")