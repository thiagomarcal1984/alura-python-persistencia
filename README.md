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

## Trabalhando com tuplas
Tuplas são 1) ordenadas e 2) imutáveis.

Note que listas também são ordenadas, mas são mutáveis. Tuplas não mudam.

```python
# Declarando uma tupla:
t = 123, 234, 'oi'
t
# Saída:
# (123, 234, 'oi')

# Acessando um elemento da tupla:
t[2]
# Saída: 
# 'oi'

t[1] = 'alterado'
# Saída: TypeError: 'tuple' object does not support item assignment
t.append('alterado')
# Saída: AttributeError: 'tuple' object has no attribute 'append'

# Criando uma tupla aninhada:
v = t, lista
type(v)
# Saída: <class 'tuple'>
v
# Saída: 
# ((123, 234, 'oi'), ['Alterado', 'python', 2, 'novo elemento'])
# Note que é uma tupla de dois elementos, sendo o primeiro uma tupla aninhada e o segundo uma lista.
```

> Note que para criar uma tupla os parênteses são opcionais:
> ```python
> tupla = 123, 234, 'oi'
> ```

## Explorando dicionários
* Dicionários são 1) não ordenados e 2) mutáveis. 
* Diferente de tuplas, dicionários são mutáveis. 
* Diferente das listas, dicionários não são ordenados.
* Dicionários funcionam como um mapeamento/armazenamento de par chave/valor.
* Dicionários são muito usados para criar arquivos no formato JSON.

```python
# Criando um dicionário:
telefones = {
    'joao': 911112222,
    'leo' : 933334444
}
telefones
# Saída:
# {'joao': 911112222, 'leo': 933334444}

# Acessando um item do dicionário `telefones` a partir da chave `joao`:
telefones['joao']
# Saída: 
# 911112222

# Acrescentando um item chave/valor ao dicionário `telefones`:
telefones['elena'] = 955556666
telefones
# Saída: 
# {'joao': 911112222, 'leo': 933334444, 'elena': 955556666}
```
