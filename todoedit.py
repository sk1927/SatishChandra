itlis = []
while True:
    usrin=input("Enter add show edit delete or exit to your to do list:")
    match usrin:
       case 'add':
           it=input("Enter the item you want to add:")+'\n'
           file=open('todo.txt','r')
           itlis=file.readlines()
           file.close()
           itlis.append(it)
           file=open('todo.txt','w')
           file.writelines(itlis)
           file.close()

       case 'show':
           file=open('todo.txt','r')
           itlis=file.readlines()
           file.close()
           for indexes, names in enumerate(itlis):
               print(f"{indexes+1}-{names}")
           #itlis=[i for i in itlis]
           #print(itlis)
           #print(*itlis,sep='\n')
       case 'edit':
           rep=int(input("which item do you want to edit? say in number"))
           itlis[rep-1]=input("enter new item")
           print("your to do now:",*itlis,sep='\n')
       case 'delete':
           rem=int(input("which item do you want to delete? say in number"))
           itlis.pop(rem-1)
           for indexes, names in enumerate(itlis):
               print(f"{indexes+1}-{names}")
       case 'exit':
            print("good bye")
            break
