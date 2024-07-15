### Lista 2 - Exercício 5  ###

print("=" * 5 + "Reajuste Salarial" + "=" * 5)
salario_atual = int(input("Digite o seu salário atual: R$"))
if salario_atual >= 5000:
    porcentagem= (salario_atual * 5) / 100
    salario_novo = salario_atual + porcentagem
    print('''O seu salário era de R${:.2f}.
O aumento será de 5%, no valor de R${:.2f}.
O seu novo salário será R${:.2f}'''.format(salario_atual, porcentagem, salario_novo))
elif salario_atual >= 3000 and salario_atual <= 4999.99:
    porcentagem= (salario_atual * 10) / 100
    salario_novo = salario_atual + porcentagem
    print('''O seu salário era de R${:.2f}.
O aumento será de 10%, no valor de R${:.2f}.
O seu novo salário será R${:.2f}'''.format(salario_atual, porcentagem, salario_novo))
elif salario_atual >= 2000 and salario_atual <= 2999.99:
    porcentagem= (salario_atual * 15) / 100
    salario_novo = salario_atual + porcentagem
    print('''O seu salário era de R${:.2f}.
O aumento será de 15%, no valor de R${:.2f}.
O seu novo salário será R${:.2f}'''.format(salario_atual, porcentagem, salario_novo))
elif salario_atual >= 1500 and salario_atual <= 1999.99:
    porcentagem= (salario_atual * 20) / 100
    salario_novo = salario_atual + porcentagem
    print('''O seu salário era de R${:.2f}.
O aumento será de 20%, no valor de R${:.2f}.
O seu novo salário será R${:.2f}'''.format(salario_atual, porcentagem, salario_novo))
else:
    porcentagem= (salario_atual * 25) / 100
    salario_novo = salario_atual + porcentagem
    print('''O seu salário era de R${:.2f}.
O aumento será de 25%, no valor de R${:.2f}.
O seu novo salário será R${:.2f}'''.format(salario_atual, porcentagem, salario_novo))
