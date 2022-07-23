def reprovados(alunos):
  failedStudents = []

  for student in alunos:
    amountGrade = 0
    sumGrade = 0
    
    for grade in alunos[student]:
      amountGrade = len(alunos[student])

      sumGrade += grade

      media = sumGrade / amountGrade

    if media < 6:
      failedStudents.append(student)

  return failedStudents


# Debug
alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
          'Denise': [9.0, 8.5],
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = reprovados(alunos)			
print(resultado)
