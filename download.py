# -*- encoding: utf-8 -*-

import os, sys, requests, re, time


class Downloader:
    """
    文件下载器
    """

    def __init__(self, config={}):
        """
        初始化配置
        :param config:
        """
        self.config = {
            'block': int(config['block'] if hasattr(config, 'block') else 1024),
        }
        self.total = 0
        self.size = 0
        self.filename = ''

    def touch(self, filename):
        """
        :param filename:
        :return:
        """
        with open(filename, 'w') as fin:
            pass

    def remove_nonchars(self, name):
        """
        删除无效的字符
        :param name:
        :return:
        """
        (name, _) = re.subn(r'[\\\/\:\*\?\"\<\>\|]', '', name)
        return name

    def support_continue(self, url):
        """
        判断是否支持断点续传
        :param url: 下载地址
        :return:
        """
        headers = {
            'Range': 'bytes=0-4'
        }
        try:
            r = requests.head(url, headers=headers)
            crange = r.headers['content-range']
            self.total = int(re.match(r'^bytes 0-4/(\d+)$', crange).group(1))
            return True
        except:
            pass
        try:
            self.total = int(r.headers['content-length'])
        except:
            self.total = 0
        return False

    def download(self, url, filename, headers={}):
        """
        文件下载
        :param url: 下载地址
        :param filename: 文件名
        :param headers: 文件头
        :return:
        """
        finished = False
        block = self.config['block']
        local_filename = filename
        dir_path = os.path.dirname(local_filename)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        tmp_filename = local_filename + '.downtmp'
        size = self.size
        total = self.total
        if self.support_continue(url):  # 支持断点续传
            try:
                with open(tmp_filename, 'rb') as fin:
                    self.size = int(fin.read())
                    size = self.size + 1
            except:
                self.touch(tmp_filename)
            finally:
                headers['Range'] = "bytes=%d-" % (self.size,)
        else:
            self.touch(tmp_filename)
            self.touch(local_filename)

        r = requests.get(url, stream=True, verify=False, headers=headers)
        if total > 0:
            print("[+] Size: %dKB" % (total / 1024))
        else:
            print("[+] Size: None")

        start_t = time.time()
        with open(local_filename, 'ab+') as f:
            f.seek(self.size)
            f.truncate()
            try:
                for chunk in r.iter_content(chunk_size=block):
                    if chunk:
                        f.write(chunk)
                        size += len(chunk)
                        f.flush()
                    sys.stdout.write('\b' * 64 + 'Now: %d, Total: %s' % (size, total))
                    sys.stdout.flush()
                finished = True
                os.remove(tmp_filename)
                spend = int(time.time() - start_t)
                speed = int((size - self.size) / 1024 / spend)
                sys.stdout.write('\nDownload Finished!\nTotal Time: %ss, Download Speed: %sk/s\n' % (spend, speed))
                sys.stdout.flush()
            except:
                # import traceback
                # print traceback.print_exc()
                print("\nDownload pause.\n")
            finally:
                if not finished:
                    with open(tmp_filename, 'wb') as ftmp:
                        ftmp.write(str(size))

if __name__ == '__main__':
    pass
