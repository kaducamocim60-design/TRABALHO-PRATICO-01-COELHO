# Trabalho Prático 01 — Programação Orientada a Objetos

## Descrição

Este projeto foi desenvolvido como parte da disciplina de **Programação Orientada a Objetos (POO)**, utilizando a linguagem **Python**.

O projeto apresenta a implementação de um sistema simplificado para gerenciamento de uma escola, aplicando conceitos fundamentais da Programação Orientada a Objetos e os relacionamentos entre classes representados em UML.

## Objetivo

O objetivo do trabalho é representar, por meio de classes em Python, um cenário de gerenciamento escolar envolvendo:

* Escola;
* Sala de Aula;
* Professor;
* Aluno;
* Endereço.

Também são demonstrados os seguintes relacionamentos entre as classes:

* **Composição**;
* **Associação**;
* **Agregação**.

## Classes do sistema

### Escola

Representa uma escola.

**Atributos:**

* `nome: str`
* `cnpj: str`
* `salas: list`
* `professores: list`

**Métodos:**

* `adicionar_sala()`
* `adicionar_professor()`
* `mostrar_escola()`

### SalaDeAula

Representa uma sala de aula pertencente à escola.

**Atributos:**

* `numero: int`
* `capacidade: int`

**Método:**

* `mostrar_sala()`

### Professor

Representa um professor que pode lecionar em diferentes escolas.

**Atributos:**

* `nome: str`
* `disciplina: str`
* `matricula: str`
* `escolas: list`

**Métodos:**

* `adicionar_escola()`
* `mostrar_escolas()`

### Aluno

Representa um aluno matriculado na escola.

**Atributos:**

* `nome: str`
* `matricula: str`
* `idade: int`
* `endereco: Endereco`

**Método:**

* `mostrar_aluno()`

### Endereco

Representa o endereço associado ao aluno.

**Atributos:**
