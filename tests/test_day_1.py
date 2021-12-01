import unittest, os
from day_1.day_1 import DayOne
TESTDATA_DAYONE = os.path.join(os.path.dirname(__file__), 'test_inputs/day_1_test_input.txt')
class TestDayOne(unittest.TestCase):
    def test_day_one_part_one_depth_increase_counter(self):
        self.assertEqual(DayOne().count_depth_increases(depths=[199,200,208,2010,200,207,240,269,260,263]), 7)

    def test_day_one_part_two_window_depth_increase_counter(self):
        self.assertEqual(DayOne().count_increasing_window_depths(depths=[199,200,208,210,200,207,240,269,260,263]), 5)
    
    def test_day_one_input_loading(self):
        self.assertEqual(DayOne().convert_input_file_to_list(TESTDATA_DAYONE), [199,200,208,210,200,207,240,269,260,263])


if __name__ == '__main__':
    unittest.main()