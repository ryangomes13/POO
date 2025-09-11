class Produto:
    def __init__(self, nome, quantidade, preco_unitario, codigo):
        self.nome_produto = nome
        self.quantidade = quantidade
        self.preco = preco_unitario
        self.codigo_produto = codigo

    def get_consultar_nome(self):
        return self.nome_produto
    def get_consultar_qtd(self):
        return self.quantidade
    def get_consultar_preco(self):
        return self.preco
    def get_consultar_codigo(self):
        return self.codigo_produto
    
    def set_alterar_nome_produto(self, nome_atual_produto):
        self.nome_produto = nome_atual_produto    
    def set_alterar_quantidade(self, qtd_atual):
        self.quantidade = qtd_atual    
    def set_alterar_preco(self, preco_atual):
        self.preco = preco_atual
    def set_alterar_codigo(self, novo_codigo):
        self.codigo_produto = novo_codigo

    def mostrar_dados(self):
        print(f"Dados do produto:\nNome do produto: {self.nome_produto}\nQuantidade no estoque: {self.quantidade}\nPreço Unitário: {self.preco}\nCódigo do produto: {self.codigo_produto}")

    def repor_estoque(self, qtd_aumento):
        self.quantidade += qtd_aumento
    def vendas(self, qtd_estoque):
        if self.quantidade >= qtd_estoque:
            self.quantidade -= qtd_estoque
            print("Produto vendido com sucesso!!")
        else:
            print("Produto sem estoque, tente outro produto!!")
    
    def calcular_total(self, qtd_a_ser_vendido):
        return qtd_a_ser_vendido * self.preco


def main():
    produto1 = Produto(nome='Garrafa', quantidade=15, preco_unitario=14.99, codigo=1145)
    produto2 = Produto(nome='Caderno', quantidade=8, preco_unitario=38.75, codigo=1146)
    produto3 = Produto(nome='Caneta', quantidade=35, preco_unitario=2.50, codigo=1147)
    produto4 = Produto(nome='Estojo', quantidade=4, preco_unitario=10.99, codigo=1148)

    while True:
        print("---MENU---")
        pro = str(input("Insira o produto. (produto1, produto2, produto3, produto4). Ou insira 'sair' para finalizar o programa: ").lower())
        if pro == 'produto1'.lower():
            produto = produto1
        elif pro == 'produto2'.lower():
            produto = produto2
        elif pro == 'produto3'.lower():
            produto = produto3
        elif pro == 'produto4'.lower():
            produto = produto4
        elif pro == 'sair'.lower():
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente!!")
            continue


        if produto:
            print("---MENU PRODUTO---")
            escolha = str(input("Insira o que deseja fazer. alterar/consultar/repor/vender/calcular: ").lower())
            if escolha == 'consultar'.lower():
                consul = int(input("Consultas:\n[1] - Consultar nome;\n[2] - Consultar quantidade;\n[3] - Consultar preço;\n[4] - Consultar código;\n[5] - Consultar dados\nEscolha: "))
                if consul == 1:
                    print(f"Nome do produto: {produto.get_consultar_nome()}")
                elif consul == 2:
                    print(f"Quantidade: {produto.get_consultar_qtd()}")
                elif consul ==3:
                    print(f"Preço do produto: {produto.get_consultar_preco()}")
                if consul == 4:
                    print(f"Código do produto: {produto.get_consultar_codigo()}")
                else:
                    produto.mostrar_dados()

            elif escolha == 'alterar'.lower():
                alte = int(input("Alterações:\n[1] - Alterar nome;\n[2] - Alterar preço;\n[3] - Alterar código.\nEscolha: "))
                if alte == 1:
                    novo_nome = str(input("Insira o novo nome do produto: "))
                    produto.set_alterar_nome_produto(novo_nome)
                    print("Nome atualizado com sucesso!!")
                elif alte == 2:
                    preco = float(input("Insira o novo preço do produto: "))
                    produto.set_alterar_preco(preco)
                    print("Preço atualizado com sucesso!!")
                else:
                    novo_codigo = int(input("Insira o novo código do produto: "))
                    produto.set_alterar_codigo(novo_codigo)
                    print("Código atualizado com sucesso!!")

            elif escolha == 'repor'.lower():
                repor = int(input("Insira a quantidade da reposição: "))
                produto.repor_estoque(repor)
                print("Estoque atualizado!!")

            elif escolha == 'vender'.lower():
                venda = int(input("Insira quantos serão vendidos: "))
                produto.vendas(venda)

            elif escolha =='calcular'.lower():
                quantidade = int(input("Insira a quantidade a ser vendida: "))
                print(f"O valor a ser pago no {pro} será: R$ {produto.calcular_total(quantidade):.2f}")

            else:
                print("Opção inválida. Tente novamente!!")
                continue

main()