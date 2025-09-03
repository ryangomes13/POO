class Veiculo:
    def __init__(self, nome, preco, ano_fabricacao, marca):
        self.nome = nome
        self.preco = preco
        self.ano_fabricacao = ano_fabricacao
        self.marca = marca

    def get_consultar_nome(self):
        return self.nome
    def get_consultar_preco(self):
        return self.preco
    def get_consultar_ano(self):
        return self.ano_fabricacao
    def get_consultar_marca(self):
        return self.marca
    
    def set_alterar_nome(self, novo_nome):
        self.nome = novo_nome
    def set_alterar_preco(self, novo_preco):
        self.preco = novo_preco
    def set_alterar_ano_fabricacao(self, ano_atualizado):
        self.ano_fabricacao = ano_atualizado
    def set_alterar_marca(self, nova_marca):
        self.marca = nova_marca
    
    def consultar_veiculo(self):
        print(f"Veículo:\nNome: {self.nome}\nPreço: {self.preco}\nAno de Fabricação: {self.ano_fabricacao}\nMarca: {self.marca}")
    def aumentar_preco(self, aumento):
        self.preco = self.preco + aumento

def main():
    vec1 = Veiculo(nome="Jetta", preco=220000, ano_fabricacao=2006, marca="Volkswagem")
    # print(vec1)
    vec2 = Veiculo(nome="Argo", preco=80000, ano_fabricacao=2017, marca="Fiat")
    # print(vec1)

    # print(f"Veiculo 1:\nNome = {vec1.get_consultar_nome()}\nPreço = {vec1.get_consultar_preco()}\nAno de Fabricação = {vec1.get_consultar_ano()}\nMarca = {vec1.get_consultar_marca()}")
    # print(f"Veiculo 2:\nNome = {vec2.get_consultar_nome()}\nPreço = {vec2.get_consultar_preco()}\nAno de Fabricação = {vec2.get_consultar_ano()}\nMarca = {vec2.get_consultar_marca()}")

    while True:
        print("---MENU---")
        veic = int(input("Insira qual veículo deseja fazer as alterações, (veículo 1/ veículo 2): "))
        if veic == 1:
            print("Opções:\n[1] - Alterar nome do veiculo;\n[2] - Alterar o preço;\n[21] - Aumentar o valor do veículo;\n[3] - Alterar o ano de fabricação;\n[4] - Alterar/Atualizar marca;\n[5] - Consultar Veículo;\n[6] - Sair.")
            escolha = int(input("Escolha: "))
            if escolha == 1:
                nome = str(input("Insira o novo nome do veículo: "))
                vec1.set_alterar_nome(nome)
                print("Nome atualizado com sucesso!!")
            elif escolha == 2:
                preco = float(input("Insira o valor a ser alterado do veículo: "))
                vec1.set_alterar_preco(preco)
                print("Valor atualizado com sucesso!!")
                if escolha == 21:
                    aumento = float(input("Insira o valor a ser somado: "))
                    vec1.aumentar_preco(aumento)
                    print("Valor aumentado com sucesso!!")
            elif escolha == 3:
                ano = int(input("Insira o ano de fabricação: "))
                vec1.set_alterar_ano_fabricacao(ano)
                print("Ano de Fabricação atualizado com sucesso!!")
            elif escolha == 4:
                nova_marca = str(input("Insira o nome da marca do veículo: "))
                vec1.set_alterar_marca(nova_marca)
                print("Marca do veículo atualizada com sucesso!!")
            elif escolha == 5:
                vec1.consultar_veiculo
            else:
                break

        if veic == 2:
            print("Opções:\n[1] - Alterar nome do veiculo;\n[2] - Alterar o preço;\n[21] - Aumentar o valor do veículo;\n[3] - Alterar o ano de fabricação;\n[4] - Alterar/Atualizar marca;\n[5] - Consultar Veículo;\n[6] - Sair.")
            escolha = int(input("Escolha: "))
            if escolha == 1:
                nome = str(input("Insira o novo nome do veículo: "))
                vec2.set_alterar_nome(nome)
                print("Nome atualizado com sucesso!!")
            elif escolha == 2:
                preco = float(input("Insira o valor a ser alterado do veículo: "))
                vec2.set_alterar_preco(preco)
                print("Valor atualizado com sucesso!!")
                if escolha == 21:
                        aumento = float(input("Insira o valor a ser somado: "))
                        vec2.aumentar_preco(aumento)
                        print("Valor aumentado com sucesso!!")
            elif escolha == 3:
                ano = int(input("Insira o ano de fabricação: "))
                vec2.set_alterar_ano_fabricacao(ano)
                print("Ano de Fabricação atualizado com sucesso!!")
            elif escolha == 4:
                nova_marca = str(input("Insira o nome da marca do veículo: "))
                vec2.set_alterar_marca(nova_marca)
                print("Marca do veículo atualizada com sucesso!!")
            elif escolha == 5:
                vec2.consultar_veiculo
            else:
                break

main()