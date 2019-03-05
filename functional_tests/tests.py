from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)

	def test_start_list_and_retrieve_later(self):
		#Bob goes to our website
		self.browser.get(self.live_server_url)

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
		self.wait_for_row_in_list_table('1: Buy peacock feathers')
	
		#There is still a text box for a new item
		#Bob enters "Use feather to make a fly"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use feathers to make a fly')
		#When he hits enter, the page updates and lists
		#1: Buy peacock feathers
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy peacock feathers')
		self.wait_for_row_in_list_table('2: Use feathers to make a fly')
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