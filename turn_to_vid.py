import moviepy.editor as mp
import os

# Function to convert GIF to MP4
def convert_gif_to_mp4(input_gif, output_mp4):
    clip = mp.VideoFileClip(input_gif)
    clip.write_videofile(output_mp4, codec="libx264", fps=24)

# Folder paths
gif_folder = "./gifs_2"
mp4_folder = "./mp4_videos"

# Create output folder if it doesn't exist
if not os.path.exists(mp4_folder):
    os.makedirs(mp4_folder)

# Convert each GIF in the folder to MP4, maintaining subfolder structure
for setting in os.listdir(gif_folder):
    setting_path = os.path.join(gif_folder, setting)

    if os.path.isdir(setting_path):
        # Create corresponding subfolder in mp4_folder for each setting
        setting_mp4_folder = os.path.join(mp4_folder, setting)
        if not os.path.exists(setting_mp4_folder):
            os.makedirs(setting_mp4_folder)

        for content in os.listdir(setting_path):
            content_path = os.path.join(setting_path, content)

            if os.path.isdir(content_path):
                # Create corresponding subfolder in mp4_folder for each content
                content_mp4_folder = os.path.join(setting_mp4_folder, content)
                if not os.path.exists(content_mp4_folder):
                    os.makedirs(content_mp4_folder)

                for style_num in range(1, 5):
                    input_gif = os.path.join(content_path, f"{content}_style{style_num}.gif")
                    output_mp4 = os.path.join(content_mp4_folder, f"{content}_style{style_num}.mp4")

                    # Convert GIF to MP4
                    convert_gif_to_mp4(input_gif, output_mp4)
                    print(f"Converted {input_gif} to {output_mp4}")
