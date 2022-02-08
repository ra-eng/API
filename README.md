# RESTful APIs Example

[![Python Version](https://img.shields.io/badge/python-3.68-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0.1-brightgreen.svg)](https://djangoproject.com)

##  Esse Projeto foi criado para marcação de pontos de registros dos funcionários. 
Essas marcações devem ocorrer em um intervalo de tempo muito pequeno e para isso foi montada uma api em que é possível adicionar ou remover informações do funcionário tais quais:  

```
{"includedAt":"2021-03-15 15:10:00", "employeeId": 123, "employerId": 999} 
```
Essas informações são armazenadas em um banco de dados inicialmente e após a inserção dos dados, os mesmos devem ser enviados para a api do sistema legado

## Running the Project Locally

Clone o repositório para a máquina local:

```bash
git clone https://github.com/ra-eng/API
```

Instale os requisitos:

```bash
pip install -r requirements.txt
```

Criação do banco de dados :

```bash
python manage.py migrate
```

Rode o servidor ! 
```bash
python manage.py runserver
```

Execução dos testes 

```bash
python manage.py test 
```

O projeto estara disponível em:  **localhost:8000**
Após a inserção dos dados é necessário enviá-los pelo usando o comando **send
```bash
 localhost:8000/send
```



