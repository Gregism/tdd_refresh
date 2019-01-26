from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_start_list_and_retrieve_later(self):
		#Bob goes to our website
		self.browser.get('http://localhost:8000')

		#Bob notices the page title and header mention To-Do lists
		self.assertIn('To-Do', self.browser.title)


		#Bob is invited to enter a to-do item
		#
		#He types "Buy peacock feathers" as an item in a to-do list
		#
		#When he hits enter, the page updates and lists
		#1: Buy peacock feathers
		#
		#There is still a text box for a new item
		#Bob enters "Use feather to make a fly"
		#
		#The page updates again and shows both items in the list
		#
		#Bob wonders if the site will remember the list, then he sees that the site
		#generated a unique URL for him with explantory text
		#
		#He goes to the URL and the todo is still there
		#
		#Satisfied he closes the browser
		#
		self.fail('Finish the Test')

if __name__ == '__main__':
	unittest.main(warnings='ignore')