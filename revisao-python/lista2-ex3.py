### Lista 2 - Exercício 3  ###

print("=" * 5 + "Calculadora de Média" + "=" * 5)
nota_1 = float(input("Digite a sua primeira nota: "))
nota_2 = float(input("Digite a sua segunda nota: "))
media = (nota_1 + nota_2)/ 2
if media >= 7:
  print("Fostes aprovado meu truta!! Média: " + str(media))
elif media < 5:
  print("Foi reprovado fi kkkkkk! Média: " + str(media))
else:
  print("Vai ficar de recuperação! Média: " + str(media))