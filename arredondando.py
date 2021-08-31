#para exibir mensagem com print

print("calculadora de idade")


#usuarrio digitar um dado

nome =input("digite seu nome")

#dados numericos

ano_nascimento =int(input("digite seu ano de nasciment"))

idade = 2021 - ano_nascimento

#formas corretas de concatenar texto com a variavel
print(f" {nome}, sua idade é {idade}")
print("{}, sua idade é {}".format(nome , idade))