
from pathlib import Path

# Это константы
ALLOWED_EXTENTIONS = ['.png', '.jpg', '.jpeg', '.gif']
MAX_FILE_SIZE = 5 * 1024 *1024

def is_allowed_file(filename: Path) -> bool:
    """Проверяем есть ли расширение в списке разрешенных"""

    ext = filename.suffix.lower()
    print(ext)
    return ext in ALLOWED_EXTENTIONS   


# Вызываем функцию

if __name__ == '__main':
    print(is_allowed_file(Path('test.jpg'))) 