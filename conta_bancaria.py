class Conta_bancaria:
    def __init__(self, titular, saldo, numero_conta, limite):
        self.titular = titular
        self.saldo = saldo
        self.num_conta = numero_conta
        self.limite_conta = limite

    def consultar_dados(self):
        print(f"Conta Bancária:\nTitular: {self.titular}\nSaldo da conta: {self.saldo}\nNúmero da conta: {self.num_conta}\nLimite da conta: {self.limite_conta}")

    def set_alterar_titular(self, novo_titular):
        self.titular = novo_titular
    
    def set_alterar_limite_conta(self, novo_limite):
        self.limite_conta = novo_limite
    
    def sacar(self, valor):
        if self.saldo + self.limite_conta >= valor:
            self.saldo = self.saldo - valor
            print("Saque efetuado com sucesso!!")
        else:
            print("Saldo insuficiente.")
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def transferir(self, conta_destino, valor):
        if self.saldo + self.limite_conta >= valor:
            self.saldo = self.saldo - valor
            conta_destino.depositar(valor)
            print(f"Transferência realizada com sucesso para a conta de: {conta_destino.titular}\nNo valor de: R$ {valor:.2f}")
        else:
            print("Saldo insuficiente.")

class Usuario:
    def __init__(self, nome, rg, cpf, cidade):
        self.nome_user = nome
        self.rg = rg
        self.cpf = cpf
        self.cidade_user = cidade

    def mostrar_dados(self):
        print(f"Pessoa:\nNome: {self.nome_user}\nRG: {self.rg}\nCPF: {self.cpf}\nCidade: {self.cidade_user}")
    
    def set_alterar_nome(self, novo_nome):
        self.nome_user = novo_nome
    def set_alterar_rg(self, rg_atualizado):
        self.rg = rg_atualizado
    def set_alterar_cpf(self, cpf_atualizado):
        self.cpf = cpf_atualizado
    def set_alterar_cidade(self, cidade_atual):
        self.cidade_user = cidade_atual
    

def main():
    conta_pessoa1 = Conta_bancaria(titular='Jodiscley', saldo=2560.98, numero_conta=15664, limite=5630)
    pessoa1 = Usuario(nome='Jodiscley', rg=6888759638, cpf=36284526851, cidade='Águas Claras')

    conta_pessoa2 = Conta_bancaria(titular='Matilda', saldo=684.57, numero_conta=15665, limite=3980)
    pessoa2 = Usuario(nome='Matilda', rg=963264510, cpf=84532169712, cidade='Taguatinga Sul')

    conta_pessoa3 = Conta_bancaria(titular='Jorjinho', saldo=6857.45, numero_conta=15666, limite=8650)
    pessoa3 = Usuario(nome='Jorjinho', rg=689574813, cpf=84576932415, cidade='Lago Sul')

    while True:
        print("---MENU---")
        pes = str(input("Insira a conta/pessoa. (pessoa1/pessoa2/pessoa3), ou insira 'sair' para finalizar o programa: ").lower())

        if pes == 'pessoa1'.lower():
            pessoa = pessoa1
            conta = conta_pessoa1
        elif pes == 'pessoa2'.lower():
            pessoa = pessoa2
            conta = conta_pessoa2
        elif pes == 'pessoa3'.lower():
            pessoa = pessoa3
            conta = conta_pessoa3
        else:
            print("Saindo do programa...")
            break
                    
        if pessoa:
            print("---MENU PESSOA---")
            escolha = str(input("Insira o que deseja fazer. Consultar/alterar/operacoes: ").lower())
            if escolha == 'consultar'.lower():
                people_or_cont = str(input("Escolha entre. (pessoa/conta): ").lower())
                if people_or_cont == 'pessoa'.lower():
                    pessoa.mostrar_dados()
                else:
                    conta.consultar_dados()

            elif escolha == 'alterar'.lower():
                conta_ou_pessoa = str(input("Escolha entre. (pessoa/conta): ").lower())
                if conta_ou_pessoa == 'pessoa':
                    alt = int(input("Alterações:\n[1] - Alterar nome;\n[2] - Alterar RG;\n[3] - Alterar CPF;\n[4] - Alterar Cidade.\nEscolha: "))
                    if alt == 1:
                        nome_novo = str(input("Insira o nome atualizado: "))
                        pessoa.set_alterar_nome(nome_novo)
                        print("Nome atualizado com sucesso!!")
                    elif alt == 2:
                        rg_atual = int(input("Insira o RG atual: "))
                        pessoa.set_alterar_rg(rg_atual)
                        print("RG atualizado com sucesso!!")
                    elif alt == 3:
                        cpf_atual = int(input("Insira o CPF atualizado: "))
                        pessoa.set_alterar_cpf(cpf_atual)
                    else:
                        cidade_nova = str(input("Insira a cidade atualizada: "))
                        pessoa.set_alterar_cidade(cidade_nova)
                        print("Cidade atualizada com sucesso!!")
                
                else:
                    alter = int(input("Alterações:\n[1] - Alterar Titular;\n[2] - Alterar Limite.\nEscolha: "))
                    if alter == 1:
                        titular_novo = str(input("Insira o nome do titular: "))
                        conta.set_alterar_titular(titular_novo)
                        print("Titular atualizado com sucesso!!")
                    else:
                        novo_limite = float(input("Insira o limite atual da conta: "))
                        conta.set_alterar_limite_conta(novo_limite)
                        print("Limite atualizado com sucesso!!")

            elif escolha == 'operacoes'.lower():
                opera = int(input("Operações:\n[1] - Sacar;\n[2] - Depositar;\n[3] - Transferir.\nEscolha: "))
                if opera == 1:
                    valor_saque = float(input("Insira o valor do saque: "))
                    conta.sacar(valor_saque)
                elif opera == 2:
                    valor_deposito = float(input("Insira o valor do depósito: "))
                    conta.depositar(valor_deposito)
                    print("Depósito feito com sucesso!!")
                else:
                    destino_conta = str(input("Insira a conta destino. Ex: conta_pessoa1.\nConta destino: ").lower())
                    valor_transferencia = float(input("Insira o valor da transferência: "))
                    conta.transferir(destino_conta, valor_transferencia)

        else:
            print("Dados incorretos. Tente novamente!!")


main()