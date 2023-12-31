
import os
from PIL import Image, ImageDraw, ImageFont
import key_names


def create_key_icon(key_name):
    # Settings
    font_path = "path/to/font.ttf"
    font_size = 40
    text_color = (255, 255, 255)
    background_color = None
    border_color = (255, 255, 255)
    border_width = 3
    border_radius = 8
    h_padding = 19
    is_uppercase = True
    min_width = 64  # Minimum width as some keys are wider than others
    height = 64
    filename = f"Keyboard_{key_name}"
    ssaa_factor = 3

    scaled_font_size = font_size * ssaa_factor
    scaled_border_width = border_width * ssaa_factor
    scaled_border_radius = border_radius * ssaa_factor
    scaled_h_padding = h_padding * ssaa_factor
    scaled_min_width = min_width * ssaa_factor
    scaled_height = height * ssaa_factor

    # Create font and calculate width for given text
    if is_uppercase:
        key_name = key_name.upper()
    font = ImageFont.truetype(font_path, scaled_font_size)
    _, _, text_width, text_height = font.getbbox(key_name)
    image_width = max(int(text_width) + 2 * scaled_h_padding, scaled_min_width)

    # Draw base_image depending on text width
    base_image = Image.new("RGBA", (image_width, scaled_height))
    draw = ImageDraw.Draw(base_image)

    # Draw text in the middle of the image
    x = (image_width - text_width) // 2
    y = (scaled_height - text_height) // 2
    draw.text((x, y), key_name, fill=text_color, font=font)

    # Draw rounded rectangle around the text
    box_xy = [(0, 0), (image_width - 1, scaled_height - 1)]
    draw.rounded_rectangle(
        box_xy, radius=scaled_border_radius, fill=background_color, outline=border_color, width=scaled_border_width)

    # Downscale image to make it look better
    base_image = base_image.resize(
        (image_width // ssaa_factor, scaled_height // ssaa_factor), resample=Image.LANCZOS)

    # Save image
    if not os.path.exists("icons"):
        os.mkdir("icons")
    base_image.save(f"icons/{filename}.png")


for key in key_names.keys:
    create_key_icon(key)
