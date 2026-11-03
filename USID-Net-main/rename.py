import os

def rename_images_with_suffix(folder_path, suffix="_1"):
    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # 排序图片文件
    image_files.sort()

    # 遍历图片文件并进行重命名
    for index, old_name in enumerate(image_files, start=1):
        # 获取文件扩展名
        _, extension = os.path.splitext(old_name)

        # 构造新的文件名
        new_name = str(index) + extension

        # 构造完整的文件路径
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        # 重命名文件
        os.rename(old_path, new_path)

        print(f'Renamed: {old_name} -> {new_name}')

if __name__ == "__main__":
    folder_path = "./data/HSTS/hazy"  # 替换为你的文件夹路径
    rename_images_with_suffix(folder_path)
# import os
#
# def rename_images(folder_path):
#     # 获取文件夹中的所有图片文件
#     image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
#
#     # 排序图片文件
#     image_files.sort()
#
#     # 遍历图片文件并进行重命名
#     for index, old_name in enumerate(image_files, start=1):
#         # 获取文件扩展名
#         _, extension = os.path.splitext(old_name)
#
#         # 构造新的文件名，统一添加"_1"作为后缀
#         new_name = f"{index}_1{extension}"
#
#         # 构造完整的文件路径
#         old_path = os.path.join(folder_path, old_name)
#         new_path = os.path.join(folder_path, new_name)
#
#         # 重命名文件
#         os.rename(old_path, new_path)
#
#         print(f'Renamed: {old_name} -> {new_name}')

# if __name__ == "__main__":
#     folder_path = "./train"  # 替换为你的文件夹路径
#     rename_images(folder_path)
#
