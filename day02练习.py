# age = int(input("请输入一个整数:"))
# if age % 2 != 0:
#     print(f"{age}是奇数")
# else:
#     print(f"{age}不是奇数")


# year = int(input("请输入自己的出生年份："))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

# age = int(input("请输入你的年龄"))
# if age >= 18:
#     print("成年人可以进入网吧")
# else:
#     print("未成年不得入内")

# count = int(input("请输入一个数字："))
# if count % 2 == 0:
#     print(f"{count}是偶数")
# else:
#     print(f"{count}不是偶数")


# age = int(input("请输入你的年龄："))
# if 0 < age <= 11:
#     print("儿童  免票")
# elif 12 <= age <= 17:
#     print("青少年  半价票")
# elif 18 <= age < 60:
#     print("成人  全价票")
# elif 60 <= age <= 120:
#     print("老人  半价票")
# else:
#     print("你想死啊？")


# money = int(input("请输入余额："))
# if money >= 2:
#     print("请上车")
#     seat = int(input("座位数量"))
#     if seat >= 1:
#         print("请坐好")
#     else:
#         print("请站稳扶好")
# else:
#     print("请下去！")


# piao = int(input("请确定是否买到票："))
# if piao >= 1:
#     print("回家")
#     daolength = int(input("刀的长度:"))
#     if daolength <= 3:
#         print("通过安检，可以带上车")
#     else:
#         print("安检没通过，等待警察")
# else:
#     print("没买到票，流浪吧")

# num = int(input("请输入一个三位数:"))
# if num // 100 == num % 10:
#     print(f"{num}是回文数")
# else:
#     print(f"{num}不是回文数")

# while 1:
#     print("666")


# count = 1
# while count <= 50:
#     print(f"{count}")
#     count += 1

# count = 50
# while count >= 1:
#     print(count)
#     count -= 1

# count = 2
# while count <= 100:
#     print(count)
#     count += 2

# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count += 1

# count = 0
# while count < 100:
#     count += 2
#     print(count)

# count = 0
# while count < 100:
#     count += 1
#     if count % 2 == 0:
#         print(count)


# 案例3 1990-2023内得闰月
# num = 1990
# while num <= 2023:
#     if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
#         print(num,end=" ")
#     num += 1
# 案例4 100-999以内的回文数
# num = 100
# while num <= 999:
#     if num // 100 == num % 10:
#         print(num,end=" ")
#     num += 1

# 案例5 while循环统计100以内奇数的数量
# count = 0
# num = 1
# while num <= 100:
#     if num % 2 != 0:
#         print(num,end=" ")
#         count += 1
#     num += 1
# print(f"一共有{count}个奇数")

# 案例6 while循环统计998-2023之间闰年的数量
# count = 0
# num = 998
# while num <= 2023:
#     if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
#         print(num)
#         count += 1
#     num += 1
# print(f"闰年的数量一共是{count}个")

# 案例7求数字1-100的和
# snum = 1
# num = 1
# while num <= 100:
#     print(num)
#     snum += num
#     num +=1

# 案例8 求1-100以内所有偶数的和
# snum = 0
# num = 1
# while num <= 100:
#     if num % 2 == 0:
#         print(num)
#         snum += num
#     num += 1
# print(f"偶数的和为{snum}")
# 案例9 统计100以内有多少个奇数，并对所有的奇数进行求和
# snum = 0
# count = 0
# num = 1
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
#         count += 1
#         snum += num
#     num += 1
# print(f"一共有{count}个")
# print(f"奇数的和为{snum}")

# 作业1
# snum = 0
# count = 0
# num = 1
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
#         count += 1
#         snum += num
#     num += 1
# print(f"奇数的数量为{count}")
# print(f"奇数的和为{snum}")

# 作业2
# count = 0
# num = 998
# while num <= 2023:
#     if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
#         print(num)
#         count += 1
#     num += 1
# print(f"闰年的数量为{count}个")

# 作业三
# count = 0
# num = 100
# while num <= 999:
#     if (num % 10) ** 3 + (num // 10 % 10)** 3 + (num // 100) ** 3 == num:
#         print(num)
#         count += 1
#     num += 1
# print(f"水仙花数的数量为{count}")

# 作业4
# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))
# if num1 == 5 and num2 == 10:
#     while num1 <= num2:
#        print(num1,end=" ")
#        num1 += 1
# elif num1 == 10 and num2 == 5:
#     while num1 >= num2:
#         print(num1,end=" ")
#         num1 -= 1

# 作业五
# count = 0
# num = 1
# while num <= 100:
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)
#         count +=1
#     num += 1
# print(f"一共有{count}个")

# 作业六
# num = 1
# snum = 0
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
#         snum += num
#     else:
#         snum -= num
#     num += 1
# print(f"结果为{snum}")

# 作业7

# count = 3
# while count >= 0:
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     count -= 1
#     if name == "admin" and password == "admin123":
#         print(f"登陆成功，这是第{3-count}次登陆")
#     else:
#         print(f"登陆失败，还有{count}次登陆机会")

# 作业8
# count = 0
# num = 20
# while num <= 200:
#     if num % 7 == 0:
#         print(num)
#         count += 1
#     else:
#         print("该区间没有满足条件的数")
#     num += 1
# print(f"一共{count}个")
