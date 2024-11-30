# Методы оптимизации (app)

![Static Badge](https://img.shields.io/badge/Yamemik-methods)
![GitHub top language](https://img.shields.io/github/languages/top/Yamemik/app-optimization-methods)
![GitHub](https://img.shields.io/github/license/Yamemik/app-optimization-methods)
![GitHub Repo stars](https://img.shields.io/github/stars/Yamemik/app-optimization-methods)
![GitHub issues](https://img.shields.io/github/issues/Yamemik/app-optimization-methods)


## Общее описание
_____
### Краткое описание
Приложение с графическим интерфейсом.


### Методы оптимизации
- Методы решения многокритериальных задач;

## Техническое описание
_____
### Стек технологий:
  - Python;
  - SQLite.

### ER-Diagrams
```mermaid
erDiagram
    USER }o--o{ COURSE : wrights    
    USER {
        int id PK      
        string email "*"
        string hashed_password "*"
        bool is_active
        bool is_superuser
        bool is_verified        
    }

```


## Python
_____

### PipENV
```bash
# install pipenv
pip install pipenv
# .venv in fold of the project
$env:PIPENV_VENV_IN_PROJECT=1
# initilization
pipenv shell
# install
pipenv install
```

## Ссылки
_____
[by Yamemik](https://github.com/Yamemik)
