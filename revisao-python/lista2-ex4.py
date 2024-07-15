### Lista 2 - Exercício 4  ###

print("=" * 5 + "Calculadora de Desconto" + "=" * 5)
valor_oculos = 200
idade = int(input("Digite a sua idade: "))
desconto = (valor_oculos * idade)/100
if idade >= 80:
  valor = valor_oculos - (80 * valor_oculos) /100
  print('Seu desconto é de 80%! O preço final ficará R${:.2f}'.format(valor))
elif idade <= 10:
    valor = valor_oculos - (10*valor_oculos) /100
    print('Seu desconto é de 10%! O preço final ficará R${:.2f}'.format(valor))
else:
    valor = valor_oculos - desconto
    print('Seu desconto é de {}%! O preço final ficará R${:.2f}'.format(idade, valor))
