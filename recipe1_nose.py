if __name__ == "__main__":
    # Without nose
    # We had to import the test cases,
    # use a test loader to create a test suite,
    # and then run it through the TextTestRunner.
    import unittest
    from tests.test_shoppingCart import TestShoppingCart

    suite = unittest.TestLoader().loadTestsFromTestCase(TestShoppingCart)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Using nose all those boilerplate code is gone, this is much more succinct
    import nose
    nose.run(argv=["", "tests/test_shoppingCart.py", "--verbosity=2"])
    # nose.main(argv=["", "", "--verbosity=2"])
