# Entre funções colocar duas linhas
# Nome de função (def) deve ser no padrão snake_case
def exemplo_tipos_primitivos():
    # Nome de variáveis deve ser padão snake_case (nome_completo_funcionario)
    # Nome de variáveis não pode começar com números, não pode conter caracteres especiais (~,','...)
    nome: str = "PS5 Pro" # str é string (texto)
    preco: float = 7000.99 # float número real
    quantidade: int = 2 # int é inteiro
    compra_realizada: bool = True # bool é operador lógico (True: verdadeiro, False: falso)

    # calcular o total da compra
    total_compra: float = preco * quantidade

    print("Nome:", nome)
    print("Preço:", preco)
    print("Quantidade:", quantidade)
    print("Compra realizada:", compra_realizada)
    print("Total da compra:", total_compra)

def exemplo_entrada_dados():
    # input é utilizado para questionar o usuário uma entrada de dados, tudo o
    # que o usuário digitar virá como string
    nome: str = input("Digite o nome: ")
    sobrenome: str = input("Digite o sobrenome: ")
    # Convertendo o que o usuário digitou para inteiro
    idade: int = int(input("Digite a idade: "))

    # + neste cenário está concatenando o nome, espaço e o sobrenome
    nome_completo: str = nome + " " + sobrenome
    # str(idade) => convertendo de int para string
    texto: str = "Nome completo: " + nome_completo + " tem " + str(idade) + " anos"
    print(texto)


def exercicio_paciente():
    nome: str = input("Digite seu nome completo: ")
    peso: float = float(input("Digito seu peso: "))
    altura: float = float(input("Digite sua altura: "))
    email: str = input("Digite seu e-mail: ")
    imc: float = peso / (altura * altura)

    texto: str = "Seu IMC é: " + str(imc)
    print(texto)

def exercicio_carro():    
    modelo_carro: str = input("Digite o modelo do carro: ")
    quantidade_parcelas: int = int(input("Digite a quantidade de parcelas: "))
    valor_parcela: float = float(input("Qual o valor da parcela? "))
    valor_fipe: float = float(input("Qual o valor da fipe? "))
    total_pago: float = quantidade_parcelas * valor_parcela
    total_com_juros: float = total_pago - valor_fipe

    texto: str = "O modelo do carro é " + modelo_carro + " a quantidade de parcelas é de " + str(quantidade_parcelas) + " o valor total do carro é de " + str(total_pago) + " a quantidade de juros pagos é de " + str(total_com_juros)
    print(texto)

    # esse trecho é chamado quando o arquivo é executado, main é
    # o ponto de entrada(execução) de uma aplicação
if __name__ == "__main__":
    # executa a função abaixo, ou seja, executará o código que está dentro da função
    exercicio_paciente()

    # Como executar:
    # Abrir o terminal (Ctrl + J)
    # Executar o comando 'py exemplo_00_variaveis.py'