import os
import django
from django.apps import apps


def get_project_name():
    for item in os.listdir('.'):
        if os.path.isdir(item) and os.path.isfile(os.path.join(item, 'settings.py')):
            return item
    return os.path.basename(os.getcwd())


def build_tree(start_path, indent=""):
    tree_lines = []
    items = sorted(os.listdir(start_path))
    for i, item in enumerate(items):
        path = os.path.join(start_path, item)
        connector = "└── " if i == len(items) - 1 else "├── "
        tree_lines.append(f"{indent}{connector}{item}")
        if os.path.isdir(path) and not item.startswith(".") and item not in ["__pycache__", "venv"]:
            next_indent = indent + ("    " if i == len(items) - 1 else "│   ")
            tree_lines.extend(build_tree(path, next_indent))
    return tree_lines


def get_models_info():
    models_info = []
    for model in apps.get_models():
        app_label = model._meta.app_label
        model_name = model.__name__
        fields = []
        for field in model._meta.fields:
            field_type = field.get_internal_type()
            field_name = field.name
            fields.append(f"- **{field_name}** ({field_type})")
        model_doc = f"### Модель `{model_name}` (приложение `{app_label}`)\n" + "\n".join(fields)
        models_info.append(model_doc)
    return "\n\n".join(models_info)


def get_requirements():
    if not os.path.exists("requirements.txt"):
        return "Файл requirements.txt не найден."
    with open("requirements.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    if not lines:
        return "Файл requirements.txt пуст."
    return "\n".join(f"- {line}" for line in lines)


def generate_md():
    project_name = get_project_name()

    # --- Заголовок и описание ---
    md = [f"# Проект: {project_name}\n", "## Описание\nTODO: Добавить описание проекта.\n"]

    # --- Структура проекта ---
    md.append("## Структура проекта\n")
    md.append("```\n")
    md.extend(build_tree('.'))
    md.append("```\n")

    # --- Структура базы данных ---
    md.append("## Структура базы данных\n")
    md.append(get_models_info())

    # --- Установленные библиотеки ---
    md.append("\n## Установленные библиотеки\n")
    md.append(get_requirements())

    with open("PROJECT_INFO.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system.settings")  # заменить на свой settings
    django.setup()
    generate_md()
    print("Файл PROJECT_INFO.md успешно создан!")