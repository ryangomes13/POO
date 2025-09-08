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
        pes = str(input("Insira qual pessoa deseja, consultar/fazer operações/alterar, (pessoa1, pessoa2, pessoa3), insira 'sair' para finalizar o programa: ").lower())
        if pes == 'pessoa1':
            print("---Menu Pessoa---")
            escolha = str(input("Insira o que deseja fazer, alterar/consultar/operações: ").lower())
            if escolha == 'alterar':
                print("Alterações:\n[1] - Alterar nome;\n[2] - Alterar RG;\n[3] - Alterar CPF;\n[4] - Alterar cidade.")
                alt = int(input("Escolha: "))
                if alt == 1:
                    nome_novo = str(input("Insira o novo nome da pessoa: "))
                    pessoa1.set_alterar_nome(nome_novo)
                    print("Nome atualizado com sucesso!!")
                elif alt == 2:
                    rg_atual = int(input("Insira o rg atual: "))
                    pessoa1.set_alterar_rg(rg_atual)
                    print("RG atualizado com sucesso!!")
                elif alt == 3:
                    cpf_atual = int(input("Insira o cpf atual: "))
                    pessoa1.set_alterar_cpf(cpf_atual)
                    print("CPF atualizado com sucesso!!")
                else:
                    cidade = str(input("Insira o nome atual da cidade: "))
                    pessoa1.set_alterar_cidade(cidade)
                    print("Cidade atualizada com sucesso!!")
                
            if escolha == 'consultar':
                consult = str(input("Insira qual consulta você deseja fazer, (pessoa/conta): "))
                if consult == 'pessoa':
                    pessoa1.mostrar_dados()
                else:
                    conta_pessoa1.consultar_dados()

            if escolha == 'operações':
                print("Operações:\n[1] - Sacar;\n[2] - Depositar;\n[3] - Transferir.")
                opera = int(input("Escolha: "))
                if opera == 1:
                    valor = float(input("Insira o valor que deseja sacar: "))
                    conta_pessoa1.sacar(valor)
                elif opera == 2:
                    valor_deposito = float(input("Insira o valor do deposito: "))
                    conta_pessoa1.depositar(valor_deposito)
                    print(f"Deposito efetuado no valor de R$ {valor_deposito}, com sucesso!!")
                else:
                    conta_destino_user = str(input("Insira qual a conta que deseja fazer a transferência, (conta2, conta3): "))
                    valor_transferencia = float(input("Insira o valor da transferência: "))
                    
                    if conta_destino_user == 'conta2':
                        conta_pessoa1.transferir(conta_pessoa2, valor_transferencia)
                    else:
                        conta_pessoa1.transferir(conta_pessoa3, valor_transferencia)

        if pes == 'pessoa2':
            print("---Menu Pessoa---")
            escolha = str(input("Insira o que deseja fazer, alterar/consultar/operações: ").lower())
            if escolha == 'alterar':
                print("Alterações:\n[1] - Alterar nome;\n[2] - Alterar RG;\n[3] - Alterar CPF;\n[4] - Alterar cidade.")
                alt = int(input("Escolha: "))
                if alt == 1:
                    nome_novo = str(input("Insira o novo nome da pessoa: "))
                    pessoa2.set_alterar_nome(nome_novo)
                    print("Nome atualizado com sucesso!!")
                elif alt == 2:
                    rg_atual = int(input("Insira o rg atual: "))
                    pessoa2.set_alterar_rg(rg_atual)
                    print("RG atualizado com sucesso!!")
                elif alt == 3:
                    cpf_atual = int(input("Insira o cpf atual: "))
                    pessoa2.set_alterar_cpf(cpf_atual)
                    print("CPF atualizado com sucesso!!")
                else:
                    cidade = str(input("Insira o nome atual da cidade: "))
                    pessoa2.set_alterar_cidade(cidade)
                    print("Cidade atualizada com sucesso!!")
                
            if escolha == 'consultar':
                consult = str(input("Insira qual consulta você deseja fazer, (pessoa/conta): "))
                if consult == 'pessoa':
                    pessoa2.mostrar_dados()
                else:
                    conta_pessoa2.consultar_dados()

            if escolha == 'operações':
                print("Operações:\n[1] - Sacar;\n[2] - Depositar;\n[3] - Transferir.")
                opera = int(input("Escolha: "))
                if opera == 1:
                    valor = float(input("Insira o valo que deseja sacar: "))
                    conta_pessoa2.sacar(valor)
                elif opera == 2:
                    valor_deposito = float(input("Insira o valor do deposito: "))
                    conta_pessoa2.depositar(valor_deposito)
                    print(f"Deposito efetuado no valor de R$ {valor_deposito}, com sucesso!!")
                else:
                    conta_destino_user = str(input("Insira qual a conta que deseja fazer a transferência, (conta1, conta3): "))
                    valor_transferencia = float(input("Insira o valor da transferência: "))
                    
                    if conta_destino_user == 'conta1':
                        conta_pessoa2.transferir(conta_pessoa1, valor_transferencia)
                    else:
                        conta_pessoa2.transferir(conta_pessoa3, valor_transferencia)

        if pes == 'pessoa3':
            print("---Menu Pessoa---")
            escolha = str(input("Insira o que deseja fazer, alterar/consultar/operações: ").lower())
            if escolha == 'alterar':
                print("Alterações:\n[1] - Alterar nome;\n[2] - Alterar RG;\n[3] - Alterar CPF;\n[4] - Alterar cidade.")
                alt = int(input("Escolha: "))
                if alt == 1:
                    nome_novo = str(input("Insira o novo nome da pessoa: "))
                    pessoa3.set_alterar_nome(nome_novo)
                    print("Nome atualizado com sucesso!!")
                elif alt == 2:
                    rg_atual = int(input("Insira o rg atual: "))
                    pessoa3.set_alterar_rg(rg_atual)
                    print("RG atualizado com sucesso!!")
                elif alt == 3:
                    cpf_atual = int(input("Insira o cpf atual: "))
                    pessoa3.set_alterar_cpf(cpf_atual)
                    print("CPF atualizado com sucesso!!")
                else:
                    cidade = str(input("Insira o nome atual da cidade: "))
                    pessoa3.set_alterar_cidade(cidade)
                    print("Cidade atualizada com sucesso!!")
                
            if escolha == 'consultar':
                consult = str(input("Insira qual consulta você deseja fazer, (pessoa/conta): "))
                if consult == 'pessoa':
                    pessoa1.mostrar_dados()
                else:
                    conta_pessoa3.consultar_dados()

            if escolha == 'operações':
                print("Operações:\n[1] - Sacar;\n[2] - Depositar;\n[3] - Transferir.")
                opera = int(input("Escolha: "))
                if opera == 1:
                    valor = float(input("Insira o valo que deseja sacar: "))
                    conta_pessoa3.sacar(valor)
                elif opera == 2:
                    valor_deposito = float(input("Insira o valor do deposito: "))
                    conta_pessoa3.depositar(valor_deposito)
                    print(f"Deposito efetuado no valor de R$ {valor_deposito}, com sucesso!!")
                else:
                    conta_destino_user = str(input("Insira qual a conta que deseja fazer a transferência, (conta2, conta1): "))
                    valor_transferencia = float(input("Insira o valor da transferência: "))
                    
                    if conta_destino_user == 'conta2':
                        conta_pessoa3.transferir(conta_pessoa2, valor_transferencia)
                    else:
                        conta_pessoa3.transferir(conta_pessoa1, valor_transferencia)

        if pes == 'sair':
            print("Saindo do programa...")
            break            
                           

main()
