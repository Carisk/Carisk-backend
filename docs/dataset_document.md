# Datasets 
## 1. Introdução:
Dentro de uma aplicação de aprendizagem de máquina, seja deep learning, machine learning ou até mesmo da inteligência artificial os dados são uma das partes mais delicadas. Na mioria dos projetos, há uma grande quantidade de dados a serem processados e isso demanda tempo e processamento e, no nosso caso, temos mais de 3 milhões de dados para serem processados para ai sim poderem ser usados na aplicação. 
### 1.1. Objetivos:
Esse dataset tem como objetivo fazer um retrato de todos os acidentes para que o nosso modelo possa fazer predições de modo mais preciso possível. Tendo isso, o dataset foi filtrado de modo que as informações menos relevantes fossem deixadas de lado.
### 1.2. Origem:
Os dados utilizados foram obtidos no site da Polícia Federal neste [link](https://portal.prf.gov.br/dados-abertos-acidentes) e os dados pegos foram os acidentes agrupados por pessoa, assim dando um peso maior para acidentes que tenham mais vitimas.

## 2. Descrição dos campos:
O campos do dataset são as colunas ou caracteristicas descritas em cada acidente. Abaixo será descrito o que cada campo representa e como ele pode significar algo com relação a predição. Além disso será descrito como o campo é apresentado no dataset, aleém do valor default. todos os valores são separados pelo caractere ';'.
### 2.1. Data:
Tem o formato **'dia/mes/ano'** sendo **dia**, **mes** e **ano** valores numéricos. **dia** e **mes** tem dois dígitos enquanto **ano** tem 4, sendo necessário algumas vezes zeros à esquerda para representar algumas datas. Esse campo representa a data do acidente e ode relacionar alguns períodos que são mais perigosos nas estradas, além do aumento de número de acidentes frequentemente aumentar em datas específicas como feriados (i.e. 07/09).
### 2.2. Dia da semana:
Esse campo é uma string com 3 caracteres maiúsculos que são as três primeiras letras do respectivo dia da semana (i.e. 'DOM' representa domingo).  Assim como a data o dia da semana pode influenciar no tipo de acidente, pois aos fins de semanas há mais pessoas que trafegam com objetivo de lazer do que nos dias úteis.
### 2.3. Cidade:
É uma string, separada por espaços ou não de caracteres maiusculos. Representa a cidade onde o acidente ocorreu.
### 2.4. Causa do acidente:
É uma string com caracteres maiúsculos e minúsculos e com caracteres especiais utilizados na língua portuguesa brasileira como 'ã', 'â' e entre outros. Esse será o label que o modelo retornará ao usuário.
### 2.5. Tipo do acidente:
Assim como a causa do acidente, é uma string com caracteres maiúsculos e minúsculos e com caracteres especiais utilizados na língua portuguesa brasileira como 'ç', 'í' e entre outros. representa o que o acidente foi, por exemplo: colisão, atropelamento, entre outros.
### 2.6. Hora do acidente:
Está no formato "**hora**:**minuto**" sendo que **hora** é um inteiro de dois dígitos, eventualmente com zeros a esquerda, com valores entre 00 e 24, enquanto os **minutos** são valores inteiros de dois dígitos também e igualmente possivel de haver zeros à esquerda com valores de 00 até 60. Esse campo é importante para saber qual fase do dia o acidente aconteceu, podendo ter alguma relação com a causa do acidente.
### 2.7. Unidade da Federação:
É uma string com dois caracteres maiúsculos referente a unidade da federação onde ocorreu o acidente. No Brasil como o Distrito federal não é considerado um estado, o termo levado em consideração nesse campo foi unidade da federação.
### 2.8. Tempo meteriológico:
É uma string com caracteres maiúsculos e minusculos, sem caracteres especiais e sem espaço. Esse campo informa qual era a condição meteriológica no momento do acidente, que pode ser uma possível causa do acidente ou ter alguma corelação.
### 2.9. Latitude:
É um valor de ponto flutuante, com a separação decimal representada pelo caractere '.' que representa a coodernada geográfica latitude do local do acidente. Certos locais podem ser perigosos para certo tipo de acidente.
### 2.10. Longitude:
Assim como a latitude, é um valor de ponto flutuante, com a separação decimal representada pelo caractere '.' que representa a coodernada geográfica longitude do local do acidente. Juntamente com a latitude representa o local onde o acidente ocorreu.
### 2.11. Ano de fabricação do veiculo:
É um valor numérico que representa o ano de fabricação do veículo envolvido no acidente. Relacionado principalmente com os acidentes causado por falta de manutenção do veículo.
### 2.12. Idade da vitima:
É um valor numerico que representa a idade da vítima envolvida no acidente. Pode ser útil a predizer acidentes relacionados a imprudência.
### 2.13. Gênero da vitima:
É um string que tem apenas duas opções: **Masculino** e **Feminino** e representa o gênero da vitima do acidente. 
### 2.14. Valor padrão:
Para todos os campos acima descritos, caso não tenha um valor estabelecido, receberá o valor **null** como um valor default
## 3. Detalhes técnicos:
Nesse tópico será apresentado alguns detalhes importantes com relação ao seu processamento.
### 3.1. Encoding:
O dataset original, do site da Polícia Federal, está codificado em ISO-8859-1 e a linguagem de programação Python 3.8, a qual estamos usando, tem como codificação padrão a UTF-8 então a fim de facilitar futuros preprocessamentos e até mesmo o treinamento e validação, os arquivos foram convertidos para codificação UTF-8
### 3.2. Preprocessamento:
Todos os datasets foram processados em scripts em Python 3.8, pois como a quantidade de dados é enorme, apenas tarbalho humano não era suficiente. Além disso o dataset de 2007 originalmente não possui os valores das coordenadas, então foi necessário usar uma ferramenta da geocodificação para obter esses valores e apos isso o dataset foi reprocessado para padronização. 
## 4. Restrições:
Os datasets de 2007 até 2016 não possuem dados geográficos originalmente, sendo necessário a geocodificação desse dataset. As ferramentas gratuitas permitiram apenas a geocodificação do dataset de 2007. Para efeitos de treinamento esses datasets serão desconsiderados, mas ainda podem ser geocodificados.
## Referências:
ROQUIM, Fernanda V; NAKAMURA, Luis Fernando; RAMIRES, Thiago R.; LIMA, Renato R. **Regressão logı́stica**: o que leva um acidente rodoviário a ser uma tragédia?. Alfenas. 2019.