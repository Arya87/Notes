import csv

path = 'C:/Users/Arya/Desktop/TDMPC_DrQ_exp_data/100k_env steps/cheetah-run/2.log'

# 1. newline这里是去除行之间的空行
f = open('C:/Users/Arya/Desktop/TDMPC_DrQ_exp_data/100k_env steps/cheetah-run/2.csv', 'w', encoding='utf-8', newline="")


# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

with open(path, 'r') as f1:
    lines = f1.readlines()
    for i in lines:
        data = i.split(',')
        data1 = data[1][:-1]
        csv_writer.writerow([data[0], data1])