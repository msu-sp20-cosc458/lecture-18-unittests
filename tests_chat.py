# tests_chat.py
import chat_bot
import unittest

class RandomFunctionsChatbotTestCase(unittest.TestCase):
    def test_bangbang_means_command(self):
        r = random_functions.get_chatbot_response('!!')
        self.assertEquals(r, 'WooHoo')

    def test_no_bangbang_means_no_command(self):
        # here we need to create an invalid input
        # we need to make sure our assertEquals function validates that our chat_bot function handled the bad input correctly.

if __name__ == '__main__':
  # make sure we call the function that runs the unit tests!
