## Diárias pagas aos deputados da Assembleia Legislativa de SC

Este repositório foi criado como projeto final da primeira certificação no Master em Jornalismo Dados, Automação e Data Storytelling do Insper. O projeto recebeu orientação de [Álvaro Justen] (https://github.com/turicas), Berbardo Vianna e Eduardo Cuducos. 

O projeto contém o código necessário para capturar atuomaticamente as informações das diárias pagas aos gabinetes dos deputados catarinenses. O programa permite baixar as planilhas de 11 anos de legislatura e convertê-las em um arquivo único no formato CSV.  

O arquivo final gerado pelo programa possui as seguintes informações: o valor da diária paga, o nome do servidor que recebeu o pagamento, o gabinete ao qual pertence o servidor, o vínculo empregatício, a data do uso da diária, a quantidade de diárias usufruídas e um relatório com mais detalhes sobre a diária. A planilha concentra os dados de 2011 a dezembro de 2021. O documento, porém, continuará sendo abastecido com as informações de 2022.

Os dados são coletados automaticamente do portal da Alesc e enviados para uma planilha no Google Sheets. A planilha foi automatizada por meio do Heroku, cuja atualização está programada para ocorrer todas as noites, às 23h30. Desta forma, é possível manter a planilha do ano em exercício atualizada com os gastos mais recentes dos gabinetes dos deputados. A planilha pode ser acessada aqui (https://bit.ly/3ESXenJ).  

### Fonte dos dados

A base de captura das informações é o [Portal da Transparência](https://transparencia.alesc.sc.gov.br/diarias_dados_abertos.php) da Assembleia Legislativa de Santa Catarina (Alesc). 
