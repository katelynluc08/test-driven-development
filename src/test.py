# This is just a file I initially used to run the tests. I was going to run them individually but decided to just put all the tests into TestExperiment.py 

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Experiment import Experiment
from src.SignalDetection import SignalDetection

# Create instances of SignalDetection with example data (hits, misses, false alarms, correct rejections)
sd1 = SignalDetection(10, 5, 20, 15)  # Example condition 1
sd2 = SignalDetection(15, 10, 25, 10) # Example condition 2
sd3 = SignalDetection(5, 10, 30, 20)  # Example condition 3

# Create an instance of the Experiment class
exp = Experiment()

# Test with multiple conditions (3 conditions in this case)
exp.add_condition(sd1, "Condition 1")
exp.add_condition(sd2, "Condition 2")
exp.add_condition(sd3, "Condition 3")

# Call sorted_roc_points to get sorted ROC points and print the result
print("With 3 conditions:")
sorted_points = exp.sorted_roc_points()
print(list(sorted_points))

# Test with a single condition
exp_single = Experiment()
exp_single.add_condition(sd1, "Condition 1")
print("\nWith 1 condition:")
sorted_points_single = exp_single.sorted_roc_points()
print(list(sorted_points_single))

# Test with no conditions added (this should raise a ValueError)
exp_empty = Experiment()

try:
    print("\nWith no conditions:")
    exp_empty.sorted_roc_points()  # This should raise a ValueError
except ValueError as e:
    print(f"Error: {e}")  # Expected output: No conditions added to the experiment.
