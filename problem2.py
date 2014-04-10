import unittest

class PalindromeChecker:
	def __init__(self):
		pass

	def isPalindrome(self, sentence):					
		new_sentence=sentence.replace(" ","").lower()
		a = list(new_sentence)
		b = list(new_sentence)[::-1]
		for i in range(len(new_sentence)):
			if a[i]!=b[i] :
				return False
		return True

class PalindromeCheckerTests(unittest.TestCase):

    def test_isPalindrome_1(self):
	    self.assertEqual(PalindromeChecker().isPalindrome("Hello World"), False)

    def test_isPalindrome_2(self):
	    self.assertEqual(PalindromeChecker().isPalindrome("eye"), True)

    def test_isPalindrome_3(self):
	    self.assertEqual(PalindromeChecker().isPalindrome("Never odd or even"), True)

if __name__ == '__main__':
	unittest.main()