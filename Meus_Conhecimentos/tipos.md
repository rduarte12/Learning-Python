# Nota: Tipos

---

## Escrever aqui as anotações…

Tabela classificando alguns tipos built in de python

| Classificação | Tipo | Descrição | Exemplos |
| --- | --- | --- | --- |
| Numérico | `int` | Números inteiros | 42, -5, 123456 |
| Numérico | `float` | Números de ponto flutuante | 3.14, -0.001, 1.0 |
| Booleano | `bool` | Valores booleanos | `True`, `False` |
| Sequência | `str` | Cadeias de caracteres (strings) | "Python", 'Exemplo', "123" |
| Sequência | `list` | Lista ordenada de elementos | [7, 8, 9], ["a", "b", "c"] |
| Sequência | `tuple` | Sequência imutável de elementos | (10, 20), ("x", "y") |
| Mapeamento | `dict` | Estrutura de dados chave-valor | {"nome": "Bob", "idade": 25} |
| Conjunto | `set` | Conjunto de elementos únicos e não ordenados | {1, 2, 3}, {"apple", "banana"} |
| Conjunto | `frozenset` | Conjunto imutável de elementos únicos | frozenset([4, 5, 6]) |
| Binário | `bytes` | Sequência de bytes | b"hello", b"123" |
| Entrada | `input` | Recebe informações do usuário em string | `nome = input("Informe seu nome: ")`               >> Informe seu nome: | |
| Saída | `print` | Informa para o usuário uma string | `nome, idade = Rafael, 18 \n`            `print(nome, idade)`                                      >>Rafael 18 |

| Comando | Função |
| --- | --- |
| `python` | Abrir interface interativa |
| `exit` | Sair da interface |
| `dir()` | Retornar os métodos que pode ser utilizado pertencente a este diretório |
| `dir(’classe’)` | Retornar os métodos que pode ser utilizado pertencente a este diretório de acordo com a classificação indicada |
| `help()` | Utilizar para explicar os métodos (Tipo uma wiki para pesquisar) |
| letra “q” | Sai da documentação |

Input and Print

| Classificação | Tipo | Descrição | Exemplo |
| --- | --- | --- | --- |
| Função | `input()` | Recebe uma entrada do usuário e a retorna como uma string. | `nome = input("Digite seu nome: ")` |
| Função | `print()` | Exibe uma mensagem ou valor na tela. | `print("Olá, Mundo!")` |
| Modificação | `end` | Altera o caractere de final de linha da função `print`. | `print("Olá", end="!")` |
| Modificação | `sep` | Altera o separador entre valores múltiplos na função `print`. | `print("Python", "é", "legal", sep="-")` |
| Modificação | `flush` | Controla a força de saída na função `print`, útil para saídas em buffer. | `print("Loading...", end="", flush=True)` |
| Parâmetro | `file` | Direciona a saída da função `print` para um arquivo ou outro destino. | `print("Mensagem", file=open("arquivo.txt", "w"))` |
| Modificação | `strip` | Remove espaços em branco (ou outros caracteres especificados) da entrada da função `input`. | `nome = input("Digite seu nome: ").strip[]` |