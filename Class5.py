# """
# List Comprehension
# """
# """
# _odd = list()
# for i in range(1,10,2):
#     _odd.append(i)
# print(_odd)
# _odd = [i for i in range(1,10,2)]
# print(_odd)
#
# _odd = [i for i in range(0,10,)if i%2==1]
# print(_odd)
# """
# """
# Dictionary comprehension
# """
# """
# sq = {}
# numbers = [2,4,6,7,8,9,11]
# for num in numbers:
#     sq[num]=num * num
# print(sq)
# _sq = {num: num * num for num in numbers}
# print(_sq)
# """
# labels = ['Name','Age','Contact No']
# user_1 = ['Parth',10,9876445664]
# user_2 = ['srikant',12,98989898]
# user_3 = ['kiran',14,78787878]
# info = {}
# for i in range(0, 3):
#     info[i]= labels[i],
#     info[i]= user_1[i]
#
# print(info)
# """
# op = list()
# for user in [user_1,user_2,user_3]:
#     _user = dict()
#
#     for index in range(0,3):
#         _user[labels[index]]=user[index]
#         op.append(_user)
# print(op)
# """

# def greetings():
#     """
#     Greeting functions
#     :return:
#     """
#     print("hello world")
# greetings()
#
# def arg_greetings(name):
#     """
#     this is greetings functions with parameter as name
#     :param name:
#     :return:
#     """
#     print(F"hello {name}")
#     print("Hello",name)
# arg_greetings(name='shri')

def arg_return_greetings(name):
    """
    function which accepts argument and returns value
    :param name:
    :return:
    """
    message = F"Hello {name}"
    return message
# resp = arg_return_greetings("sachin")
# print(resp)
# _name = input("enter name : ")
# resp = arg_return_greetings(_name)
# print(resp)



def dict_function(**kvargs):
    for key,values in kvargs.items():
     print(key, ":", values)
dict_user = {"Name":"virat","Age": "30","contact": "9099090"}
dict_function(**dict_user)