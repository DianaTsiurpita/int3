# Лабораторна робота №3 — готовий проєкт

Реалізовано варіант А (FastAPI BackgroundTasks). У ZIP включені всі потрібні файли проєкту, налаштування Docker Compose secrets та JWT. Forecast API не публікується на хост.

## Запуск

Відкрийте PowerShell у папці `integration-3` та виконайте:

```powershell
docker compose up -d --build
```

Відкрийте http://localhost:8000/docs

1. `POST /auth/register` — зареєструйте користувача (пароль від 8 символів).
2. `POST /auth/login` — отримайте `access_token`.
3. Натисніть **Authorize**, вставте токен, підтвердьте.
4. Виконуйте `POST /orders`, `GET /orders`, `POST /orders/batch`, `PATCH /orders/{oid}`.

## Перевірки

- Без токена `/orders` повертає HTTP 401.
- `POST /orders` повертає HTTP 202, `Location`, `pending`; через GET перевірте `priced`.
- `POST /orders/batch` з 10 об'єктами повертає `total: 10` та результати.
- З 51 об'єктом повертається 422 (типовий ліміт 50).
- Зміна параметрів будинку в PATCH запускає новий прогноз; зміна `client_name` — ні.
- `docker compose stop forecast-api` дозволяє перевірити `failed` без втрати замовлення; `docker compose start forecast-api` відновлює сервіс.
- Варіант А не гарантує збереження фонового завдання після перезапуску процесу; це обмеження описано в методичці.

## Секрети

`secrets/postgres_password.txt` і `secrets/jwt_secret.txt` уже створені. Не публікуйте їх у GitHub. Файли виключені через `.gitignore`. Якщо у вас є **старий Docker volume** із PostgreSQL, пароль у секреті збережено таким, як у вихідному `.env`.

## Примітка

У цьому середовищі немає доступу до вашого локального Docker. Після завантаження потрібно перевірити запуск контейнерів на вашому комп'ютері. Експерименти, що потребують зупинки/перезапуску контейнерів, виконуються локально.
