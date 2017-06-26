from unittest import TestCase
from calls import get_data

class TestGet_data(TestCase):
    def test_get_data(self):
        assert get_data() == 200
