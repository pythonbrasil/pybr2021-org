# Como utilizar os scripts nesta pasta

## distribui_palestras.py

Este script espera como entrada a *planilha com as respostas dos formulários de submissão de atividades*.

O que o script faz a essa entrada?
- Filtra apenas as submissões em português
- Remove espaços na coluna de e-mail da pessoa submetedora
- Filtra apenas submissões de palestras (ignorando tutoriais)
- Remove da planilha as colunas referentes à perguntas que existiam no form para a submissão de tutoriais e para submissões em espanhol (da coluna AG até o final no formulário de 2021)
- Remove da planilha as colunas referentes à perguntas irrelevantes para a avaliação (colunas E a W no formulário de 2021)
- Remove colunas referentes à coautoria (colunas Y a AA no formulário de 2021)
- Remove coluna de timestamp e idioma (colunas A e B no formulário de 2021)
- Ordena o resultado por e-mail da pessoa submetedora
- Obtém o indíce do nome de uma pessoa avalidadora para a submissão, utilizando o seguinte algoritmo:

```
(indíce da submissão + INCREMENTO) % tamanho da entrada
```

O `INCREMENTO` deve ser um número maior ou igual ao número de palestras da palestrante que mais submeteu palestras. Neste código usamos `9`.

- Como definimos que cada palestra teria três pessoas avaliadoras, utilizamos `INCREMENTO * 1` para obter a primeira, `INCREMENTO * 2` para obter a segunda, e `INCREMENTO * 3` para obter a terceira.
- O mesmo algoritmo é aplicado para obter o e-mail da pessoa avaliadora

### Como executar o script

1. Tenha a planilha com as respostas dos formulários de submissão de atividades na mesma pasta do script, com o nome `entrada-revisada.xlsx`

2. Execute o script com o comando `python3 distribui_palestras.py`

3. O script irá gerar um arquivo chamado `teste-saida.xlsx` na mesma pasta.
