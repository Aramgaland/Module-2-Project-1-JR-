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


https://www.toptal.com/developers/gitignore https://github.com/github/gitignore/blob/main/Python.gitignore https://git-scm.com/book/ru/v2

https://github.com/Stanislav-Wise/javarush_project.git

создадим новый коммит 

мерджим ветки

    




    





