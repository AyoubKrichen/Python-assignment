import sys
sys.path.append('..')
import unittest
import pandas as pd
from processing.calculations import DataCalculation

class TestMethod(unittest.TestCase):
    
    def setUp(self):
        print("Setting up the test data...")  
        
        self.df_test = pd.DataFrame({
            'x': [1, 2, 3],
            'y': [4, 5, 6],
            'Delta_Y_test': [0.1, 0.2, 0.3],
            'N_ideal_funct': ['y42', 'y41', 'y11']
        })
        
        self.df_train = pd.DataFrame({
            'x': [1, 2, 3],
            'y1': [4, 5, 6],
            'y2': [4.1, 5.1, 6.1],
            'y3': [3.9, 4.9, 5.9],
            'y4': [5, 6, 7]
        })
        
        self.df_ideal = pd.DataFrame({
            'x': [1, 2, 3],
            'y1': [4, 5, 6],
            'y2': [4.1, 5.1, 6.1],
            'y3': [3.9, 4.9, 5.9],
            'y4': [5, 6, 7]
        })
        
        # Initialize DataCalculation object using the test data

    def test_ideal_function(self):
        print("Running test_ideal_function") 
        self.data_calculation_instance = DataCalculation(self.df_test, self.df_train, self.df_ideal)
        min_test_dev_list, no_ideal_funct_list, max_train_dev_dict, min_test_dev_list_non0 = self.data_calculation_instance.deviations_calculation()

        ideal_funct_list, i_ideal_list, max_train_dev_dict = self.data_calculation_instance.ideal_func_list()

        # Verify if the output lengths match
        self.assertEqual(len(ideal_funct_list), 4, "The ideal function list length should be 4")
        self.assertEqual(len(i_ideal_list), 4, "The ideal function index list length should be 4")
        self.assertEqual(len(max_train_dev_dict), 4, "The max train dev dictionary should contain 4 items")

    def test_deviations_calculation(self):
        print("Running test_deviations_calculation")  
        
        # Call deviations calculation and verify outputs
        min_test_dev_list, no_ideal_funct_list, max_train_dev_dict, min_test_dev_list_non0 = self.data_calculation_instance.deviations_calculation()

        # Check the lengths of the result lists
        self.assertEqual(len(min_test_dev_list), 3, "The min_test_dev_list should have 3 items")
        self.assertEqual(len(no_ideal_funct_list), 3, "The no_ideal_funct_list should have 3 items")
        self.assertEqual(len(min_test_dev_list_non0), 3, "The min_test_dev_list_non0 should have 3 items")


if __name__ == '__main__':
    unittest.main()