## Análise exploratória de dados (EDA) sobre MAxShop

## Projeto

- Usei um pipeline de Python com Pandas para remover dados em branco, dados duplicados, padronizar letras maiúscula e minúscula desorganizadas, remover numeros decimais depois da virgula de um arquivo Excel. 
- Depois disso, fiz um resumo estatístico com os dados tratados e por último criei 3 gráficos para visualizar os dados mais importantes

## Habilidades 

- Python (Pandas, Os,  matplotlib e pipeline para automatizar o tratamento dos dados) e Excel 

## Resultados e recomendações

- De acordo com os dados,  as vendas cresceram durante os 3 anos o que significa que é possível e viável abrir novas lojas em outros estados 
- Verificar o que está acontecendo com Rs, Pe, Pa, Am, Ro e Ce pois as vendas nesses estados estão baixas comparadas com os outros estados
- Número elevado de atendimento ruim (quase 30%) o que pode acarretar a perda de clientes

## Instruções

Entrada do arquivo:
- "data/raw/Vendas.xlsx"

Saída do arquivo:
- "data/processed/Vendas_tratado.xlsx"

Comando para usar o arquivo:

- python main.py para tratar o arquivo
- python dados.py para ver os dados resumidos
- Para ver os gráficos basta executar o arquivo visualização
