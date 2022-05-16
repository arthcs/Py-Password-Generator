from lib2to3.pygram import Symbols
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-@"

code = (input("Codigo de assinatura: "))
server = (input("Sua senha é para qual serviço: "))

all = lower+upper+numbers+symbols

length = 6
password = "".join(random.sample(all, length))

password = code+password+server
print(password)
