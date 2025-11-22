1
pip install fastapi jinja2 uvicorn pillow

pip install fastapi[all] jinja2 uvicorn pillow



git config --global user.name "Aram"  //присвоить новое имя

git config --global user.email "granturis@yandex.ru"   //почту установить

git config (команда для настройки гита)
--global (значит эта настройка будет работать для всех проектов)

git config --global --list    посмотреть настройки своего гита



git init  создает/ инициализирует проект в гите и создает папку

 Initialized empty Git repository in C:/Users/ACER/OneDrive/Desktop/JavaRush_University/M2_Project_1/.git/

 cd ./.git  \\ зайти в созданную директорию гита

 ls -a    \\ посмотреть что в папке

ls -Force

git init

git status     \\посмотреть какие файлы изменены и в каком они статусе

файл gitignore должен быть в корневой папке

git add .gitignore  \\ добавляем файл .gitignore

git commit -m "add gitignore"

git add ./      //добавляем все файлы в директории

git commit -m "add project"  \\ делаем коммит и в кавычках название

git log      \\ запрашиваем список коммитов

git log --oneline    \\\ посмотреть одним списком коммиты


git commit -am "Edit readme"      am - это (add и meerge)  тиип добавь этот файл в коммит и следай сам коммит


git remote add origin https://github.com/Aramgaland/Module-2-Project-1-JR-.git

git branch -M main   создать ветку main

git push -u origin main     \\ пушим ветку main

git pull   \\ закачать обновленный репозиторий

git clone \\  скопировать и подключиться к новому репозиторию

git remote -v     \\ проверить есть ли подключенные удаленные репозитории

cd ..   \\ подняться папкой наверх

Ветки 

    gt checkout d598588  \\  надо вводить название хэша и мы переключимся на нужный коммит

    git branch   \\ посмотреть ветку в которой нахожусь

    git checkout main    \\ перейти в последний коммит по имени ветки

    git branch test            // создать ветку (test это название)

    git branch -a     // посмотреть удаленые ветки

    git checkout test  // переключиться к другой ветке 

https://www.toptal.com/developers/gitignore https://github.com/github/gitignore/blob/main/Python.gitignore https://git-scm.com/book/ru/v2

https://github.com/Stanislav-Wise/javarush_project.git

создадим новый коммит 



    




    
    git checkout -b effects   // создать и перейти на новую созданную ветку 

    https://github.com/Stanislav-Wise/javarush_project.git



    \\  Перекоючение веток
     git checkout main
      или
      git switch main 


      мерджим в main

      git merge test (указываем имя ветки которую хотим замерджить в ту ветку в которой мы сейчас)



git log --graph  \\ тоже показывает коммиты

git branch -d test2   \\ удаляем ветку и указываем ее имя

git branch -D test2   \\ удалит даже если были изменения без коммита



создали ветку developers


git log --oneline --autor="Aram"         \\найти коммитвы одного автора


git log --since="2025-06-19" until="2025-06-20"    \\фильтрация по дате с и до какого то числа

git log --grep="readme"   \\ найти коммит по названию

git log -- README.txt    \\ поиск измений по файлам


будем переключаться на другой коммит

git restore README.txt   \\ откатить изменения до последнего коммита

git restore .  \\ отменить изменения 

git restore --staged readme.txt

git reset --soft HEAD~1     \\ удалить предыдущий коммит 

git reset --hard HEAD~1    \\ удалит предыдущий коммит и все изменения 

git revert HEAD  \\ сщздаем новый коммит который отменит последний коммит


\\\\\\\\\\\  L20 \\\\\\\\\\\\\\\\\\\\\\\\\\\

сконфигурировали Docker файл

docker build -t image-server-2 .

<!-- запускаем образ в интерактивном режиме   -->
docker run -it -p 8000:8000 image-server-2

<!-- посмотрели наши образы и нашли свой -->
docker images 

<!-- посмотреть что запушено из контейнеров--->
docker ps

<!-- посмотреть что запущено и что остановлено  из контейнеров-->
docker ps -a


//////////////////////// docker-compose.yml   объяснения   по слоям




services:                                   открываем список сервисов проекта для заполнения и создания

  app:                                      названия базового сервиса
    build: .                                указываем куда будем собирать наш контейнер, в какую директорию  \  если точка то в ту же директорию где находится Dockerfile
    container_name: image-server-2          задаем имя нашего контейнера
    restart: unless-stopped                 добавляем рестарт \\ будет перезапускать если будут проблемы и сложности     unless-stopped        
    volumes:                                смонтируем общий том для изображений
      - images:/app/images                  для изображений в корневой папке созданного контейнера app/images 
      - logs:/app/logs                      для логов в корневой папке созданного контейнера app/logs
    expose:                                 указываем какой порт мы будем использовать
      - "8000"
    enviroment:                             можем использовать переменную окружения чтобы все писалось прямо в консоль
      PYTHONUNBUFFERED=1

volumes:                                    добавим дополнительные сервисы
  images:
  logs:




  docker compose up --build     /// так у нас будут собираться все контейнеры-сервисы прописанные в docker-compose  ... ctrl + с чтобы выйти

  docker compose up -d --build


docker compose down    /// остановить  и удалить контейнеры


<!-- добавили nginx  как сервис в докер-компос файл для отработки статики -->

docker images // предварительно можно проверить установлены ли образы nginx  и какие версии чтобы потом это добавить в докер-компос файл


docker compose logs app   \\\\\\ проверяем логи контейнера app

<!-- сконфигурировали файл  nginx.conf -->
docker compose up -d --build      запустили

docker compose ps                  проверили все ли контейнеры запустились

docker compose logs app     посмотрели логи