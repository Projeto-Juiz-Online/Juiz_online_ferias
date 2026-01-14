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

online_judge/
│
├── app.py                        ← inicializa o Flask e registra blueprints
├── config.py                     ← configs (debug, db path)
│
├── models/                       ← classes de dados (User, Problem, Submission)
│   ├── **init**.py
│   ├── user.py
│   ├── problem.py
│   └── submission.py
│
├── services/                     ← lógica de negócio
│   ├── **init**.py
│   ├── auth_service.py
│   ├── judge_service.py          ← executor + comparação de output
│   └── problem_service.py
│
├── controllers/                  ← rotas Flask
│   ├── **init**.py
│   ├── auth_controller.py
│   ├── problem_controller.py
│   └── submission_controller.py
│
├── templates/                    ← HTML com Jinja2
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── problems.html
│   ├── problem_detail.html
│   └── result.html
│
├── static/                       ← CSS, JS e bibliotecas
│   ├── css/
│   ├── js/
│   └── vendor/                   ← Ace Editor, Bootstrap
│
├── database.sqlite               ← banco local
└── requirements.txt

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

