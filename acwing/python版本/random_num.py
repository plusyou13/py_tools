import random
#随机生成0-->100之间的数
def get_randomNumber(num):
    lists=[]
    i=0
    for i in range(num):
        lists.append(random.randint(0,1000))
    return lists