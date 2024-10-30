# a = 3
# b = 2
# c = a + b
# d = a / b
# e = a * b
# f = a - b
#
#
# print(c, d, e, f)
#
#
# name = 'bob'
# age = 14
#
# isAdult = age > 19
#
# print(isAdult)
#
# # 리스트
# shop = ["수박", "사과", "참외"]
#
# print(shop)
#
# # 첫번째 뽑고 싶을 때
# print(shop[0])
# print(shop[1])
# print(shop[2])
# #뒤 부터
# print(shop[-1])
# print(shop[-2])
# print(shop[-3])
#
# # error 발생함.
# # print(shop[-4])
#
# # 함수 생성방법
# def sum(a, b) :
#     return a + b
#
#
# print(sum(1, 2))
# print(sum(3, 4))
#
#
# # 조건문
#
# # if 와 else 로 이루어진 녀석들
#
# def is_adult(age) :
#     if age > 20 :
#         print('성인입니다')
#     else :
#         print('청소년이에요.')
#
# is_adult(30)
#
#
# fruits = ['사과', '배', '딸기', '감']
#
# # 반복문
# for fruit in fruits:
#     print(fruit)
from pprint import pprint

# class Person:
#     def __init__(self, name):  # Person 이라는 객체를 생성할 때 해야하는 일의 모음
#         self.name = name  # 여기서 self는 JAVA 의 this
#
#     def sayhello(self, toWhom):
#         print(f"hello, {toWhom}. I am {self.name}")
#
#
# rtan = Person("르탄")
#
# rtan.sayhello("병관")


# import requests # requests 라이브러리 설치 필요
#
# r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
# rjson = r.json()
#
#
#
# rows = rjson['RealtimeCityAir']['row']
#
# pprint(rows)
#
# for row in rows :
#     print(row['MSRSTE_NM'], row['IDEX_MVL'])

import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
	if gu['IDEX_MVL'] < 60:
		print (gu['MSRSTE_NM'], gu['IDEX_MVL'])
