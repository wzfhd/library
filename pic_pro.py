from PIL import Image, ImageFilter

# 打开图像文件
image = Image.open('input_image.jpg')

# 应用锐化滤镜
image = image.filter(ImageFilter.SHARPEN)

# 保存处理后的图像文件
image.save('output_image.jpg')
