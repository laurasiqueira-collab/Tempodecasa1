nomeFuncionario = input("digite o nome do funcionario\n")
tempocasa = int(input("digite o tempo de casa\n"))
salario = float(input("digite o salario\n"))
meta = float(input("digite a porcentagem da meta\n"))

if tempocasa >= 5 and meta >= 80:
    salariofinal = salario * 1.30
    print(f"{nomeFuncionario} foi promovido")

elif tempocasa >= 5 and meta < 80:
    salariofinal = salario * 1.20

elif tempocasa > 5 and meta >= 80:
    salariofinal = salario * 1.10

else:
    salariofinal = salario

print(f"Salário final: {salariofinal}")