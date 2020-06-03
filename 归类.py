
import os
import shutil
 
path = "./"  # py文件所在的文件夹下
file = os.listdir(path)  # 列出当前文件夹的所有文件
 
# 循环遍历每个文件
for f in file:
    # print(f)
 
    # 以扩展名为名称的子文件夹
    folder_name = path + f.split(".")[-1]
 
    # 如果不存在该目录，先创建，再移动文件
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
 
        # 举例：这里的f为 1.png 等同于 ./1.png (因为是相对路径)
        shutil.move(f, folder_name)
 
    # 直接移动文件
    else:
        shutil.move(f, folder_name)
