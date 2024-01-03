def studentslist():
    name=input("Enter the Student Name : ")
    marks=[int(input(f"Enter Marks for Subject {i+1} :")) for i in range (5)] 
    n="shakthi"
    return name ,marks ,n

    # marks = []  # Create an empty list to store marks
    # for i in range(5):  # Loop 5 times for 5 subjects
    #     mark = float(input(f"Enter marks for subject {i + 1}: "))  # Get input for each mark
    #     marks.append(mark)  # Add the mark to the list



students=[studentslist() for _ in range(2)]
print("\nStudentName\tSub1\tSub2\tSub3\tSub4\tSub5")
for student in students:
    print(f"{student[0]}\t\t{student[1][0]}\t{student[1][1]}\t{student[1][2]}\t{student[1][3]}\t{student[1][4]}")