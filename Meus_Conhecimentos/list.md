# Nota: Métodos de List

---

## Escrever aqui as anotações…

As listas são uma estrutura de dados fundamental em Python, permitindo armazenar coleções de itens em uma única variável. Aqui está um resumo dos principais métodos que você pode usar para manipular listas:

| **Método** | **Descrição** | **Exemplo** |
| --- | --- | --- |
| `append(x)` | Adiciona o item `x` ao final da lista | `lista.append(10)` |
| `extend(iter)` | Adiciona todos os itens de um iterável (iter) à lista | `lista.extend([1, 2, 3])` |
| `insert(i, x)` | Insere o item `x` na posição `i` | `lista.insert(2, 'a')` |
| `remove(x)` | Remove a primeira ocorrência do item `x` | `lista.remove(10)` |
| `pop([i])` | Remove e retorna o item da posição `i` (ou o último) | `lista.pop()` ou `lista.pop(2)` |
| `clear()` | Remove todos os itens da lista | `lista.clear()` |
| `index(x)` | Retorna o índice da primeira ocorrência do item `x` | `lista.index(10)` |
| `count(x)` | Retorna o número de ocorrências do item `x` | `lista.count(10)` |
| `sort()` | Ordena os itens da lista em ordem crescente | `lista.sort()` |
| `reverse()` | Inverte a ordem dos itens na lista | `lista.reverse()` |
| `copy()` | Retorna uma cópia superficial da lista | `copia = lista.copy()` |

### Explicação e Resumo

1. **Adicionar e Estender**:
    - O método `append(x)` adiciona um único item ao final da lista.
    - `extend(iter)` adiciona todos os itens de um iterável, como outra lista, à lista existente.
2. **Inserir e Remover**:
    - `insert(i, x)` permite que você insira um item em uma posição específica.
    - `remove(x)` elimina a primeira ocorrência do item especificado na lista.
3. **Manipulação de Itens**:
    - `pop([i])` remove e retorna o item de uma posição específica, ou o último item se nenhum índice for fornecido.
    - `clear()` limpa todos os itens da lista, deixando-a vazia.
4. **Buscar e Contar**:
    - `index(x)` retorna o índice da primeira ocorrência de um item.
    - `count(x)` conta quantas vezes um item aparece na lista.
5. **Ordenação e Inversão**:
    - `sort()` ordena os itens da lista em ordem crescente.
    - `reverse()` inverte a ordem dos itens na lista.
6. **Cópia**:
    - `copy()` cria uma cópia superficial da lista, permitindo modificações independentes da lista original.