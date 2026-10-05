# Trabalho Prático 01 - Programação Orientada a Objetos

## Sistema de Gerenciamento de Escola

Este projeto foi desenvolvido em Python para representar um sistema simples de gerenciamento de uma escola, utilizando conceitos de Programação Orientada a Objetos.

## Classes

O sistema possui cinco classes:

- Escola
- SalaDeAula
- Professor
- Aluno
- Endereco

## Relacionamentos

### Composição

**Escola → SalaDeAula**

As salas de aula fazem parte da escola e, de acordo com o cenário proposto, dependem dela para existir no sistema.

Representação:

`Escola ◆── SalaDeAula`

### Associação

**Escola ↔ Professor**

A escola e o professor podem existir independentemente. Um professor também pode lecionar em mais de uma escola.

Representação:

`Escola ── Professor`

### Agregação

**Aluno ◇── Endereco**

O endereço está associado ao aluno, porém pode continuar existindo mesmo após a remoção do aluno.

Representação:

`Aluno ◇── Endereco`

## Execução

O arquivo `trabalho_pratico_01.py` apresenta no terminal exemplos dos três tipos de relacionamento.

## Tecnologias utilizadas

- Python
- Programação Orientada a Objetos
- UML
- Git e GitHub
