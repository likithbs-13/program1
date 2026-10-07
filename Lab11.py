#Develop Student Grade Tracker:
#Accept multiple students’ names and marks.
#Store them in a list of tuples or dictionaries.
#Display summary reports (average, topper, etc.). 

students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print(students)

# Average marks
average = sum(students.values()) / n
# Topper
topper = max(students, key=students.get)
print("\n--- Student Summary Report ---")
print("Average Marks:", average)
print("Topper:", topper, "with", students[topper], "marks")
