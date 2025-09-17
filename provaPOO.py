class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def get_consultar_base(self):
        return self.base
    
    def consultar_dados(self):
        print(f"Dados do retângulo:\nBase: {self.base}\nAltura: {self.altura}")
    
    def set_alterar_altura(self, nova_altura):
        self.altura = nova_altura
        print("Altura atualizada com sucesso!!")

    def set_alterar_base(self, nova_base):
        self.base = nova_base
        print("Base atualizada com sucesso!!")
    
    def calcular_area(self):
        return self.base * self.altura

def main():
    retangulo1 = Retangulo(base=8, altura=15)
    retangulo2 = Retangulo(base=7, altura=11)

    while True:
        print("---MENU---")
        ret = str(input("Escolha o retângulo, (retangulo1/retangulo2). Ou insira 'sair' para finalizar o programa: ").lower())
        if ret == 'retangulo1'.lower():
            retangulo = retangulo1
        elif ret == 'retangulo2'.lower():
            retangulo = retangulo2
        else:
            print("Saindo do programa...")
            break
        
        if retangulo:
            print("==MENU RETÂNGULO==")
            escolha = str(input("Insira o que deseja fazer. Consultar/alterar: ").lower())
            if escolha == 'consultar'.lower():
                consul = int(input("Consultas:\n[1] - Consultar dados do retângulo;\n[2] - Consultar Área do retângulo.\nEscolha: "))
                if consul == 1:
                    retangulo.consultar_dados()
                else:
                    print(f"Área do retângulo: {retangulo.calcular_area()}")

            elif escolha == 'alterar'.lower():
                alt = int(input("Alterações:\n[1] - Alterar Altura;\n[2] - Alterar Base.\nEscolha: "))
                if alt == 1:
                    altura_nova = int(input("Insira a nova altura do retângulo: "))
                    retangulo.set_alterar_altura(altura_nova)
                else:
                    base_nova = int(input("Insira a base nova do retângulo: "))
                    retangulo.set_alterar_base(base_nova)

main()