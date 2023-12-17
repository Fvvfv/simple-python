shopping_list=[]
shopping_list.append("键盘")
shopping_list.append("键帽")
shopping_list.append("鼠标")
shopping_list.append("音响")
print(shopping_list)
print(len(shopping_list))

shopping_list.remove("键帽")
print(shopping_list)
print(len(shopping_list))
print(shopping_list[1])

price=[799,1024,999]
max_price=max(price)
min_price=min(price)
sorted_price=sorted(price)
print(max_price)
print(min_price)
print(sorted_price)