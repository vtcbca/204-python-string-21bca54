# was to create two  list student and adderes which contain
#the name of student and there respect adderess print
#stud name with its adderess for example
#student(om sai ram)
#adderess="bardoli surat navsari"
#out put: om--> bardoli
#stname="Om"
#adde="Bardoli"
#print("{}-->{}".format(stname,adde))
l1=[]
l2=[]
def create1List():
    for i in range(3):
        s=input("Enter Name:")
        l1.append(s)
        s2=input("Enter Address:")
        l2.append(s2)
    for i in range(3):
        print(l1[i],"-->",l2[i])
                   
a=create1List()


