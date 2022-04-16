import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculatePrice(self):
    prices_a = [10, 1000000, 1, -50, 20, 3.456, 1, -3.45, 10]
    prices_b = [10, 1, 1000000, 20, -50, 1, 3.456, 10, -3.45]

    for a, b in zip(prices_a, prices_b):
      self.assertEqual(getRatio(a, b) , a / b)
  
  def test_getRatio_calculatePriceIsZero(self):
    a = 0
    b = 50
    self.assertEqual(getRatio(a, b) , 0)
    a = 50
    b = 0
    self.assertEqual(getRatio(a, b) , "Price B is zero")
    a = 0
    b = 0
    self.assertEqual(getRatio(a, b) , "Price B is zero")




if __name__ == '__main__':
    unittest.main()
