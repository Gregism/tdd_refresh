from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)


		#Bob is invited to enter a to-do item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			"Enter a to-do item"
		)
		#
		#He types "Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys('Buy peacock feathers')
		#When he hits enter, the page updates and lists
		#1: Buy peacock feathers
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows), 
			"New to-do item did not appear in table"
		)
	
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