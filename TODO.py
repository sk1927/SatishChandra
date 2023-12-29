def file_read():
    with open('todo.txt', 'r') as f:
        itlis = f.readlines()
    return itlis
"""This file_read function used to read the contents of the txet file """

def test_file_read():
    with open('todo.txt', 'w') as f:
        f.write('test')
    assert file_read() == ['test']
itlis = []
while True:
    usrin=input("Type add show edit delete or exit:")
    match usrin:
       case 'add':
           it=input("Enter the item you want to add:")+'\n'
           itlis=file_read()
           itlis.append(it)

           with open('todo.txt', 'w') as f:
                 f.writelines(itlis)

           message="added successfully!"
       case 'show':
           itlis=file_read()
           for indexes, names in enumerate(itlis):
               names=names.strip('\n')
               print(f"{indexes+1}-{names}")
           #itlis=[i for i in itlis]
           #print(itlis)
           #print(*itlis,sep='\n')
       case 'edit':
           rep=int(input("which item do you want to edit? say in number"))
           itlis=file_read()
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
           itlis=file_read()
           itlis.pop(rem - 1)
           for indexes, names in enumerate(itlis):
               names=names.strip('\n')
               print(f"{indexes+1}-{names}")
       case 'exit':
            print("good bye")
            break
