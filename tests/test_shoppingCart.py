from unittest import TestCase
from recipe1 import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self):
        self.cart = ShoppingCart().add("Tuna sandwich", 15.00)

    # def test_add(self):
    #     self.fail()

    def test_item(self):
        self.assertEquals("Tuna sandwich", self.cart.item(1))

    def test_price(self):
        self.assertEquals(15.00, self.cart.price(1))

    def test_total(self):
        self.assertAlmostEqual(16.39, \
                               self.cart.total(9.25), 2)

    def test_length(self):
        self.assertEquals(1, len(self.cart))

