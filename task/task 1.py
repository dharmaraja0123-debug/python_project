marks=[]
while True:
    try:
        mark=int(input("Enter student marks(0-100)or-1 to stop:"))
        if mark==-1:
            break
        elif 0<=mark<= 100:
            marks.append(mark)
        else:
            print("Invalid input! enter a number between 0 and 100,or -1 to stop.")
    except ValueError:
        print("Invalid input! enter an integer.")

if len(marks)>0:
    total_students=len(marks)
    average_marks=sum(marks)/total_students
    highest_marks=max(marks)
    lowest_marks=min(marks)
    passed=sum(1 for m in marks if m >=40)
    failed=total_students-passed

    print("Total number of students:",total_students)
    print("Average marks:",round(average_marks,2))
    print("Highest marks:",highest_marks)
    print("Lowest marks:",lowest_marks)
    print("Number of students passed:",passed)
    print("Number of students failed:",failed)
else:
    print("No student marks entered.")
