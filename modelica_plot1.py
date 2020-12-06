import matplotlib.pyplot as plt
from csv import reader

with open('motorgenerator_res.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

values1 = []
values2 = []
values3 = []

COLUMN_TO_PLOT_1 = 2
COLUMN_TO_PLOT_2 = 7
COLUMN_TO_PLOT_3 = 10

counter = 0

for row in list_of_rows:
    if counter != 0:  # leave out the first line, because it contains strings
        values1.append(float(row[COLUMN_TO_PLOT_1]))  # if we need to plot more lines, we can add them here
        values2.append(float(row[COLUMN_TO_PLOT_2]))
        values3.append(float(row[COLUMN_TO_PLOT_3]))
    counter = counter + 1

times = range(len(list_of_rows) - 1)

fig, ax = plt.subplots()
ax.plot(times, values1, 'b', label="values1")  # if we need to plot more lines, we can add them here
ax.plot(times, values2, 'g', label="values2")
ax.plot(times, values3, 'r', label="values3")

plt.legend(loc="upper right")

ax.set(xlabel='time [step]', ylabel='value [number]', title='Modelica plot')

ax.grid()

# fig.savefig("test.png")
plt.show()
