import unittest

class StringReverser:
	def __init__(self):
		pass	

	def reverse_1(self, sentence):
		return sentence[::-1]

	def reverse_2(self, sentence):
		rev=""
		for i in reversed(list(sentence)):
			rev+=i
		return rev

class StringReverserTests(unittest.TestCase):

    def test_reverse_1(self):
	    self.assertEqual(StringReverser().reverse_1("Hello World"), "dlroW olleH")

    def test_reverse_2(self):
        self.assertEqual(StringReverser().reverse_1("Hello World"), "dlroW olleH")

if __name__ == '__main__':
	unittest.main()