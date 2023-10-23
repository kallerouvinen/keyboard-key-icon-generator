
from PIL import Image, ImageDraw, ImageFont
import key_names


def create_key_icon(key_name):
    # Settings
    font_path = "path/to/font.ttf"
    font_size = 40
    text_color = (255, 255, 255)
    line_color = (255, 255, 255)
    line_width = 3
    background_color = None
    h_padding = 19
    is_uppercase = True
    min_width = 64  # Minimum width as some keys are wider than others
    height = 64

    # Create font and calculate width for given text
    if is_uppercase:
        key_name = key_name.upper()
    font = ImageFont.truetype(font_path, font_size)
    _, _, text_width, text_height = font.getbbox(key_name)
    image_width = max(int(text_width) + 2 * h_padding, min_width)

    # Draw base_image depending on text width
    base_image = Image.new("RGBA", (image_width, height))
    draw = ImageDraw.Draw(base_image)

    # Draw text in the middle of the image
    x = (image_width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), key_name, fill=text_color, font=font)

    # Draw rounded rectangle around the text
    box_xy = [(0, 0), (image_width - 1, height - 1)]
    draw.rounded_rectangle(
        box_xy, radius=8, fill=background_color, outline=line_color, width=line_width)

    base_image.save(f"icons/{key_name}.png")


for key in key_names.keys:
    create_key_icon(key)
