print("Hello World")
print("This message to test git usage in vscode")
cars = 10
print(cars)
print("There are ", cars, " cars")  # python way to print

my_name = 'Sha0w'
my_age = round(24.0323)
print(f"my name is {my_name}", f"my age is {my_age}")

hilarious = False
joke = "isn't that joke so funny ?! {}"
print(joke.format(hilarious))

print("yes i am sha0w", end=';\n')

formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
formatter2 = "{} " * 4
print(formatter2.format(1,2,3,4))

print("""123
123
123
123
4444444
{}""".format("yes"), end = '\r\n')

# age = input()

# print("how old are you ", input())

from sys import argv

v1,v2,v3,v4 = ["1","2","3","4"]
print(v3)

file1 = open("HardWayLearnPython\\lesson01\\res\\textFile.txt",'r+')
print(file1.read())
file1.write("\r\n")
file1.write("test line2")
print(file1.read())
file1.flush
print(file1.read())