import re

class Contact:
	def __init__(self,name, Fields):
		self.name=name
		self.fields={}
		dictFields=self.__dictFielding__(Fields)
		for key, value in dictFields.iteritems():
			self.fields[key]=value

	def setField(self, key, value)
		self.fields[key]=value		
			
	def __dictFielding__(self, Fields):
		'#2|Ashbourne#3|N17#4|04978563166'
		new_fields=Fields.strip().split('#')[1:]
		dictFields={}
		for field in new_fields:
			dictForm=field.split('|')
			dictFields[dictForm[0]]=dictForm[1]
		return dictFields		



with open('addressbook.txt', 'r') as fp:
    for line in fp:
        print line
        tmp=re.search('(?P<name>[\w, ]*)(.*)',line).groups()
        person=Contact(tmp[0],tmp[1])
        print '\nContact %s : Info %s' % (person.name, str(person.fields))
