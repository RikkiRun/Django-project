from selenium import webdriver
import unittest
browser = webdriver.Firefox()


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        assert 'To-Do' in browser.title, "Browser title was " + browser.title


if __name__ == '__main__':
    unittest.main(warnings='ignore')