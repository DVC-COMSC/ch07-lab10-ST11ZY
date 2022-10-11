# ******************************
# Make your Code
# ******************************
userinputs=input("All numbers:")
numbers1=userinputs.split()
i=0
x=0
numbers2=[]
while i<len(numbers1):
    smallest=10000000000000
    numbers1[i]=int(numbers1[i])
    while x<len(numbers1):
        if(smallest>int(numbers1[x])):
            smallest=numbers1[x]
        x=x+1
    numbers2.append(smallest)
    numbers1.pop(numbers1.index(smallest))
    i=i+1
print(numbers2)
    
