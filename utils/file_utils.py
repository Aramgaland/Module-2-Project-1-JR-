
from pathlib import Path
import uuid

# Это константы
ALLOWED_EXTENTIONS = ['.png', '.jpg', '.jpeg', '.gif']
MAX_FILE_SIZE = 5 * 1024 *1024

def is_allowed_file(filename: Path) -> bool:
    """Проверяем есть ли расширение в списке разрешенных"""

    ext = filename.suffix.lower()
    print(ext)
    return ext in ALLOWED_EXTENTIONS   


def get_name(filename: Path) -> str:
    ext = filename.suffix.lower()
    unic_name = f'{uuid.uuid4().hex} {ext}'
    print(f'New file name {unic_name}')
    return unic_name


# Вызываем функцию

if __name__ == '__main':
    print(is_allowed_file(Path('test.jpg')))
    print(get_name(Path('test.jpg')))  