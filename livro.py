class Livro:
    def __init__(self, titulo, autor, paginas, preco):
        self.titulo_livro = titulo
        self.autor_livro = autor
        self.paginas = paginas
        self.preco_livro = preco
        self.paginas_lidas = 0
    
    def set_alterar_titulo_livro(self, novo_titulo):
        self.titulo_livro = novo_titulo
    def set_alterar_autor_livro(self, nome_autor):
        self.autor_livro = nome_autor
    def set_alterar_paginas_livro(self, qtd_paginas):
        self.paginas = qtd_paginas
    def set_alterar_preco_livro(self, novo_valor):
        self.preco_livro = novo_valor

    def mostrar_dados(self):
        print(f"Dados Livro:\nTitulo: {self.titulo_livro}\nAutor: {self.autor_livro}\nPáginas do livro: {self.paginas}\nPreço do livro: {self.preco_livro}")
    
    def aplicar_desconto(self, percentual):
        desconto = (self.preco_livro * percentual)/100
        self.preco_livro -= desconto
        print(f"No desconto de {percentual}%. O valor do desconto ficará: R$ {desconto:.2f}\nO livro ficará no valor de: R$ {self.preco_livro:.2f}")
    
    def ler_paginas(self, quantidade):
        if self.paginas_lidas + quantidade <= self.paginas:
            self.paginas_lidas += quantidade
        else:
            print("Livro finalizado...")

    def progresso(self):
        porcentagem = (self.paginas_lidas / self.paginas) * 100
        return f"Progresso: {self.paginas_lidas}/{self.paginas} páginas. ({porcentagem:.2f}%)"
    
def main():
    livro1 = Livro(titulo='Oito Assassinatos Perfeitos', autor='Peter Sweanson', paginas=300, preco=51.98)
    livro2 = Livro(titulo='A Droga da Obediência', autor='Pedro Bandeira', paginas=150, preco=25.68)
    livro3 = Livro(titulo='Assassinato de Roger Ackroyd', autor='Agatha Christie', paginas=300, preco=32.50)
    livro4 = Livro(titulo='Sobre a Brevidade da Vida', autor='Sêneca', paginas=96, preco=12.45)

    while True:
        print("---MENU---")
        liv = str(input("Escolha o livro. (livro1/livro2/livro3/livro4), ou insira 'sair' para finalizar o programa: ").lower())
        if liv == 'livro1'.lower():
            livro = livro1
        elif liv == 'livro2'.lower():
            livro = livro2
        elif liv == 'livro3'.lower():
            livro = livro3
        elif liv == 'livro4'.lower():
            livro = livro4
        else:
            print("Saindo do programa...")
            break

        if livro:
            print("--MENU LIVRO---")
            escolha = str(input("Insira o que deseja fazer: consultar/alterar/desconto/progresso.\nEscolha: ").lower())
            if escolha == 'consultar'.lower():
                livro.mostrar_dados()

            elif escolha == 'alterar'.lower():
                alt = int(input("Alterações:\n[1] - Alterar Titulo;\n[2] - Alterar Autor;\n[3] - Alterar Página;\n[4] - Alterar Preço.\nEscolha: "))
                if alt == 1:
                    titulo_novo = str(input("Insira o novo titulo do livro: "))
                    livro.set_alterar_titulo_livro(titulo_novo)
                    print("Titulo atualizado com sucesso!!")
                elif alt == 2:
                    autor_nome = str(input(f"Insira o nome atualizado do autor do livro: "))
                    livro.set_alterar_autor_livro(autor_nome)
                    print("Autor atualizado com sucesso!!")
                elif alt == 3:
                    pagina = int(input(f"Insira o número atualizado de páginas do livo: "))
                    livro.set_alterar_paginas_livro(pagina)
                    print("Páginas atualizada com sucesso!!")
                else:
                    preco_novo = float(input(f"Insira o valor atual do livro: "))
                    livro.set_alterar_preco_livro(preco_novo)
                    print("Preço atualizado com sucesso!!")

            elif escolha == 'desconto'.lower():
                desc = int(input("Insira o valor do desconto: "))
                livro.aplicar_desconto(desc)

            elif escolha == 'progresso'.lower():
                paginas_lidas = int(input("Insira quantas páginas foram lidas: "))
                livro.ler_paginas(paginas_lidas)
                print(livro.progresso())

main()