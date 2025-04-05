# Nota: If, elif and else

---

## Escrever aqui as anotações…

| **Função** | **Descrição** | **Exemplo** |
| --- | --- | --- |
| `if` | Avalia uma condição. Se a condição for verdadeira, executa o bloco de código associado. | `python\nx = 10\nif x > 5:\n    print("x é maior que 5")\n` |
| `elif` | (abreviação de "else if") Avalia uma nova condição se a condição anterior (`if` ou `elif`) for falsa. | `python\nx = 10\nif x > 15:\n    print("x é maior que 15")\nelif x > 5:\n    print("x é maior que 5, mas menor ou igual a 15")\n` |
| `else` | Executa um bloco de código se todas as condições anteriores (`if` e `elif`) forem falsas. | `python\nx = 3\nif x > 5:\n    print("x é maior que 5")\nelif x > 2:\n    print("x é maior que 2, mas menor ou igual a 5")\nelse:\n    print("x é menor ou igual a 2")\n` |