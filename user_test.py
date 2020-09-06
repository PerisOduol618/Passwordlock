import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_credential = User('PerisOduol','peris254')

    def test_init(self):
        self.assertEqual(self.user_credential.user_name,'PerisOduol')
        self.assertEqual(self.user_credential.password, 'peris254')

if __name__ == "__main__":
    unittest.main()
    
