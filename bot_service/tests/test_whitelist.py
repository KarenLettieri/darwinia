import unittest
from unittest.mock import MagicMock
from domain.repositories.user_repository import UserRepository
from core.exceptions import UserNotWhitelistedError
from domain.use_cases.check_whitelist import CheckWhitelist


class TestCheckWhitelist(unittest.TestCase):

    def setUp(self):
        # Create mock user repository
        self.mock_user_repository = MagicMock(spec=UserRepository)
        self.check_whitelist = CheckWhitelist(self.mock_user_repository)

    def test_user_in_whitelist(self):
        # Simulate that the user exists in the database
        self.mock_user_repository.get_user_by_telegram_id.return_value = {'telegram_id': '123456789'}

        telegram_id = '123456789'
        result = self.check_whitelist.execute(telegram_id)

        self.assertIsNotNone(result)
        self.mock_user_repository.get_user_by_telegram_id.assert_called_once_with(telegram_id)

    def test_user_not_in_whitelist(self):
        # Simulate that the user does not exist in the database
        self.mock_user_repository.get_user_by_telegram_id.return_value = None

        telegram_id = '987654321'

        # Check correct exception is raised
        with self.assertRaises(UserNotWhitelistedError):
            self.check_whitelist.execute(telegram_id)

        self.mock_user_repository.get_user_by_telegram_id.assert_called_once_with(telegram_id)

if __name__ == '__main__':
    unittest.main()