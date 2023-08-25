filename="Data.txt"

f=open(filename)
# # print(type(f))
# f.seek(5) #move to 5 characters next
# print(f.tell())#tellstill where have we seeked
# data=f.read(5) #read 5 characters from current position
# print(data)

with open("Data.txt",'a') as f:
    f.write("Hiw")
    f.truncate(5) #restrict size of file



with open("Data.txt",'r') as f:
    print(f.read())

