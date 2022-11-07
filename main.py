# ******************************
# Make your Code
# ******************************
userinputs=input("All numbers:")
numbers1=userinputs.split()
i=0
x=0
while x<len(numbers1):
    temp=numbers1[x]
    numbers1[x]=int(temp)
    x=x+1
numbers2=numbers1.copy()
while i<len(numbers1):
    minimum=min(numbers2)
    if minimum<numbers1[i]:
        numbers1[numbers1.index(minimum)]=numbers1[i]
        numbers1[i]=minimum
        numbers2.remove(minimum)
    print(numbers1)
    i=i+1
