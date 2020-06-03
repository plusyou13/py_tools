import os
import comtypes.client


def get_path():
    # 获取当前运行路径
    path = os.getcwd()
    # 获取所有文件名的列表
    filename_list = os.listdir(path)
    # 获取所有word文件名列表
    wordname_list = [filename for filename in filename_list \
                     if filename.endswith((".doc", ".docx"))]
    for wordname in wordname_list:
        # 分离word文件名称和后缀，转化为pdf名称
        pdfname = os.path.splitext(wordname)[0] + '.pdf'
        # 如果当前word文件对应的pdf文件存在，则不转化
        if pdfname in filename_list:
            continue
        # 拼接 路径和文件名
        wordpath = os.path.join(path, wordname)
        pdfpath = os.path.join(path, pdfname)
        #生成器
        yield wordpath,pdfpath


def convert_word_to_pdf():
    word = comtypes.client.CreateObject("Word.Application")
    word.Visible = 0
    for wordpath,pdfpath in get_path():
        newpdf = word.Documents.Open(wordpath)
        newpdf.SaveAs(pdfpath, FileFormat=17)
        newpdf.Close()
    # ppt转化为pdf
    # ppt = comtypes.client.CreateObject("Powerpoint.Application")
    # ppt.Visible = 1
    # newpdf = ppt.Presentations.Open(in_file)
    # newpdf.SaveAs(out_file, FileFormat=32)
    # newpdf.Close()


if __name__ == "__main__":
    convert_word_to_pdf()
