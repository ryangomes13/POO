class Livro:
    def __init__(self, titulo, autor, paginas, preco):
        self.titulo_livro = titulo
        self.autor_livro = autor
        self.paginas = paginas
        self.preco_livro = preco
        self.paginas_lidas = 0

    def get_consultar_titulo(self):
        return self.titulo_livro
    def get_consultar_autor(self):
        return self.autor_livro
    def get_consultar_paginas(self):
        return self.paginas
    def get_consultar_preco(self):
        return self.preco_livro
    
    def set_alterar_titulo_livro(self, novo_titulo):
        self.titulo_livro = novo_titulo
    def set_alterar_autor_livro(self, nome_autor):
        self.autor_livro = nome_autor
    def set_alterar_paginas_livro(self, qtd_paginas):
        self.paginas = qtd_paginas
    def set_alterar_preco_livro(self, novo_valor):
        self.preco_livro = novo_valor

    def mostrar_dados(self):
        print(f"Dados Livro:\nTitulo: {self.titulo_livro}\nAutor: {self.autor_livro}\nPáginas do livro: {self.paginas}\nPreço do livro: {self.preco_livro}.")
    
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
        menu = str(input("Digite qual livro deseja entrar no menu. (livro1/livro2/livro3/livro4), ou insira 'sair' para finalizar o programa: ").lower())
        if menu == 'livro1'.lower():
            print(f"---MENU {menu}---")
            escolha = str(input("Insira o que deseja fazer, consultar/alterar/progresso/desconto: ").lower())
            if escolha == 'consultar'.lower():
                print("Consultas:\n[1] - Consultar titulo;\n[2] - Consultar autor;\n[3] - Consultar páginas;\n[4] - Consultar preço;\n[5] - Consultar dados do livro.")
                consu = int(input("Escolha: "))
                if consu == 1:
                    print(f"Titulo: {livro1.get_consultar_titulo()}")
                elif consu == 2:
                    print(f"Autor: {livro1.get_consultar_autor()}")
                elif consu == 3:
                    print(f"Páginas: {livro1.get_consultar_paginas()}")
                elif consu == 4:
                    print(f"Preço: {livro1.get_consultar_preco()}")
                else:
                    livro1.mostrar_dados()

            elif escolha == 'alterar'.lower():
                print("Alterações:\n[1] - Alterar titulo;\n[2] - Alterar Autor;\n[3] - Alterar Número de Páginas;\n[4] - Alterar Preço.")
                alt = int(input("Escolha: "))
                if alt == 1:
                    titulo_novo = str(input("Insira o titulo do livro: "))
                    livro1.set_alterar_titulo_livro(titulo_novo)
                    print("Titulo atualizado com sucesso!!")         
                elif alt == 2:
                    autor_nome = str(input("Insira o nome do autor do livro: "))
                    livro1.set_alterar_autor_livro(autor_nome)
                    print("Autor(a) atualizado com sucesso!!")         
                elif alt == 3:
                    paginas_livro = int(input("Insira a quantidade de páginas do livro: "))
                    livro1.set_alterar_paginas_livro(paginas_livro)
                    print("Páginas atualizado com sucesso!!")         
                else:
                    preco_atual = float(input("Insira o preço atual do livro: "))
                    livro1.set_alterar_preco_livro(preco_atual)
                    print("Preço atualizado com sucesso!!")         
            
            elif escolha == 'progresso'.lower():
                qtd = int(input("Insira a quantidade de páginas já lidas: "))
                livro1.ler_paginas(qtd)
                print(livro1.progresso())

            else:
                desc = int(input("Insira o valor do desconto: "))
                livro1.aplicar_desconto(desc)

        if menu == 'livro2'.lower():
            print(f"---MENU {menu}---")
            escolha = str(input("Insira o que deseja fazer, consultar/alterar/progresso/desconto: ").lower())
            if escolha == 'consultar'.lower():
                print("Consultas:\n[1] - Consultar titulo;\n[2] - Consultar autor;\n[3] - Consultar páginas;\n[4] - Consultar preço;\n[5] - Consultar dados do livro.")
                consu = int(input("Escolha: "))
                if consu == 1:
                    print(f"Titulo: {livro2.get_consultar_titulo()}")
                elif consu == 2:
                    print(f"Autor: {livro2.get_consultar_autor()}")
                elif consu == 3:
                    print(f"Páginas: {livro2.get_consultar_paginas()}")
                elif consu == 4:
                    print(f"Preço: {livro2.get_consultar_preco()}")
                else:
                   livro2.mostrar_dados()

            elif escolha == 'alterar'.lower():
                print("Alterações:\n[1] - Alterar titulo;\n[2] - Alterar Autor;\n[3] - Alterar Número de Páginas;\n[4] - Alterar Preço.")
                alt = int(input("Escolha: "))
                if alt == 1:
                    titulo_novo = str(input("Insira o titulo do livro: "))
                    livro2.set_alterar_titulo_livro(titulo_novo)
                    print("Titulo atualizado com sucesso!!")         
                elif alt == 2:
                    autor_nome = str(input("Insira o nome do autor do livro: "))
                    livro2.set_alterar_autor_livro(autor_nome)
                    print("Autor(a) atualizado com sucesso!!")         
                elif alt == 3:
                    paginas_livro = int(input("Insira a quantidade de páginas do livro: "))
                    livro2.set_alterar_paginas_livro(paginas_livro)
                    print("Páginas atualizado com sucesso!!")         
                else:
                    preco_atual = float(input("Insira o preço atual do livro: "))
                    livro2.set_alterar_preco_livro(preco_atual)
                    print("Preço atualizado com sucesso!!")         
            
            elif escolha == 'progresso'.lower():
                qtd = int(input("Insira a quantidade de páginas já lidas: "))
                livro2.ler_paginas(qtd)
                print(livro2.progresso())

            else:
                desc = int(input("Insira o valor do desconto: "))
                livro2.aplicar_desconto(desc)

        if menu == 'livro3'.lower():
            print(f"---MENU {menu}---")
            escolha = str(input("Insira o que deseja fazer, consultar/alterar/progresso/desconto: ").lower())
            if escolha == 'consultar'.lower():
                print("Consultas:\n[1] - Consultar titulo;\n[2] - Consultar autor;\n[3] - Consultar páginas;\n[4] - Consultar preço;\n[5] - Consultar dados do livro.")
                consu = int(input("Escolha: "))
                if consu == 1:
                    print(f"Titulo: {livro3.get_consultar_titulo()}")
                elif consu == 2:
                    print(f"Autor: {livro3.get_consultar_autor()}")
                elif consu == 3:
                    print(f"Páginas: {livro3.get_consultar_paginas()}")
                elif consu == 4:
                    print(f"Preço: {livro3.get_consultar_preco()}")
                else:
                   livro3.mostrar_dados()

            elif escolha == 'alterar'.lower():
                print("Alterações:\n[1] - Alterar titulo;\n[2] - Alterar Autor;\n[3] - Alterar Número de Páginas;\n[4] - Alterar Preço.")
                alt = int(input("Escolha: "))
                if alt == 1:
                    titulo_novo = str(input("Insira o titulo do livro: "))
                    livro3.set_alterar_titulo_livro(titulo_novo)
                    print("Titulo atualizado com sucesso!!")         
                elif alt == 2:
                    autor_nome = str(input("Insira o nome do autor do livro: "))
                    livro3.set_alterar_autor_livro(autor_nome)
                    print("Autor(a) atualizado com sucesso!!")         
                elif alt == 3:
                    paginas_livro = int(input("Insira a quantidade de páginas do livro: "))
                    livro3.set_alterar_paginas_livro(paginas_livro)
                    print("Páginas atualizado com sucesso!!")         
                else:
                    preco_atual = float(input("Insira o preço atual do livro: "))
                    livro3.set_alterar_preco_livro(preco_atual)
                    print("Preço atualizado com sucesso!!")         
            
            elif escolha == 'progresso'.lower():
                qtd = int(input("Insira a quantidade de páginas já lidas: "))
                livro3.ler_paginas(qtd)
                print(livro3.progresso())

            else:
                desc = int(input("Insira o valor do desconto: "))
                livro3.aplicar_desconto(desc)

        if menu == 'livro4'.lower():
            print(f"---MENU {menu}---")
            escolha = str(input("Insira o que deseja fazer, consultar/alterar/progresso/desconto: ").lower())
            if escolha == 'consultar'.lower():
                print("Consultas:\n[1] - Consultar titulo;\n[2] - Consultar autor;\n[3] - Consultar páginas;\n[4] - Consultar preço;\n[5] - Consultar dados do livro.")
                consu = int(input("Escolha: "))
                if consu == 1:
                    print(f"Titulo: {livro4.get_consultar_titulo()}")
                elif consu == 2:
                    print(f"Autor: {livro4.get_consultar_autor()}")
                elif consu == 3:
                    print(f"Páginas: {livro4.get_consultar_paginas()}")
                elif consu == 4:
                    print(f"Preço: {livro4.get_consultar_preco()}")
                else:
                    livro4.mostrar_dados()

            elif escolha == 'alterar'.lower():
                print("Alterações:\n[1] - Alterar titulo;\n[2] - Alterar Autor;\n[3] - Alterar Número de Páginas;\n[4] - Alterar Preço.")
                alt = int(input("Escolha: "))
                if alt == 1:
                    titulo_novo = str(input("Insira o titulo do livro: "))
                    livro4.set_alterar_titulo_livro(titulo_novo)
                    print("Titulo atualizado com sucesso!!")         
                elif alt == 2:
                    autor_nome = str(input("Insira o nome do autor do livro: "))
                    livro4.set_alterar_autor_livro(autor_nome)
                    print("Autor(a) atualizado com sucesso!!")         
                elif alt == 3:
                    paginas_livro = int(input("Insira a quantidade de páginas do livro: "))
                    livro4.set_alterar_paginas_livro(paginas_livro)
                    print("Páginas atualizado com sucesso!!")         
                else:
                    preco_atual = float(input("Insira o preço atual do livro: "))
                    livro4.set_alterar_preco_livro(preco_atual)
                    print("Preço atualizado com sucesso!!")         
            
            elif escolha == 'progresso'.lower():
                qtd = int(input("Insira a quantidade de páginas já lidas: "))
                livro4.ler_paginas(qtd)
                print(livro4.progresso())

            else:
                desc = int(input("Insira o valor do desconto: "))
                livro4.aplicar_desconto(desc)

        elif menu == 'sair'.lower():
            print("Saindo do programa...")
            break

main()