from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size, Image.ANTIALIAS)
    resized_image.save(output_image_path)

# 设置图片路径和新的分辨率
input_image_path = 'lydia2.png'
output_image_path = 'lydia21.png'
new_size = (470, 470)  # 新的分辨率，例如800x600

resize_image(input_image_path, output_image_path, new_size)