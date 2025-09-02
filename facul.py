class Consumidor(object):
    def __init__(self, nome, sobrenome,  valor_compra, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.valor_compra = valor_compra
        self.ano_nascimento = ano_nascimento

    def get_consulta_nome(self):
        return self.nome

    def get_consulta_sobrenome(self):
        return self.sobrenome
    
    def get_consulta_valor_compra(self):
        return self.valor_compra
    
    def get_consulta_ano_nascimento(self):
        return self.ano_nascimento
    
    def set_nome_atualizado(self, novo_nome):
        self.nome = novo_nome

    def set_sobrenome(self, novo_sobrenome):
        self.sobrenome = novo_sobrenome

    def set_aumento_valor_da_compra(self, aumento_valor):
        self.valor_compra = self.valor_compra + aumento_valor

    def set_alterar_anonascimento(self, ano_novo):
        self.ano_nascimento = ano_novo

def main():
    cliente1 = Consumidor(nome="Jabiscleyson", sobrenome="de Oliveira", valor_compra=17.50, ano_nascimento=1978)
    cliente2 = Consumidor(nome="Claudete", sobrenome="dos Santos", valor_compra=85.99, ano_nascimento=1981)

    print(f"Dados do primeiro cliente:\nNome/Sobrenome: {cliente1.get_consulta_nome()} {cliente1.get_consulta_sobrenome()}\nValor da Compra: {cliente1.get_consulta_valor_compra()}\nAno de Nascimento: {cliente1.get_consulta_ano_nascimento()}.")
    print(f"Dados do segundo cliente:\nNome/Sobrenome: {cliente2.get_consulta_nome()} {cliente2.get_consulta_sobrenome()}\nValor da Compra: {cliente2.get_consulta_valor_compra()}\nAno de Nascimento: {cliente2.get_consulta_ano_nascimento()}.")

    cliente = int(input("Escolha qual cliente queira fazer alterações, (cliente1/cliente2): "))
    if cliente == 1:
        print("[1] - Atualizar nome e sobrenome;\n[2] - Valor da Compra;\n[3] - Atualizar Ano de Nascimento.")
        escolha = int(input("Insira a escolha: "))
        if escolha == 1:
            nome = str(input("Insira o novo nome do cliente1: "))
            sobrenome = str(input("Insira o sobrenome do cliente1: "))
            cliente1.set_nome_atualizado(nome)
            cliente1.set_sobrenome(sobrenome)
            print(f"Nome atualizado com sucesso!\nNovo nome e sobrenome: {cliente1.get_consulta_nome()} {cliente1.get_consulta_sobrenome()}.")
        elif escolha == 2:
            valor = float(input("Insira o aumento do valor da compra: "))
            cliente1.set_aumento_valor_da_compra(valor)
            print(f"Valor atualizado com sucesso!\nO novo valor da compra: {cliente1.get_consulta_valor_compra()}")
        elif escolha == 3:
            nascimento = int(input("Insira o novo ano de nascimento: "))
            cliente1.set_alterar_anonascimento(nascimento)
            print(f"Ano de Nascimento atualizado!!\nAno de Nascimento: {cliente1.get_consulta_ano_nascimento()}")
        else:
            print("Dados Incorretos....")

    if cliente == 2:
        print("[1] - Atualizar nome e sobrenome;\n[2] - Valor da Compra;\n[3] - Atualizar Ano de Nascimento.")
        escolha = int(input("Insira a escolha: "))
        if escolha == 1:
            nome = str(input("Insira o novo nome do cliente1: "))
            sobrenome = str(input("Insira o sobrenome do cliente1: "))
            cliente2.set_nome_atualizado(nome)
            cliente2.set_sobrenome(sobrenome)
            print(f"Nome atualizado com sucesso!\nNovo nome e sobrenome: {cliente2.get_consulta_nome()} {cliente2.get_consulta_sobrenome()}.")
        elif escolha == 2:
            valor = float(input("Insira o aumento do valor da compra: "))
            cliente2.set_aumento_valor_da_compra(valor)
            print(f"Valor atualizado com sucesso!\nO novo valor da compra: {cliente2.get_consulta_valor_compra()}")
        elif escolha == 3:
            nascimento = int(input("Insira o novo ano de nascimento: "))
            cliente2.set_alterar_anonascimento(nascimento)
            print(f"Ano de Nascimento atualizado!!\nAno de Nascimento: {cliente2.get_consulta_ano_nascimento()}")
        else:
            print("Dados Incorretos....")
           
main()