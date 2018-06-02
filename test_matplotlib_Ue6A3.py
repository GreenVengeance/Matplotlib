import unittest
import Matplotlib_Ue6A3 as mat

"""Created by Bilal"""
class TestMatplotlib_Ue6A3(unittest.TestCase):
	def test_create_plot(self):
		plt = mat.create_plot('x+2', min_range=0, max_range=4)
		self.assertEqual(plt[0], 2)

	def test_create_plot(self):
		plt = mat.create_plot('security_gap', min_range=0, max_range=4)
		self.assertEqual(plt, 'ERROR')


if __name__ == '__main__':
	unittest.main()
