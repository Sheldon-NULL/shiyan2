
str = input()
if(len(str) > 15):
    print(str.lower()[:16])
else:
    print("{:=^15}".format(str))