import os

# Paths
gif_folder = "./gifs_2"  # Folder with GIFs structured by setting/content/style
style_folder = "./style"  # Folder with style reference images (style1, style2, etc.)
output_html = "./style-align-gifs.html"

# Mapping of settings to argument labels
arguments_mapping = [
    "share_group_norm",
    "share_layer_norm",
    "share_attention",
    "adain_queries",
    "adain_keys",
    "adain_values"
]

# Function to convert setting digits to argument labels
def setting_to_args(setting_str):
    args = []
    for i, char in enumerate(setting_str):
        state = "True" if char == "1" else "False"
        args.append(f"{arguments_mapping[i]}={state}")
    return ", ".join(args)

# Initialize HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Style Align GIF Presentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container {
            margin-bottom: 40px;
            width: 100%;
            text-align: center;
        }
        .title {
            font-size: 24px;
            margin-bottom: 10px;
        }
        .row {
            display: flex;
            justify-content: center;
            margin: 10px 0;
        }
        .image-box {
            margin: 0 15px;
        }
        .image-box img {
            width: 200px;
            height: 200px;
        }
        .gif-box img {
            width: 320px;
            height: 240px;
            margin: 0 15px;
        }
    </style>
</head>
<body>
    <h1>Style Align GIF Presentation</h1>
"""

# Loop through the GIFs folder and generate HTML content
for setting in os.listdir(gif_folder):
    setting_path = os.path.join(gif_folder, setting)

    if os.path.isdir(setting_path) and not setting.startswith('.'):
        # Convert setting string (e.g., "011001") to argument labels
        setting_args = setting_to_args(setting)

        # Add a title for the setting (shown only once for the whole setting)
        html_content += f'<div class="container">\n'
        html_content += f'<div class="title">Setting: {setting_args}</div>\n'

        # Add top row with style reference images (shown once for each setting)
        html_content += '<div class="row">\n'
        for style_num in range(1, 5):
            if style_num == 1 or style_num == 4:
                style_img = os.path.join(style_folder, f"style{style_num}.jpg")
            else:
                style_img = os.path.join(style_folder, f"style{style_num}.png")
            html_content += f'<div class="image-box"><img src="{style_img}" alt="Style {style_num}"></div>\n'
        html_content += '</div>\n'  # Close top row for style images

        # Loop through the contents (only GIFs for each content)
        for content in os.listdir(setting_path):
            content_path = os.path.join(setting_path, content)

            if os.path.isdir(content_path):
                # Add bottom row with GIFs for each content
                html_content += '<div class="row">\n'
                for style_num in range(1, 5):
                    gif_file = os.path.join(content_path, f"{content}_style{style_num}.gif")
                    html_content += f'<div class="gif-box"><img src="{gif_file}" alt="GIF Style {style_num}"></div>\n'
                html_content += '</div>\n'  # Close bottom row for GIFs

        # End container for this setting
        html_content += '</div>\n'

# End HTML content
html_content += """
</body>
</html>
"""

# Write the HTML file
with open(output_html, 'w') as f:
    f.write(html_content)

print(f"HTML presentation created successfully at {output_html}")
