# 作业1编写一个Python程序，统计100以内奇数的数量，并对所有的奇数进行求和
# count = 0
# snum = 0
# num = 1
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
#         count += 1
#         snum += num
#     num += 1
# print(f"奇数的数量为{count}个")
# print(f"奇数的和为{snum}")

# 作业2编写一个 Python 程序，找到998-2023之间所有的闰年并统计数量
# 闰年的判断规则是：能够被4整除但不能被100整除的年份，或者能够被400整除的年份，都是闰年。
# count = 0
# num = 998
# while num <= 2023:
#     if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
#         print(num)
#         count += 1
#     num += 1
# print(f"闰年的数量为{count}")

# 作业3编写一个 Python 程序，找到100-999之间的水仙花数并统计数量
# 水仙花数的判断规则是：水仙花数是一个三位数，个位数的立方+十位数的立方+百位数的立方 = 这个数本身
# count = 0
# num = 100
# while num <= 999:
#     if (num % 10 )** 3 + (num // 100 )** 3 + (num // 10 % 10) ** 3 == num:
#         print(num)
#         count += 1
#     num +=1
# print(f"水仙花数的数量为{count}个")

# 作业4(while循环)写一个程序，让用户输入num1和num2
# 如果num1为5，num2为10，则输出 5 6 7 8 9 10
# 如果num1为10，num2为5，则输出 10 9 8 7 6 5
# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))
# if num1 == 5 and num2 == 10:
#     while num1 <= num2:
#         print(num1,end=" ")
#         num1 += 1
# elif num1 == 10 and num2 == 5:
#     while num1 >= num2:
#         print(num1,end=" ")
#         num1 -= 1

# 作业5编写一个 Python 程序，找出1-100之间所有既能够被3整除又能被5整除的数,并统计有多少个这样的数
# count = 0
# num = 1
# while num <= 100:
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)
#         count += 1
#     num += 1
# print(f"一共有{count}个")

# 作业6 while循环实现1-2+3-4+5-6……+99-100的结果

# snum = 0
# num =1
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
#         snum += num
#     else:
#         snum -= num
#
#     num += 1
# print(f"while循环实现1-2+3-4+5-6……+99-100的结果为{snum}")

# 作业7设计一个密码登录程序。给用户三次登录机会，如果用户输入用户名为admin
# 密码为admin123则登录成功并告诉用户这第几次输入账号密码登陆成功 ,否则登陆失败，登陆失败并告诉用户还有几次登陆机会
# count = 3
# while count >= 0:
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     count -= 1
#     if name == "admin" and password == "admin123":
#         print(f"登陆成功,这是第{3-count}次登陆成功")
#         break
#     else:
#         print(f"登陆失败,还有{count}次登陆机会")

# 作业8找到20-200之间所有的7的倍数，判断区间是否有满足条件的数
# 如果有则输出满足条件的数，并统计个数
# 如果没有则输出，该区间没有满足条件的数
# count = 0
# num = 20
# while num <= 200:
#     if num % 7 == 0:
#         print(num)
#         count += 1
#     num += 1
# if count == 0:
#     print(f"该区间没有满足条件的数")
# else:
#     print(f"一共有{count}个")
