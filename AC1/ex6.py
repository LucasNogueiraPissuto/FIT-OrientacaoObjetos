def maior_nota(students):
  bestGradeOfStudents = {}

  for student in students:
    bestGrade = 0

    for grade in students[student]:
      if grade > bestGrade:
        bestGrade = grade

    bestGradeOfStudents[student] = bestGrade

  return bestGradeOfStudents

# Debug
alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0], 
          'Denise': [9.0, 8.5], 
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = maior_nota(alunos)
print(resultado)
