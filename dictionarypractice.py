months={}
number=[1,2,3,4,5,6,7,8,9,10,11,12]
names=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
for key in number:
    months[key]=names[key-1]
print(months)