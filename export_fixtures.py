import io
from django.core.management import call_command

# Створення файлу з правильним кодуванням UTF-8
with io.open('fixtures/cat.json', 'w', encoding='utf-8') as output_file:
    try:
        call_command('dumpdata', 'goods.Categories', indent=2, stdout=output_file)
        print("Дані успішно експортовані до 'fixtures/cat.json'")
    except Exception as e:
        print(f"Помилка під час експорту: {e}")
