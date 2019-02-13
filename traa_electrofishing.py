import csv
import matplotlib.pyplot as plt
import numpy as np

# Creating arrays

with open('data/traa_data.cvs') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0