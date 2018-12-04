nota1 = float(input())
nota2 = float(input())

media = (nota1 + nota2) / 2

if media  > 6:
  print ("A Média do Aluno foi: {:.1f}, Aluno Aprovado".format(media))
elif media < 6 and media > 4:
  print ("A Média do Aluno foi: {:.1f}, Aluno de Recuperação".format(media))
else:
  print("A Média do Aluno foi: {:.1f}, Aluno Reprovado".format(media))