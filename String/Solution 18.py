# was to enter 5 string in a list and check and print string hows length
# has even number of character without using any string function.
# note:Do this script using UDF.
l=[]
def createList():
    for i in range(5):
        s=input("Enter string:")
        l.append(s)
        
def length(l):
    s=[]
    co=0
    for i in l:
        for j in i:
            co=co+1
        if co%2==0:
            s.append(i)
        co=0
    return s

createList()
ans=length(l)
print(ans)
