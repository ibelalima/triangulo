a = float(input("Digite o primeiro valor"))
b = float(input("Digite o segundo valor"))
c = float(input("Digite o terceiro valor"))

if a > b + c or b > c + a or c > a + b:
    print("Não forma um triângulo")
elif a == b!= c or c == a!= b or b == c!= a:
    print("É um triângulo isóceles")
elif a == b == c:
    print("É um triângulo equilátero")
else:
    print("É um triângulo escaleno")