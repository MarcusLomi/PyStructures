'''
Created on Jun 8, 2016

@author: Marcus
'''
fw=open('sample.txt', 'w')
fw.write('Writing some stuff in my text file. \n')
fw.write('I hope I can become a good programmer soon.\n')
fw.close()
fr=open('sample.txt','r')
text=fr.read()
print(text)
