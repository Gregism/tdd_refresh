from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit
		# an empty list item.  She hits Enter on the empty input box
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
		# 
		# The homepage refreshes, and there is an error message saying that list items
		# cannot be blank
		self.wait_for(lambda: self.assertEqual(
			self.browser.find_element_by_css_selector('.has-error').text, "You can't have an empty list"
		))

		# Enter text, it works
		self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
		self.browser.find_element_by_id('id_new_item').send_keys(Key.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')
		# 
		# Enter blank again, fails again
		self.browser.find_element_by_id('id_new_item').send_keys(Key.ENTER)
		self.wait_for(lambda: self.assertEqual(
			self.browser.find_element_by_css_selector('.has-error').text, "You can't have an empty list"
		))