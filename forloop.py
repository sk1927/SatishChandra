
for i in 'main':
    i=i.upper()
    print(i)

main=['hello','world','goodbye']
for i in main:
    i=i.upper()
    print(i)

main1=['hello','world','goodbye','now']
main1=[i.capitalize() for i in main1]
print(main1)

print("printing each item in list without loop",*main1)
print("printing each item in list without loop",*main1 ,sep="\n")