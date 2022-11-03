print("Bem vindo ao seu Holerite Virtual")

salario_hora_str = input("Quanto você ganha por hora trabalhada?\n")
horas_trabalhadas_str = input("Quantas horas você trabalhou este mes?\n")

salario_hora = int(salario_hora_str)
horas_trabalhadas = int(horas_trabalhadas_str)

salario_bruto = salario_hora * horas_trabalhadas
valor_inss = (salario_bruto * 8) / 100
valor_sindicato = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - valor_inss - valor_sindicato

print("Seguem valores referentes a este mês de trabalho:\n")
print("Salário Bruto {}\nValor Pago ao INSS {}\nValor pago ao Sindicato {}\nSalário Líquido {}".format(salario_bruto, valor_inss, valor_sindicato, salario_liquido))