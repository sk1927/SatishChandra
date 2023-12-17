con=["adadadadadadadadad",'cdsvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvd','gjcjvijoifjvodijdnidsnids','gdfgbdfdbdfbfbfbdfbfbfbfbfbfbfbfbf']

filnames =["a.txt","b.txt","c.txt","d.txt"]

for c,f in zip(con,filnames):
    file=open(f".idea/files/{f}", 'w')
    file.write(c)
