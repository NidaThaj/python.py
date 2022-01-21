keys=[]
values=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    keys.append(int(input("Enter the key:")))
    values.append(input("Enter the value:"))
dict={keys[i]:values[i] for i in range(len(keys))}
print("Resultant dictionary is:"+str(dict))
