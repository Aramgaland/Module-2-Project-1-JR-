

import uvicorn
from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles
from utils.file_utils import is_allowed_file, MAX_FILE_SIZE, get_name
from pathlib import Path


# Создали эклемпляр класса, это само приложение
app = FastAPI()

# Подключаем папку static, где  css, js, картинки
app.mount("/static", StaticFiles(directory="static"), name="static")

# Задаем директорию для шаблона, папку templates
templates = Jinja2Templates(directory='templates')   

# Задаем маршруты с методом .get Это функции представления или Вьюшки, ведут на страницы
# для главной срабатывает функция индекс итд

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    context = {'request':request}
    return templates.TemplateResponse('index.html', context=context)

@app.get('/images/', response_class=HTMLResponse)
async def images(request: Request):
    context = {'request':request}
    return templates.TemplateResponse('images.html', context=context)

@app.get('/upload/', response_class=HTMLResponse)
async def upload_get(request: Request):
    context = {'request':request}
    return templates.TemplateResponse('upload.html', context=context)

@app.post('/upload/')
async def upload_image(file: UploadFile = File(...)):
    
    print(f'File: {file.filename} recieved')
    my_file = Path(file.filename)
    if is_allowed_file(my_file):
        print('Correct extention!')
    else:
        print('Wrong extention!')
        raise HTTPException(status_code=400, detail='File does not fit')

    content = await file.read(MAX_FILE_SIZE + 1)
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail='File is too big')
    

    # СОздаем папку для картинок и указываем его путь
    new_file_name = get_name(my_file)
    print(f'New file name: {new_file_name}')

    image_dir = Path('images')
    image_dir.mkdir(exist_ok=True)

    save_path = image_dir / new_file_name

    # Сохраняем сам файл
    save_path.write_bytes(content)

    print(f'{save_path}')
    
    return PlainTextResponse(f"All is good, tha is your file: {file.filename}")




#  uvicorn app:app --reload --host localhost --port 8001    чтобы запустить сервер с терминала
# Вызываем функцию
if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)