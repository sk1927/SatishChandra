itlis = []
while True:
    usrin=input("Enter add show edit delete or exit to your to do list:")
    match usrin:
       case 'add':
           it=input("Enter the item you want to add:")+'\n'

           with open('todo.txt', 'r') as f:
               itlis=f.readlines()
               f.close()
           itlis.append(it)

           with open('todo.txt', 'w') as f:
                 f.writelines(itlis)
                 f.close()
           message="added successfully!"
       case 'show':
           with open('todo.txt', 'r') as f:
               itlis=f.readlines()
               f.close()
           for indexes, names in enumerate(itlis):
               names=names.strip('\n')
               print(f"{indexes+1}-{names}")
           #itlis=[i for i in itlis]
           #print(itlis)
           #print(*itlis,sep='\n')
       case 'edit':
           rep=int(input("which item do you want to edit? say in number"))
           with open('todo.txt', 'r') as f:
               itlis=f.readlines()
               f.close()
           newwrd=input("enter new item")
           itlis[rep-1]=newwrd
           with open('todo.txt', 'w') as f:
               f.writelines(itlis)
               f.close()
           print("updated successfully!"+'\n'+"Updated list is")
           for indexes, names in enumerate(itlis):
               names = names.strip('\n')
               print(f"{indexes + 1}-{names}")
       case 'delete':
           rem=int(input("which item do you want to delete? say in number"))
           with open('todo.txt', 'r') as f:
               itlis=f.readlines()
               f.close()
           itlis.pop(rem - 1)
           for indexes, names in enumerate(itlis):
               names=names.strip('\n')
               print(f"{indexes+1}-{names}")
       case 'exit':
            print("good bye")
            break
