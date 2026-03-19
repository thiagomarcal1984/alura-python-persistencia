# Listas, Tuplas e Dicionários
## Características e declaração de uma lista
Listas são 1) ordenadas e 2) mutáveis.

```python
# Lista vazia
lista = []
lista
# Saída: 
# [] 

lista = [1, 'python', 2]
lista
# Saída: 
# lista = [1, 'python', 2]

# Acesso a um elemento específico da lista:
lista[0]
# Saída: 
# 1
lista[2]
# Saída: 
# 2

# Alterando um item da lista:
lista[0] = 'Alterado'
lista
# Saída: 
# ['Alterado', 'python', 2]
```
## Adicionando elementos na lista
1. Usando o método `append`:
```python
lista = ['Alterado', 'python', 2]
lista.append('novo elemento')
lista
# Saída:
# ['Alterado', 'python', 2, 'novo elemento']
```
2. Usando o método `insert` (com dois parâmetros, sendo o primeiro a posição na lista e o segundo o elemento a ser inserido):
```python
lista = ['Alterado', 'python', 2, 'novo elemento']
lista.insert(0, 'Elemento zero')
lista
# Saída: 
# ['Elemento zero', 'Alterado', 'python', 2, 'novo elemento']
```
