# # # # # # # # # recursion
# # # # # # # # def fun(n):
# # # # # # # #     if n==0:
# # # # # # # #         return
# # # # # # # #     print(n)
# # # # # # # #     fun(n-1)
# # # # # # # # fun(10)
# # # # # # # def fact(n):
# # # # # # #     if n==0 or n==1:
# # # # # # #         return 1
# # # # # # #     return n*fact(n-1)
# # # # # # print(fact(5))
# # # # # # # fact(5)-> 5*fact(4)
# # # # # # # fact(4)-> 4*fact(3)
# # # # # # # fact(3)-> 3*fact(2)
# # # # # # # fact(2)-> 2*fact(1)
# # # # # # # fact(1)->1
# # # # # #
# # # # # #
# # # # # # # indirect recursion
# # # # # # def even(n):
# # # # # #     if n==0:
# # # # # #         return True
# # # # # #     return odd(n-1)
# # # # # # def odd(n):
# # # # # #     if n==0:
# # # # # #         return False
# # # # # #     return even(n-1)
# # # # # # print(even(5))
# # # # #
# # # # # def head(n):
# # # # #     if n==0:
# # # # #         return
# # # # #     head(n-1)
# # # # #     print(n)
# # # # # head(10)
# # # # #
# # # # # def tail(n):
# # # # #     if n==0:
# # # # #         return
# # # # #     print(n)
# # # # #     tail(n-1)
# # # # # tail(10)
# # # # #
# # # # # tree recursion
# # # # def fib(n):
# # # #     if n<=1:
# # # #         return n
# # # #     return fib(n-1)+fib(n-2)
# # # # print(fib(10))
# # # #
# # # # #nested recursion
# def f(n):
#     if n>100:
#         return n-10
#     return f(f(n+11))
#
# print(f(10))
# #
# # def fun():
# #     fun()
# # # fun()
# # import sys
# # sys.setrecursionlimit(2000)
# # print(sys.getrecursionlimit())
