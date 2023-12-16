file_path = ['1.report1.csv', '2.report 2.csv','3.report 3.csv','4.report4.csv']

for i in file_path:
    i=i.replace('.','_',1).replace(' ','')
    print(i)

color_codes=((1,2,3),('hi','how','you'),(3,4,5),(6,7,7))
print(color_codes[1])
