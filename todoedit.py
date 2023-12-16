itlis = []
while True:
    usrin=input("Enter add show edit or exit to your to do list:")
    match usrin:
       case 'add':
           it=input("Enter the item you want to add:")

           itlis.append(it)
       case 'show':
           for indexes, names in enumerate(itlis):
               print(f"{indexes}-{names}")
           #itlis=[i for i in itlis]
           #print(itlis)
           #print(*itlis,sep='\n')
       case 'edit':
           rep=int(input("which item do you want to edit? say in number"))
           itlis[rep-1]=input("enter new item")
           print("your to do now:",*itlis,sep='\n')
       case 'exit':
            print("good bye")
            break
