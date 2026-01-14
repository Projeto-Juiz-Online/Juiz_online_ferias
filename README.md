# Juiz Online de Férias

Um mini *online judge* inspirado em plataformas como **HackerRank**, **BeeCrowd** e **LeetCode**, desenvolvido como projeto de férias para praticar programação, arquitetura e boas práticas de desenvolvimento.

A plataforma permite que usuários criem contas, escolham problemas, enviem código e vejam o resultado da execução automaticamente.

---

## 🚀 Tecnologias Utilizadas

### **Backend**
- Python 3
- Flask 
- Execução de código via `subprocess`
- Docker (Dockerfile)

### **Banco de Dados**
- SQLAlchemy

### **Frontend**
- HTML + CSS + JavaScript
- Bootstrap

---

## 📁 Estrutura do Projeto

```
JuizOnline
├── README.md
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── controller
│   │   ├── __init__.py
│   │   ├── admin_controller.py
│   │   ├── auth_controller.py
│   │   ├── problem_controller.py
│   │   ├── ranking_controller.py
│   │   ├── submission_controller.py
│   │   └── test_case_controller.py
│   ├── database.db
│   ├── models
│   │   ├── __init__.py
│   │   ├── problem.py
│   │   ├── submission.py
│   │   ├── test_case.py
│   │   └── user.py
│   ├── service
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── database.py
│   │   ├── judge.py
│   │   ├── problem_service.py
│   │   ├── ranking_service.py
│   │   ├── runner
│   │   │   ├── c_runner.py
│   │   │   ├── cpp_runner.py
│   │   │   └── python_runner.py
│   │   ├── submission_service.py
│   │   └── test_case_service.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   ├── templates
│   │   ├── admin_dashboard.html
│   │   ├── base.html
│   │   ├── create_problem.html
│   │   ├── create_submission.html
│   │   ├── create_test_case.html
│   │   ├── home.html
│   │   ├── list_problem_submissions.html
│   │   ├── list_problems.html
│   │   ├── list_test_cases.html
│   │   ├── list_user_submissions.html
│   │   ├── login.html
│   │   ├── problem.html
│   │   ├── problem_detail.html
│   │   ├── ranking.html
│   │   ├── register.html
│   │   └── submission.html
│   └── utils
│       ├── decorators.py
│       ├── sandbox.py
│       └── test.py
├── docker
│   ├── c
│   │   └── Dockerfile
│   ├── c++
│   │   └── Dockerfile
│   ├── java
│   │   └── Dockerfile
│   └── python
│       └── Dockerfile
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── 12954c2e4e01_.py
├── readme.md
├── requirements.txt
├── run.py
└── tests
    ├── test_auth.py
    ├── test_problem.py
    └── test_submission.py

````

---

## 🎯 Objetivo do Projeto

Criar um juiz online funcional ecompleto para demonstrar:

- autenticação de usuários  
- CRUD de problemas e submissões  
- execução segura (com timeout) de código Python enviado pelo usuário  
- comparação automática de output  
- aplicação organizada em camadas (controllers, services, models)  
- editor de código integrado no frontend  

---

## 🔧 Como Rodar o Projeto

### **1. Clonar o repositório**
```bash
git clone https://github.com/seu-usuario/Juiz_online_ferias.git
cd Juiz_online_ferias
````

### **2. Criar ambiente virtual**

```bash
python3 -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### **3. Instalar dependências**

```bash
pip install -r requirements.txt
```

### **4. Rodar**

```bash
flask run
```

Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## 🤝 Equipe

Projeto desenvolvido durante as férias por:

* **[Gabriel Soares Segatto](https://github.com/GabrielSSegatto)**
* **[Eduardo Jesus Dal Pizzol](https://github.com/Edupizzol)**

---

## 📜 Licença

Este projeto é livre para estudo, modificação e uso não comercial.

```

