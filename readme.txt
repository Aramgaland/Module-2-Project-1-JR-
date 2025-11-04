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

git status     \\посмотреть какие файлы измененыБ и в каком они статусе

файл gitignore должен быть в корневой папке

git add .gitignore  \\ добавляем файл .gitignore

git commit -m "add gitignore"

git add ./  добавляем все файлы в директории

git commit -m "add project"

git log

git log --oneline

git commit -am "Edit readme"      am - это (add и meerge)  тиип добавь этот файл в коммит и следай сам коммит


git remote add origin https://github.com/Aramgaland/Module-2-Project-1-JR-.git

git push -u origin main



