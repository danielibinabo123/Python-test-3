students = {"Daniel":90,"Donald":70,"Davian":85,"Diamond":65,"Divine":80}

total=0
for score in students.values():
    total+=score

average=total/len(students)

print("STUDENT GRADE BOOK")
print("------------------")

for name,score in students.items():
    print(name,":",score)

    print("Class Average:",average)

print("Highest Score:",max(students.values()))

print("Lowest Score:",min(students.values()))
search=input("Enter student name")
 

grade = students.get(search)

 if grade is not None:
   print(search,"'s score is:",grade)
   print("student not found")