# #
# # def shang(a,b):  #(行参)
# #     if(b == 0):   # 判断 b如果等于0直接执行return
# #         return  None  #返回 None
# #     else: #不满足if,执行以下操作
# #         return (a // b ,a % b)  #将a和b的值 取余和取商
# #
# # res = shang(10, 5)  #(实参),将变量值赋值到res
# #
# # if res is None:  #判断res 是否为None
# #     print("参数错误")
# # else:
# #     print("商为:", res[0], "余为:", res[1])
#
#
#
#
#
#
# # res = shang_yu(20,0):
# #
# # if res is None:
# #     print("参数错误")
# # else:
# #      print("商：",res[0],"余：",res[1])
#
# class calc():
#     res =None
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#
#     def div(self):
#         self.res = self.a / self.b
#
#     def get_result(self):
#          print(self.res)
#
# c = calc(29,39)
# c.sunm()
# c.get_result()

#
#
#
#
# for i in range(1,10):
#     # print("i每次遍历的值为:",i)
#     for j in range(1,i+1):
#         # print("j每次遍历的值为:",j)
#         print(j,"x",i,"=",i*j,end="\t") # \t 空格
#     print(end="\n")  # \n换行
#
#



s =[1,2,5,9,54,6,54,8,71,55,4,889,74,545,4,54,554,1,21,5,5]
length = len(s)
print(length)
for b in range(length-1,0,-1):
    for j in range(b):
        if (s[j] >s[j+1]):
            s[j],s[j + 1]=s[j+1],s[j][动画表情]
print(s)