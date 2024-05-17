RuCloud bot

1. Установка зависимостей
```bash
pip install -r requirements.txt
```

2. Настройка окружение
```
в dotenv закидываем данные для бдшки и токен бота
```

3. Ставим alembic, инициализируем его, заполняем alembic.ini и прононяем миграции
```
pip install alembic
```
alembic init alembic
```
alembic revision --autogenerate -m "first migration"
```
alembic upgrade head
```

3. Запуск бота
```bash
python main.py
```

Дополнительные материалы
- [Документация aiogram](https://docs.aiogram.dev/)