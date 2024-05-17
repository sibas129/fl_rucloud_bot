RuCloud bot

1. Установка зависимостей
```bash
pip install -r requirements.txt
```

2. Настройка окружение
-> в dotenv закидываем данные для бдшки и токен бота

3. Ставим alembic и инициализируем его, заполняем alembic.ini и прононяем миграции
```
pip install alembic
alembic init alembic
```

4. Заполняем alembic.ini и alembic/env.py
-> в alembic.ini правим строку соединения с бд
-> в env.py импортируем базовый класс и берем от него Base.metadata

5. Прогоняем миграции
```
alembic revision --autogenerate -m "first migration"
alembic upgrade head
```

6. Запуск бота
```bash
python main.py
```

Дополнительные материалы
- [Документация aiogram](https://docs.aiogram.dev/)