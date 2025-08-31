# Проект: system

## Описание
TODO: Добавить описание проекта.

## Структура проекта

```

├── .git
├── .gitignore
├── PROJECT_INFO.md
├── README.md
├── api
│   ├── __init__.py
│   ├── __pycache__
│   ├── apps.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── documentation
│   ├── 2.order_add_table_num.png
│   ├── 3.order_add_items_add.png
│   ├── 4.orders_add_orders_list.png
│   ├── delete.png
│   ├── logo.svg
│   ├── revenue.png
│   ├── revenue_result.png
│   ├── search.png
│   ├── search_order_list.png
│   ├── search_table_number.png
│   ├── start.png
│   ├── status_approved.png
│   ├── status_cancelled.png
│   └── status_pending.png
├── generate_doc.py
├── manage.py
├── menu
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── orders
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_remove_order_items_order_created_at_and_more.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── project.md
├── requirements.txt
├── static
│   ├── css
│   │   ├── base.css
│   │   ├── delete_confirm.css
│   │   └── orders.css
│   └── logo.svg
├── system
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates
    ├── 404.html
    ├── base.html
    ├── menu
    │   ├── food_add.html
    │   └── menu_list.html
    └── orders
        ├── add_items.html
        ├── delete_confirm.html
        ├── order_add.html
        ├── orders.html
        └── revenue.html
```

## Структура базы данных

### Модель `Order` (приложение `orders`)
- **id** (BigAutoField)
- **table_number** (PositiveIntegerField)
- **total_price** (DecimalField)
- **status** (CharField)
- **created_at** (DateTimeField)

### Модель `OrderItem` (приложение `orders`)
- **id** (BigAutoField)
- **order** (ForeignKey)
- **food** (ForeignKey)
- **quantity** (PositiveIntegerField)

### Модель `Food` (приложение `menu`)
- **id** (BigAutoField)
- **name** (CharField)
- **price** (DecimalField)

### Модель `LogEntry` (приложение `admin`)
- **id** (AutoField)
- **action_time** (DateTimeField)
- **user** (ForeignKey)
- **content_type** (ForeignKey)
- **object_id** (TextField)
- **object_repr** (CharField)
- **action_flag** (PositiveSmallIntegerField)
- **change_message** (TextField)

### Модель `Permission` (приложение `auth`)
- **id** (AutoField)
- **name** (CharField)
- **content_type** (ForeignKey)
- **codename** (CharField)

### Модель `Group` (приложение `auth`)
- **id** (AutoField)
- **name** (CharField)

### Модель `User` (приложение `auth`)
- **id** (AutoField)
- **password** (CharField)
- **last_login** (DateTimeField)
- **is_superuser** (BooleanField)
- **username** (CharField)
- **first_name** (CharField)
- **last_name** (CharField)
- **email** (CharField)
- **is_staff** (BooleanField)
- **is_active** (BooleanField)
- **date_joined** (DateTimeField)

### Модель `ContentType` (приложение `contenttypes`)
- **id** (AutoField)
- **app_label** (CharField)
- **model** (CharField)

### Модель `Session` (приложение `sessions`)
- **session_key** (CharField)
- **session_data** (TextField)
- **expire_date** (DateTimeField)

## Установленные библиотеки

- Django==4.2
- djangorestframework==3.15.2
- flake8==7.1.1
- pycodestyle==2.12.1
- pyflakes==3.2.0
- sqlparse==0.5.3