import re

def __dictFielding__(Fields):
		##2|Ashbourne#3|N17#4|04978563166
		new_fields=Fields.strip().split('#')[1:]
		dictFields={}
		for field in new_fields:
			dictForm=field.split('|')
			dictFields[dictForm[0]]=dictForm[1]
		return dictFields	

class Contact:

	fieldMapper=["Address","Town","Postcode","Phone"]

	def __init__(self,name, Fields):
		self.name=name
		self.fields={}
		dictFields=__dictFielding__(Fields)
		for key, value in dictFields.iteritems():
			self.fields[key]=value

	def setField(self, key, value):
		self.fields[key]=value		
	
	def seeContact(self):
		to_str="Contact %s --- " % self.name
		for key, value in sorted(self.fields.iteritems()):
			to_str+="|%s| : %s    " % (Contact.fieldMapper[int(key)-1],value)
		to_str+='\n'
		return to_str	
		

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
		contacts=""
		for key, contact in self.Contacts.iteritems():
			contacts+=contact.seeContact()
		return contacts	

class AddressBookFixer:
	def __init__(self):
		pass

	def fixAddressBook(self,inputFilename, outputFilename):
		aBook=AddressBook()
		with open(inputFilename, 'r') as fp:
			for line in fp:
				tmp=re.search('(?P<name>[\w, ]*)(.*)',line).groups()
				aBook.addContact(tmp[0],tmp[1])
		f = open(outputFilename,'w')
		f.write(aBook.seeAll())
		f.close()

test=AddressBookFixer()
test.fixAddressBook("addressbook.txt","test")		