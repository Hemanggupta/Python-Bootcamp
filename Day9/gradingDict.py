student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades= dict()

for val in student_scores:
  if(student_scores[val]>90 and student_scores[val]<=100):
    student_grades[val]="Outstanding"
  elif(student_scores[val]>80 and student_scores[val]<=90):
    student_grades[val]="Exceeds Expectations"
  elif(student_scores[val]>70 and student_scores[val]<=80):
    student_grades[val]="Acceptable"
  else:
    student_grades[val]="Fail"

print(student_grades)