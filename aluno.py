class Aluno:
    def __init__(self, nome, matricula, curso, media):
        self.nome_aluno = nome
        self.matricula = matricula
        self.curso = curso
        self.media_aluno = media

    def get_consutar_nome(self):
        return self.nome_aluno
    def get_consutar_matricula(self):
        return self.matricula
    def get_consutar_curso(self):
        return self.curso
    
    def set_alterar_nome(self, nome_novo):
        self.nome_aluno = nome_novo
    def set_alterar_matricula(self, nova_matricula):
        self.matricula = nova_matricula
    def set_alterar_curso(self, nome_curso):
        self.curso = nome_curso
    
    def media(self):
        soma = 0
        qtd = 0

        for i in range(1, 5):
            nota = input(f"Insira a {i}ª nota do aluno: ")
            if nota == "":
               nota = 0
               print("Não aceitamos campos vazios")
               break
            else:
                nota = float(nota)
            
            soma += nota
            qtd += i
            self.media_aluno = nota

        med = soma/qtd
        print(f"Média do aluno: {med:.2f}")

    def aprovado_or_nao(self):
        if self.media >= 7:
            print("Aluno Aprovado!!")
        elif self.media >= 5 or self.media <= 6:
            print("Aluno de Recuperação!!")
        else:
            print("Aluno Reprovado!!")

def main():
    aluno1 = Aluno(nome='Ryan', matricula=22508757, curso='ADS', media=0)
    aluno2 = Aluno(nome='Sabrina', matricula=22308956, curso='Direito', media=0)
    aluno3 = Aluno(nome='Jurandir', matricula=22846975, curso='Gastronômia', media=0)
    aluno4 = Aluno(nome='Valentina', matricula=22505874, curso='Medicina', media=0)

    while True:
        print("---MENU---")
        aprendiz = str(input("Escolha o aluno, (aluno1, aluno2, aluno3, aluno4), ou insira 'sair' para finalizar o programa: ").lower())
        if aprendiz == 'aluno1'.lower():
            aluno = aluno1    
        elif aprendiz == 'aluno2'.lower():
            aluno = aluno2        
        elif aprendiz == 'aluno3'.lower():
            aluno = aluno3
        elif aprendiz == 'aluno4'.lower():
            aluno = aluno4
        elif aprendiz == 'sair'.lower():
            print("Saindo do programa...")
            break
        else:
            print("Dados incorretos. Tente novamente!")
            continue

        if aluno:
            print("---MENU ALUNO---")
            escolha = str(input("Insira o que queira fazer, consultar/alterar/media/aprovacao: ").lower())
            if escolha == 'consultar'.lower():
                consul = int(input("Consultas:\n[1] - Consultar nome;\n[2] - Consultar matrícula;\n[3] - Consultar curso;\nEscolha: "))
                if consul == 1:
                    print(f"Nome: {aluno.get_consutar_nome()}")
                elif consul == 2:
                    print(f"Matrícula: {aluno.get_consutar_matricula()}")
                else:
                    print(f"Curso: {aluno.get_consutar_curso()}")
                
            elif escolha == 'alterar'.lower():
                alt = int(input("Alterações:\n[1] - Alterar nome;\n[2] - Alterar matrícula;\n[3] - Alterar curso;\nEscolha: "))
                if alt == 1:
                    novo_nome = str(input("Insira o nome do aluno: "))
                    aluno.set_alterar_nome(novo_nome)
                    print("Nome atualizado com sucesso!!")
                elif alt == 2:
                    matricula_nova = int(input("Insira a nova matrícula do aluno: "))
                    aluno.set_alterar_matricula(matricula_nova)
                    print("Matrícula atualizada com sucesso!!")
                else:
                    novo_curso = str(input("Insira o nome do curso: "))
                    aluno.set_alterar_curso(novo_curso)
                    print("Curso atualizado com sucesso!!")
                
            elif escolha == 'media'.lower():
                aluno.media()

            elif escolha == 'aprovacao'.lower():
                aluno.aprovado_or_nao()

main()