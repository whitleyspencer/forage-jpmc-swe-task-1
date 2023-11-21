import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected = 'ABC', 120.48, 121.2, 120.84
    result = getDataPoint(quotes[0])
    self.assertEqual(result, expected)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected = 'ABC', 120.48, 119.2, 119.84
    result = getDataPoint(quotes[0])
    self.assertEqual(result, expected)

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatio(self):
    prices = [125.25, 121.65]
    expected = prices[0]/prices[1]
    result = getRatio(prices[0], prices[1])
    self.assertEqual(result, expected)


  def test_getRatio_priceBzero(self):
    prices = [99.75, 0]
    result = getRatio(prices[0], prices[1])
    self.assertEqual(result, None)


  def test_getRatio_equalPrices(self):
    prices = [99.75, 99.75]
    result = getRatio(prices[0], prices[1])
    self.assertEqual(result, 1)


  def test_getRatio_MissingPrice(self):
    prices = [99.75, None]
    result = getRatio(prices[0], prices[1])
    self.assertEqual(result, None)


  def test_getDataPoint_missingData(self):
    quotes = [
      {'top_ask': {'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    result = getDataPoint(quotes[0])
    expected = None, None, None, None
    self.assertEqual(result, expected)


  def test_getDataPoint_InvalidDataType(self):
    quotes = [
      {'top_ask': {"price": "test", 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    result = getDataPoint(quotes[0])
    expected = None, None, None, None
    self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
