pi_string = ''
pi_long_string = ''
with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
    lines = file_object.readlines()
    for line in lines:
        pi_string += line.strip()
    print(pi_string)
    print(len(pi_string))
    print(lines)

# file_path = r'D:\xml\pi_digits.txt'
# with open(file_path) as file_object2:
#     contents2 = file_object2.read()
#     print(contents2)

file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in lines:
        pi_long_string += line.strip()
    # print(pi_long_string[:52] + "...")
birthday = input("请输入生日：")
if birthday in pi_long_string:
    print("你的生日在pi小数点后100万位内！")
else:
    print("你的生日不在pi小数点后100万位内!")

fileName = 'programming.txt'
with open(fileName, 'a') as file_object2:
    file_object2.write("I love programming so much.")

