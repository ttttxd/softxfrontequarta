#Declarando as variáveis do programa
maiorNotaA = 0.0 
maiorNotaB = 0.0 
maiorNotaC = 0.0
maiorNotaD = 0.0
maiorNotaGeral = 0.0
notaTemp =""

alunoMaiorA = ""
alunoMaiorB = ""
alunoMaiorC = ""
alunoMaiorD = ""
alunoMaiorGeral = ""
alunoTemp =""

qtdAprovadosA = 0
qtdAprovadosB = 0
qtdAprovadosC = 0
qtdAprovadosD = 0

print("Programas para cadastro de notas do Vestibular")
#laço de repetição para pegar as notas e nomes dos alunoes de cada turma - Turma A
for i in range(1, 26, 1):
    print("Digite o nome do aluno " , i , "da Turma A:")
    alunoTemp = input()
    print("Digite a nota do Aluno ", i , " da Turma A: ")
    notaTemp = float (input())
    if notaTemp > maiorNotaA:
        maiorNotaA= notaTemp
        alunoMaiorA = alunoTemp
    if notaTemp >= 7.0:
        qtdAprovadosA += 1
    if notaTemp > maiorNotaGeral:
        maiorNotaGeral = notaTemp
        alunoMaiorGeral = alunoTemp
#laço de repetição para pegar as notas e nomes dos alunoes de cada turma - Turma B
for i in range(1, 26, 1):
    print("Digite o nome do aluno " , i , "da Turma B:")
    alunoTemp = input()
    print("Digite a nota do Aluno ", i , " da Turma B: ")
    notaTemp = float (input())
    if notaTemp > maiorNotaA:
        maiorNotaB= notaTemp
        alunoMaiorB = alunoTemp
    if notaTemp >= 7.0:
        qtdAprovadosB += 1
    if notaTemp > maiorNotaGeral:
        maiorNotaGeral = notaTemp
        alunoMaiorGeral = alunoTemp
#laço de repetição para pegar as notas e nomes dos alunoes de cada turma - Turma C
for i in range(1, 26, 1):
    print("Digite o nome do aluno " , i , "da Turma C:")
    alunoTemp = input()
    print("Digite a nota do Aluno ", i , " da Turma C: ")
    notaTemp = float (input())
    if notaTemp > maiorNotaC:
        maiorNotaC= notaTemp
        alunoMaiorC = alunoTemp
    if notaTemp >= 7.0:
        qtdAprovadosC += 1
    if notaTemp > maiorNotaGeral:
        maiorNotaGeral = notaTemp
        alunoMaiorGeral = alunoTemp
#laço de repetição para pegar as notas e nomes dos alunoes de cada turma - Turma D
for i in range(1, 26, 1):
    print("Digite o nome do aluno " , i , "da Turma D:")
    alunoTemp = input()
    print("Digite a nota do Aluno ", i , " da Turma D: ")
    notaTemp = float (input())
    if notaTemp > maiorNotaA:
        maiorNotaD= notaTemp
        alunoMaiorD = alunoTemp
    if notaTemp >= 7.0:
        qtdAprovadosD += 1
    if notaTemp > maiorNotaGeral:
        maiorNotaGeral = notaTemp
        alunoMaiorGeral = alunoTemp
#imprindo o resultado do Vestibular:
print("Quantidade de aprovados da turma A: ", qtdAprovadosA)
print("Quantidade de aprovados da turma A: ", qtdAprovadosB)
print("Quantidade de aprovados da turma A: ", qtdAprovadosC)
print("Quantidade de aprovados da turma A: ", qtdAprovadosD)

print("O aluno ", alunoMaiorA , " teve a maior nota da Turma A, que foi ", maiorNotaA)
print("O aluno ", alunoMaiorB , " teve a maior nota da Turma A, que foi ", maiorNotaB)
print("O aluno ", alunoMaiorC , " teve a maior nota da Turma A, que foi ", maiorNotaC)
print("O aluno ", alunoMaiorD , " teve a maior nota da Turma A, que foi ", maiorNotaD)

print("O aluno ", alunoMaiorGeral, "Teve a maior nota Geral entre todas as turmas")





