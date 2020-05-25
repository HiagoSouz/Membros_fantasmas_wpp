Lista = open('Wat.txt', 'r',encoding='UTF8')           #Arquivo com o histórico de conversas
Membros = open('Membros.txt', 'r',encoding='UTF8')     #Arquivo com todos os membros
fantasmas = []
ativos = []


for x in Membros.readlines():          #Corrige um erro de espaço no fim de cada numero (as vezes desnecessário dependendo do .txt)
    ativos.append(x[:-1])

for line in ativos:                                     #Verifica se cada número está contido no histórico
    Lista.seek(0)                                       #Retorna ao início do arquivo em cada loop
    if line not in Lista.read():
        fantasmas.append(line)                             #Adiciona o número à lista de afk se não estiver no histórico

with open('Inativos.txt', 'w') as f:
    for item in fantasmas:
        f.write("%s\n" % item)             #Transcreve a lista de afk para um outro arquivo .txt separado