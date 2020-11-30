#coding = utf-8

# 导入 xlwt excel处理的库
import xlwt

# 测试的txt
dic = 'test.txt'
file = open(dic, encoding='utf-8')

# Excel，默认存储在脚本同一目录下
excel_file = xlwt.Workbook(encoding='utf-8')
table = excel_file.add_sheet('data')

# Excel存入数据
ldata = []

while 1:
    # 读取全部数据
    lines = file.readlines(100000)
    if not lines:
        break   # Txt文本处理结束后退出
    for num in range(len(lines)):
        line = lines[num]   # 读取单独一行
        line = line.split() #以" "为标志分割
        for i in range(len(line)):
            line[i] = line[i].strip()   # 去掉多余的空格
        t = [int(num)]
        word = '' # 把英文词组重新连接
        for i in range(len(line)-1):
            word = word + ' ' + line[i]
        t.append(word)
        t.append(line[-1])

        # 存入数据
        ldata.append(t)

# 写入Excel
for i,p in enumerate(ldata):
#将数据写入文件,i是enumerate()函数返回的序号数
    for j,q in enumerate(p):
        #print(i,j,q)
        table.write(i,j,q)

# 保存至Excel
excel_file.save('data.xls')
