fw = open('sample.txt','w')
fw.write('Just a test yo!\n')
fw.write('Looks like its working.')
fw.close()
#this shouldnt change anything.
#2
#FINALLY!!
# Adding a branched comment
fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()
