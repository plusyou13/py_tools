# -*- encoding: utf-8 -*-

import os
import zipfile


class ZIP:
    """
    文件压缩
    """

    def unzip_file(self, zip_file: str, dist_dir: str = None, password: str=None):
        """
        解压缩文件
        :param zip_file: 压缩文件路径
        :param dist_dir: 目标文件夹
        :param password: 压缩文件密码
        :return:
        """
        # 判断文件是否存在
        print(zip_file, dist_dir)
        if not os.path.exists(zip_file):
            return

        # 判断目录文件夹是否存在,不存在创建
        if not os.path.exists(dist_dir):
            os.makedirs(dist_dir)

        r = zipfile.is_zipfile(zip_file)
        print(r)
        if not r:
            return

        with zipfile.ZipFile(zip_file, 'r') as zf:
            print(zf.namelist())
            for file in zf.namelist():
                zf.extract(file, dist_dir, password.encode())
        pass

    def zip_file(self, source_path, zip_file, password: str=None):
        """
        对目标进行压缩
        :param source_path: 待压缩目标路径
        :param zip_file: 压缩文件路径
        :param password: 压缩密码
        :return:
        """
        if not os.path.exists(source_path):
            print(source_path + "not found!")
            return

        if os.path.exists(zip_file):
            os.remove(zip_file)

        with zipfile.ZipFile(zip_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:

            # 如果设置密码,给定压缩密码
            if password is not None and len(password) > 0:
                zf.setpassword(password.encode())

            if os.path.isdir(source_path):
                for home, dirs, files in os.walk(source_path):
                    file_dir = home.replace(source_path, "")
                    for file in files:
                        zf.write(os.path.join(home, file), os.path.join(file_dir, file))
            else:
                zf.write(source_path, source_path.replace(os.path.dirname(source_path), ""))
            zf.close()
        pass