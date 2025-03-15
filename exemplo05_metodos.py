# método com retorno do tipo int
def somar() -> int:
    numero1 = 10
    numero2 = 20
    soma = numero1 + numero2
    return soma 

# método sem retorno
def calculadora():
    # chama o método somar e armazena a soma dos dois números
    resultado = somar()
    print("Soma:", resultado)

# Método sem retorno
# Responsabilidade do método: solicitar o nome garantindo no mínimo 3 carac
def solicitar_nome() -> str:
    nome_solicitado = input("Digite i nome: ").strip()
    while len(sobrenome_solicitado) < 3:
        print("Nome inválido, deve conter no mínimo 3 caracteres")
        nome_solicitado = input("Digite o nome: ").strip()
    return nome_solicitado

# Método com retorno do tipo string
# Responsabilidade do método: solicitar o sobrenome garantindo no mínimo 3 e máximo 100
def solicitar_sobrenome() -> str:
    sobrenome_solicitado = input("Digite o sobrenome: ").strip()
    while len(sobrenome_solicitado) < 3 or len(sobrenome_solicitado) > 100:
        print("Sobrenome inválido, deve conter no mínimo 3 caracteres e no máximo 100")
        sobrenome_solicitado = input("Digite o sobrenome: ").strip()
    return sobrenome_solicitado

# Método sem retorno
def apresentar_nome_completo():
    # Executando o método solicitar_nome() e armazenando seu retorno na variável nome
    nome = solicitar_nome()
    # Executando o método solicitar_sobrenome() e armazenando seu retorno na variável sobrenome
    sobrenome = solicitar_sobrenome()

    nome_completo = nome + "" + sobrenome
    print("Nome completo: ", nome_completo)

def solicitar_modelo() -> str:
    modelo_solicitado = input("Digite o modelo do produto: ").strip()
    while len(modelo_solicitado) < 4:
        print("Modelo inválido, deve conter no mínimo 4 caracteres")
        modelo_solicitado = input("Digite o modelo do produto: ").strip()
    return modelo_solicitado

def solicitar_quantidade() -> int:
    quantidade_solicitada = int (input("Digite a quantidade de produtos: ").strip())
    while quantidade_solicitada < 1 or quantidade_solicitada > 5:
        print("Quantidade inválida, deve solicitar no mínimo 1 e máximo 5")
        quantidade_solicitada = int (input("Digite a quantidade de produtos: ").strip())
    return quantidade_solicitada

def solicitar_preco() -> float:
    preco_solicitado = float(input("Digite o preço do produto: ").strip())
    while preco_solicitado < 100 or preco_solicitado > 500:
        print("Preço inválido, deve custar no mínimo 100 e no máximo 500")
        preco_solicitado = float(input("Digite o preço do produto: ").strip())
    return preco_solicitado

def solicitar_calcular_produto():
    modelo_produto = solicitar_modelo()
    quantidade_produto = solicitar_quantidade()
    preco_produto = solicitar_preco()

    valor_total = quantidade_produto * preco_produto
    print("O produto escolhido foi", modelo_produto)
    print("a quantidade foi de", quantidade_produto)
    print("que sairá no valor de", valor_total)

if __name__ == "__main__":
    import os
    os.system("cls")
    solicitar_calcular_produto()