fw = open('sample.txt','w')
fw.write('Just a test yo!\n')
fw.write('Looks like its working.')
fw.close()
#this shouldnt change anything.
fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()
