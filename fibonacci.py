myLimit=int(input("Enter number of elements:"));
a1=1;
a2=1;
x=3;
print("Term number 1 is",a1);
print("Term number 2 is",a2);
while myLimit>0:
    a3=a2+a1;
    print("Term number",x," is:", a3);
    a1=a2;
    a2=a3;
    myLimit-=1;
    x+=1;
