
import random
u=0
p=0
a="s"
b="w"
c="g"
i=0
lst=[a,b,c]
pc=random.choice(lst)
print("WELCOME TO SNAKE WATER GUN!\nYou will get 10 chances!")
while(i<10):
    print("\n",i+1,"chance")
    user=input("\n1:Enter 's' for snake\n2:Enter 'w' for water\n3:Enter 'g' for gun\nEnter your choice:")

    if user=="s" and pc=="w":
        u=u+1
    elif pc=="s" and user=="w":
        p=p+1
    elif user=="g" and pc=="w":
        p=p+1
    elif pc=="g" and user=="w":
        u=u+1
    elif user=="g" and pc=="s":
        u=u+1
    elif pc=="g" and user=="s":
        p=p+1
    elif user == "g" and pc == "g":
        u=u+0
        p=p+0
    elif user == "s" and pc == "s":
        u = u + 0
        p = p + 0
    elif user == "w" and pc == "w":
        u = u + 0
        p = p + 0

    i=i+1
    print("You:",user)
    print("Computer:",pc)


if(u>p):
    print("\nYOUR SCORE:",u,"\nCOMPUTER'S SCORE:",p)
    print("\nCongrats!\tYou won!")
elif(u<p):
    print("\nYOUR SCORE:", u, "\nCOMPUTER'S SCORE:", p)
    print("\nSorry you lost")
elif(u==p):
    print("\nYOUR SCORE:", u, "\nCOMPUTER'S SCORE:", p)
    print("\nMatch draw!")