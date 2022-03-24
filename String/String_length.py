# was to enter 5 string in a list and check and print string hows length
# has even number of character without using any string function.
# note:Do this script using UDF.
l=[]
def createList():
    for i in range(5):
        s=input("Enter string:")
        l.append(s)
        
def length(l):
    co=0
    for i in l:
        for j in i:
            co=co+1
        print(co)
        co-=co
    

createList()
length(l)
