import csv
import matplotlib.pyplot as plt
import numpy as np

# line chart
# x-line is years
# y-line is numbers
# rainbow trout is green and brown chart is brown

# Creating arrays
rainbow_2014 = []
rainbow_2015 = []
rainbow_2016 = []
rainbow_2017 = []
rainbow_2018 = []
btrout_2014 = []
btrout_2015 = []
btrout_2015 = []
btrout_2016 = []
btrout_2017 = []
btrout_2018 = []
categories = []


with open('data/traa_data.cvs') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader: 
		if line_count is 0: 
			categories.append(row)
			line_count += 1


			# this is our information about Rainbow trout
		if row[1] == "2014" and row[2] == "Rainbow Trout":
			rainbow_2014.append(row)
		elif row[1] == "2015" and row[2] == "Rainbow Trout":
			rainbow_2015.append(row)
		elif row [1] == "2016" and row [2] == "Rainbow Trout":
			rainbow_2016.append(row)
		elif row[1] == "2017" and row[2] == "Rainbow Trout":
			rainbow_2017.append(row)
		elif row[1] == "2018" and row[2] == "Rainbow Trout":
			rainbow_2018.append(row)
			# this is our information on brown trout
		elif row[1] == "2014" and row[2] == "Brown Trout":
			btrout_2014.append(row)
		elif row[1] == "2015" and row[2] == "Brown Trout":
			btrout_2015.append(row)
		elif row[1] == "2016" and row[2] == "Brown Trout":
			btrout_2016.append(row)
		elif row[1] == "2017" and row[2] == "Brown Trout":
			btrout_2017.append(row)
		elif row[1] == "2018" and row[2] == "Brown Trout":
			btrout_2018.append(row)


# getting value 
rainbowInfo = (len(rainbow_2014), len(rainbow_2015), len(rainbow_2016),len(rainbow_2017), len(rainbow_2018))

brownInfo = (len(btrout_2014), len(btrout_2015), len(btrout_2016), len(btrout_2017), len(btrout_2018))


# line graph visualization
plt.rcdefaults()

x_pos = np.arange(len(rainbowInfo))

# lines
fig, ax = plt.subplots()
plt.plot(rainbowInfo, label='Rainbow Trout', color='red', linewidth=4)
plt.plot(brownInfo, label='Brown Trout', color='brown', linewidth=4)

# labels and ticks
#i should do 2014,2015,2016,2017,2018
plt.ylabel('FISH')
plt.xlabel('YEAR')
plt.suptitle('TRAA Eggs Received and Hatched')
ax.set_xticks(x_pos)
ax.set_xticklabels(('2014','2015','2016','2017','2018'))
plt.legend()


# visual for the line graph
plt.show ()

plt.rcdefaults()

years = ['2014','2015','2016','2017','2018']

plt.scatter(years, rainbowInfo, label='Rainbow', color='red', marker="o")
plt.scatter(years, brownInfo, label='Brown', color='brown', marker="o")

plt.xlabel('Years')
plt.ylabel('Countries')
plt.title('Canada VS USA \n Totals Medals')
plt.legend()

plt.show()

