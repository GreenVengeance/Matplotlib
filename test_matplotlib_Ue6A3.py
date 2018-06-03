import unittest
import Matplotlib_Ue6A3 as mat

"""Created by Bilal"""
class TestMatplotlibUe6A3(unittest.TestCase):
	def test_create_plotF(self):
		""" F=x """
		plt = mat.create_plot('x+2', min_range=0, max_range=4)
		self.assertEqual(plt[0], 2)  # x=0 --> y=2
		self.assertEqual(plt[1], 3)  # x=1 --> y=3
		self.assertEqual(plt[2], 4)  # x=2 --> y=4

	def test_create_plotF2(self):
		""" F2=x^2 """
		plt = mat.create_plot('x**2', min_range=-2, max_range=2)
		self.assertEqual(plt[0], 4)  # x=-2 --> y=4
		self.assertEqual(plt[1], 1)	 # x=-1 --> y=1
		self.assertEqual(plt[2], 0)  # x=-0 --> y=0
		self.assertEqual(plt[3], 1)  # x=-3 --> y=1

	def test_create_plot(self):
		plt = mat.create_plot('security_gap', min_range=0, max_range=4)
		self.assertEqual(plt, 'ERROR')


if __name__ == '__main__':
	unittest.main()
