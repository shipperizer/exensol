import re

def __dictFielding__(Fields):
		'#2|Ashbourne#3|N17#4|04978563166'
		new_fields=Fields.strip().split('#')[1:]
		dictFields={}
		for field in new_fields:
			dictForm=field.split('|')
			dictFields[dictForm[0]]=dictForm[1]
		return dictFields	

class Contact:
	def __init__(self,name, Fields):
		self.name=name
		self.fields={}
		dictFields=__dictFielding__(Fields)
		for key, value in dictFields.iteritems():
			self.fields[key]=value

	def setField(self, key, value):
		self.fields[key]=value		
			
		

class AddressBook:
	def __init__(self):
		self.Contacts={}

	def addContact(self, name, Fields):
		if self.Contacts.has_key(name):
				self.__setFields__(name,Fields)
		else:
			self.Contacts[name]=Contact(name,Fields)			

	def __setFields__(self, name,Fields):
		dictFields=__dictFielding__(Fields)
		for key, value in dictFields.iteritems():
			self.Contacts[name].setField(key,value)

	def seeAll(self):
		for key, value in self.Contacts.iteritems():
			print '\nContact %s : Info %s' % (key, str(value.fields))
			

aBook=AddressBook()
with open('addressbook.txt', 'r') as fp:
    for line in fp:
        print line
        tmp=re.search('(?P<name>[\w, ]*)(.*)',line).groups()
        person=Contact(tmp[0],tmp[1])
        print '\nContact %s : Info %s' % (person.name, str(person.fields))
        aBook.addContact(tmp[0],tmp[1])

print "---------------------------------------------------------------------"
aBook.seeAll()