import os
from PIL import Image, ImageSequence

# 获取当前脚本所在目录
import sys
if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

# 目标分辨率
target_size = (320, 240)

def crop_to_aspect(image, target_aspect):
    """按目标宽高比裁剪图片，保留居中部分"""
    width, height = image.size
    current_aspect = width / height

    if current_aspect > target_aspect:
        # 宽度大了，裁剪宽度
        new_width = int(target_aspect * height)
        left = (width - new_width) // 2
        right = left + new_width
        image = image.crop((left, 0, right, height))
    else:
        # 高度大了，裁剪高度
        new_height = int(width / target_aspect)
        top = (height - new_height) // 2
        bottom = top + new_height
        image = image.crop((0, top, width, bottom))
    
    return image

def resize_gif(image_path, target_size):
    """调整GIF图像的尺寸并保存"""
    with Image.open(image_path) as im:
        frames = []
        for frame in ImageSequence.Iterator(im):
            # 裁剪到指定宽高比
            cropped_frame = crop_to_aspect(frame, target_size[0] / target_size[1])
            # 缩放到目标尺寸
            resized_frame = cropped_frame.resize(target_size, Image.Resampling.LANCZOS)
            frames.append(resized_frame)

        # 保存新的GIF，添加后缀
        base_name, ext = os.path.splitext(image_path)
        new_file_path = f"{base_name}_resized{ext}"
        
        frames[0].save(new_file_path, save_all=True, append_images=frames[1:], duration=im.info['duration'], loop=0)
        print(f"GIF已保存为: {new_file_path}")

# 获取目录下所有GIF文件
for file_name in os.listdir(current_dir):
    if file_name.lower().endswith(".gif"):
        gif_path = os.path.join(current_dir, file_name)
        print(f"正在处理: {gif_path}")
        resize_gif(gif_path, target_size)
