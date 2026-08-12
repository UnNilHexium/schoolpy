import pickle
students={
    1:["a",90],
    2:["b",80],
    3:['c',85]
}
with open("studata.dat","wb") as f:
    pickle.dump(students,f)

roll_no=int(input("Please enter roll number to change- "))
with open('studata.dat',"rb") as f:
    students = pickle.load(f)
if roll_no in students:
    print(students[roll_no][1]," is the student with given roll number")
    new_marks=int(input('please enter new marks-'))
    students[roll_no][2]=new_marks
else:
    print('Roll no. invalid')

with open('studata.dat', 'wb') as f:
    pickle.dump(students,f)