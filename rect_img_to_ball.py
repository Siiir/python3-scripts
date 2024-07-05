from PIL import Image, ImageDraw
from os import path

def create_circular_image(input_image_path, output_image_path):
    image = Image.open(input_image_path)

    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    width, height = image.size
    circle_radius = min(width, height) // 2
    circle_center = (width // 2, height // 2)
    draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius, circle_center[0] + circle_radius, circle_center[1] + circle_radius), fill=255)

    circular_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
    circular_image.paste(image, (0, 0), mask)

    circular_image.save(output_image_path)

DIR_PATH= r"C:\Users\HP\Desktop\DanczakEngine\assets\images"
if __name__ == "__main__":
    input_image_path = path.join(DIR_PATH, "SquareSławcio.png")
    output_image_path = path.join(DIR_PATH, "CircularSławcio.png")
    
    create_circular_image(input_image_path, output_image_path)
