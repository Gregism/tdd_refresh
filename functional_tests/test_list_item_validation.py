from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit
		# an empty list item.  She hits Enter on the empty input box
		# 
		# The homepage refreshes, and there is an error message saying that list items
		# cannot be blank
		# 
		# Enter text, it works
		# 
		# Enter blank again, fails again
		self.fail('Write me!')