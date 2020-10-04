아래 문제를 파이썬으로 풀어서 올려주세요
https://www.acmicpc.net/problem/17293
week1 폴더 안에 파이썬 코드 파일을 넣어서 올려주시면 됩니다.

entered_bottle_number = int(input())
n = entered_bottle_number

bot_str = "bottle"
if entered_bottle_number > 1:
    bot_str = "bottles"

while n > 2 :
    statement = """%s bottles of beer on the wall, %s bottles of beer.
Take one down and pass it around, %s bottles of beer on the wall.\n""" % (n,n,n - 1)
    print(statement)
    n = n - 1

if n == 2 :
    statement = """2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.\n"""
    n = n - 1
    print(statement)

if n == 1 : 

    statement = """1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, %s %s of beer on the wall.""" % (entered_bottle_number, bot_str)
    print(statement)