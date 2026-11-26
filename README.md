# Achados e Perdidos

## Descrição do projeto

Aplicação web desenvolvida como projeto interdisciplinar do 1º período do curso de Bacharelado em Engenharia de Software do IFPB. O sistema tem como objetivo facilitar a divulgação e a identificação de objetos encontrados, permitindo que usuários cadastrem objetos e que outras pessoas consultem as publicações para identificar possíveis pertences.

## Funcionalidades

- Cadastro de usuários
- Autenticação de usuários
- Cadastro de objetos encontrados
- Listagem de objetos cadastrados
- Visualização de informações dos objetos
- Pesquisa e filtragem de objetos

## Casos de uso

<img width="726" height="922" alt="Diagrama caso de uso drawio" src="https://github.com/user-attachments/assets/b0ed8b5b-f276-4ce0-899b-315c94f706e2" />

## Tecnologias utilizadas

- Python
- Flask
- HTML5
- CSS3
- Jinja2
- CSV (armazenamento de dados)

## Como executar

### Pré-requisitos

- Python 3
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/robertogomesbr/Projeto-P1-ES.git
```

### 2. Entre na pasta do projeto

```bash
cd Projeto-P1-ES
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows, utilizando PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

No Git Bash:

```bash
source venv/Scripts/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
python app.py
```

### 7. Acesse a aplicação

Abra o navegador e acesse:

http://127.0.0.1:5000

## Autores

- Roberto Gomes
- José Cesar
- Sergio Basto
- Pedro Henrique
- Juarez Filho