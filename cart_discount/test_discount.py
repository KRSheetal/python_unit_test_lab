import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_two_prices_no_discount(self):
        prices = [20, 1] #arrange
        expected_discount = 0 # arrange
        actual_discount = discount(prices) # action
        self.assertEqual(expected_discount, actual_discount) # assert

    def test_list_of_empty_prices(self):
        prices = [ ]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_ten_prices(self):
        prices = [ 3, 10, 9, 1, 3, 2, 4, 5, 8, 7 ]
        expected_discount = 1
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_two_prices(self):
        prices = [10, 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_one_price(self):
        prices = [10]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))
    def test_list_of_one_string(self):
        prices = [ 'a' ]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_three_strings(self):
        prices = [ 'a' , 'b' , 'c' ]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    
    # Fails dues to mixed value types, must sort value types and test for mixed type lists
    # for loop and find string in the program. If string found? return 0
    def test_list_of_four_mixed_strings_number(self):
        prices = [ 'a' , '1' , 'c' , 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_four_random_Strings(self):
        prices = [ '?' , '1' , '\n' , '$']
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))
    def test_list_of_four_duplicate_number(self):
        prices = [ 1 , 1 , 9 , 4]
        expected_discount = 1
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_four_random_Strings(self):
        prices = [ '?' , '1' , '\n' , '$']
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_four_floating_point(self):
        prices = [ 12.44 , 144.2 , 12.9999 , 12]
        expected_discount = 12
        self.assertEqual(expected_discount, discount(prices))
    
    def test_list_of_four_mixed_int_floatingtype(self):
        prices = [ 12.44 , 144.2 , 10 , 12]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))
    
    def test_dictionary_of_one_item(self):
        prices = { 'one':1 }
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))
    
    def test_none_type(self):
        prices = None
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))        


if __name__ == '__main__':
    unittest.main()