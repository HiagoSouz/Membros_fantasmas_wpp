# Membros_fantasmas_wpp
<h1>Simples script para encontrar membros inativos em grupos de whatsapp<h1>
  
Ps: Para total funcionalidade será necessário a realização alguns passos manuais (ainda estou terminando de automatizar totalmente)

<h2> 1° Passo: Conseguir o histórico de conversas do grupo em questão <h2>
  
Toque e segure na conversa individual ou grupo que você deseja salvar;
Selecione Enviar por e-mail;
Escolha se você deseja Anexar Mídia ou não;
Logo depois, uma tela aparecerá no seu aplicativo de e-mail com a conversa em *.txt anexada, além das mídias, se você escolheu anexá-las;
Informe um endereço de e-mail e toque em Enviar;
Salve como 'HistoricoDeConversas.txt'

<h2> 2° Passo: Conseguir os números de todos os membros <h2>
  
Para esse passo eu utilizei uma extensão do Chrome. 
  <i>'Wa Group Exporter'</i> - Extensão utilizada por mim
A forma de obter os números é irrelevante, o importante é uma lista em um arquivo.txt com todos os membros do grupo.
Salve como: 'Membros.txt'

<h2> 3° Passo: Script <h2>

Com os dois arquivos prontos, sendo o primeiro nomeado como HistoricosDeConversas.txt e o segundo Membros.txt (claro que você pode mudar, mas também deverá alterar o script) basta copiar ambos arquivos para o local de execução da sua IDE.
Após a execução um novo arquivo será criado.
Os números contidos nele serão todos os membros que não mandaram nenhuma mensagem desde a data inicial do arquivo de HistóricoDeConversas.
