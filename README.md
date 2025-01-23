# OrderManagementSystem (OMSYS)
Цель проекта: Разработать полнофункциональное веб-приложение на Django для управления заказами в кафе.

---

## Содержание
1. [Описание](#описание)  
2. [Требования](#требования)  
3. [Установка](#установка)  
4. [Использование](#использование)  
5. [API](#API)

---

## 1.Описание
Это веб-приложение на Django для управления задачами. Пользователи могут регистрироваться, добавлять, редактировать и удалять задачи.  

## Функциональные требования

### Добавление заказа
Через веб-интерфейс пользователь вводит номер стола и список блюд с ценами.  
Система автоматически добавляет заказ с:  
- Уникальным ID,  
- Рассчитанной общей стоимостью,  
- Статусом “в ожидании”.

---
### Удаление заказа
Пользователь через веб-интерфейс выбирает заказ по ID и удаляет его из системы.

---
### Поиск заказа
Возможность поиска заказов по:  
- Номеру стола,  
- Статусу заказа через поисковую строку.

---
### Отображение всех заказов
Веб-страница с таблицей всех заказов, отображающая:  
- ID заказа,  
- Номер стола,  
- Список блюд,  
- Общую стоимость,  
- Статус заказа.

---
### Изменение статуса заказа
Пользователь через интерфейс выбирает заказ по ID и изменяет его статус:  
- “в ожидании”,  
- “готово”,  
- “оплачено”.

---
### Расчет выручки за смену
Отдельная страница или модуль для расчета общего объема выручки за заказы со статусом “оплачено”.

## 2.Требования
Для работы проекта необходимы:  
- **Python 3.10+**  
- **Django 4.2+**  
- **Virtualenv**  

---
## 3.Установка
Следуйте этим шагам для установки и запуска проекта:  

1. **Клонируйте репозиторий:**  
   ```bash
   git clone git@github.com:osman-miskhodzhev/omsys.git
   cd omsys
2. **Скачайте папку со статикой**
    https://disk.yandex.ru/d/ipeC6hMwPRjQIQ
3. **Создайте и активируйте виртуальное окружение для работы системы**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
4. **Установите зависимости**
    ```bash
    pip install -r requirements.txt
5. **Запустите проект**
    ```bash
    python3 manage.py runserver

## 4. Использование
### Описание работы с заказами

Приложение предоставляет пользователю удобный интерфейс для управления заказами в ресторане. Основной функционал включает работу со списком заказов, добавление новых заказов, расчет выручки за смену и управление пунктами меню.

---

### Главная страница: Список заказов

#### Интерфейс:

- **Таблица заказов**:
  - **Поля таблицы**:
    - `ID` — уникальный идентификатор заказа.
    - `Номер стола` — номер стола, на который оформлен заказ.
    - `Пункты заказа` — перечень выбранных блюд/напитков.
    - `Статус` — текущий статус заказа (например, "Ожидает", "Готовится", "Оплачено") с кнопкой для изменения статуса.
    - `Операции` — действия над заказом (например, удаление заказа).
  - **Кнопки изменения статуса**: позволяют быстро обновлять состояние заказа в таблице.

- **Строка поиска**: используется для поиска заказа по различным параметрам (например, номеру стола или ID заказа).

---

### Верхнее меню

В верхней части страницы находятся следующие пункты меню:

1. **Список заказов**: переход на главную страницу с таблицей заказов.
2. **Добавить заказ**: интерфейс для создания нового заказа.
3. **Расчет выручки**: инструмент для подсчета выручки за смену.
4. **Меню**: управление пунктами меню ресторана.

---

### Добавление заказа

1. Нажмите на пункт меню **Добавить заказ**.
2. Введите номер стола, на который оформляется заказ.
3. После ввода номера стола пользователь перенаправляется на страницу добавления пунктов заказа.
4. Добавьте необходимые позиции (блюда/напитки) в заказ.
5. Сохраните заказ.
6. После сохранения пользователь автоматически перенаправляется обратно на страницу со **Списком заказов**.

---

### Расчет выручки

Инструмент предназначен для расчета выручки за смену. Алгоритм работы:

1. Перейдите в раздел **Расчет выручки**.
2. Выберите начало и конец смены.
3. Нажмите кнопку для выполнения расчета.
4. Программа подсчитает сумму выручки по всем заказам со статусом **Оплачено** за указанный период.
5. Отобразится итоговая сумма и количество заказов.

---

### Управление меню

На странице **Меню** можно добавлять новые пункты меню. 

1. Введите название блюда или напитка.
2. Укажите цену.
3. Сохраните пункт меню.

Добавленные позиции становятся доступными для выбора при создании заказов.

---

#### Примечание

Все действия интуитивно понятны и позволяют эффективно управлять заказами и меню, а также получать финансовую отчетность.

## API
## Описание работы с API

Проект реализован с использованием Django REST Framework (DRF). API предоставляет функционал для управления меню, заказами, пунктами заказа, а также возможность поиска заказов и расчета выручки.

---

### Общая структура API

#### Основные эндпоинты:
| HTTP Метод | URL                     | Описание                                           |
|------------|-------------------------|---------------------------------------------------|
| GET        | `/menu/`                | Получить список всех пунктов меню.               |
| GET, POST  | `/orders/`              | Работа с заказами (просмотр, создание).          |
| GET, PUT, DELETE | `/orders/{id}/`  | Работа с конкретным заказом.                     |
| GET, POST  | `/orders_itmes/`        | Работа с пунктами заказа (просмотр, создание).   |
| GET, PUT, DELETE | `/orders_itmes/{id}/` | Работа с конкретным пунктом заказа.         |
| GET        | `/orders/search/`       | Поиск заказов по ID, номеру стола и другим полям.|
| POST       | `/calculate-revenue/`   | Расчет выручки за смену.                         |

---
