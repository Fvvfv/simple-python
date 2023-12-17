#用户输入随机数量的整数，求平均值
user_input=input("请输入数字（完成所有数字输入后请输入q终止程序）：")
total=0
count=0
while user_input!="q":
    num=float(user_input)
    total+=num
    count+=1
    user_input=input("请输入数字（完成所有数字输入后请输入q终止程序）：")
if count==0:
    result=0
else:
    result=total/count
print("您输入的数字的平均值为："+str(result))