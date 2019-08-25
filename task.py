import os

import requests 
from PIL import Image


class Task:
    def __init__(self):
        self.image_url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
        self.data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
        self.image = None

    def initialize_image(self):
        if self.is_image_downloaded():
            self.load_image()
        else:
            self.download_image()

    def download_image(self):
        response = requests.get(self.image_url)
        with open(os.path.join(self.data_dir, "oxygen.png"), 'wb') as image_file:
            image_file.write(self.image)
        
        self.image = Image.open(os.path.join(self.data_dir, "oxygen.png"))
    
    def load_image(self):
        self.image = Image.open(os.path.join(self.data_dir, "oxygen.png"))
    
    def is_image_downloaded(self):
        return os.path.exists(os.path.join(self.data_dir, "oxygen.png"))
    
    def is_grey_pixel(self, pixel : tuple) -> bool:
        r, g, b, _ = pixel
        return r == g == b

    def get_grey_pixels_in_a_row(self, row: int) -> tuple:
        pixels = list()
        current_num = 0
        pixel = self.image.getpixel((current_num, row))
        while self.is_grey_pixel(pixel):
            pixels.append(pixel)
            current_num +=7
            pixel = self.image.getpixel((current_num, row))
        return tuple(pixels)

    def get_pixel_values(self, pixels : tuple) -> tuple:
        return tuple([pixel[0] for pixel in pixels])

    def integers_to_chars(self, list_int: list) -> str:
        return "".join([chr(pixel) for pixel in list_int])

    def convert_pixels_to_chars(self, pixels : tuple) -> str:
        pixel_values = self.get_pixel_values(pixels)
        return self.integers_to_chars(pixel_values)

    def solve(self):
        self.initialize_image()
        pixels = self.get_grey_pixels_in_a_row(47)
        phrase = self.convert_pixels_to_chars(pixels)
        list_start = phrase.find('[')
        list_repr = phrase[list_start:]
        values_list = eval(list_repr)
        return self.integers_to_chars(values_list)
        # return phrase

if __name__ == '__main__':
    task = Task()
    result = task.solve()
    print(result)