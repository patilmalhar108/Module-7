print("Find out the student average marks using bar graph and line graph")
import matplotlib.pyplot as plt
studentname = ["John", "Mark", "Dave", "Phil", "Steve", "Jeff", "Jack", "Carl"]
studentmarks = [50, 44, 37, 38, 42, 29, 36, 47]
markspercentage = []
for x in studentmarks:
    res = (x / 50) * 100
    markspercentage.append(res)
print(markspercentage)

#linechart
def markslinechart():
    plt.plot(studentname, studentmarks)
    plt.title("Linegraph for student marks")
    plt.xlabel("Student names")
    plt.ylabel("Student marks")
    plt.show()

markslinechart()

#barchart
def percentbarchart():
    plt.bar(studentname, markspercentage)
    plt.title("Bar chart for student percentages")
    plt.xlabel("Student names")
    plt.ylabel("Student percentages")
    plt.show()

percentbarchart()