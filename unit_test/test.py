import unittest
import pandas as pd
from processing.calculations import DataCalculation

class TestMethod(unittest.TestCase):
    def __init__(self, df_test, df_train, df_ideal):
        self.df_test = df_test
        self.df_train = df_train
        self.df_ideal = df_ideal

    def setUp(self):
        print("Setting up the test data...")  # Confirm setUp is called
        
        # Sample test data for df_test, df_train, and df_ideal
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
        print("Running test_ideal_function...")  # Confirm this method is running
        
        # Now access self.data_calc, which is correctly initialized
        data_calculation_instance = DataCalculation(self.df_test, self.df_train, self.df_ideal)
        ideal_funct_list,i_ideal_list,max_train_dev_dict = data_calculation_instance.ideal_func_list()

        # Verify if the output lengths match
        print(len(ideal_funct_list), "The ideal function list length should be 4")
        print(len(i_ideal_list),  "The ideal function index list length should be 4")
        print(len(max_train_dev_dict), "The max train dev dictionary should contain 4 items")

        # Example assertion based on expected values (use actual expected values here)
        print(max_train_dev_dict.get('y42', 0), 0.2, places=2, msg="Deviation for y42 is incorrect")
        print('y41', i_ideal_list, "Ideal function y41 should be part of the list")

    def test_deviations_calculation(self):
        print("Running test_deviations_calculation...")  # Confirm this method is running
        
        # Call deviations calculation and verify outputs
        min_test_dev_list, no_ideal_funct_list, max_train_dev_dict, min_test_dev_list_non0 = self.data_calc.deviations_calculation()

        # Check the lengths of the result lists
        print(len(min_test_dev_list), 3, "The min_test_dev_list should have 3 items")
        print(len(no_ideal_funct_list), 3, "The no_ideal_funct_list should have 3 items")
        print(len(min_test_dev_list_non0), 3, "The min_test_dev_list_non0 should have 3 items")


# If running this script directly, execute the tests
if __name__ == '__main__':
    unittest.main()
