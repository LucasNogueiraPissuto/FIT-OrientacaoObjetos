def excluir_nota(students, studentToRemove):
  newAlunos = students

  newAlunos[studentToRemove].pop(0)

  return newAlunos

# Debug
alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0], 
          'Denise': [9.0, 8.5], 
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = excluir_nota(alunos, 'Denise')        	
print(resultado) 
