python -m venv venv - criar ambiente virtual
venv\Scripts\activate - ativar ambiente virtual
pip install django - instala o django
django-admin startproject project . - cria o projeto
python manage.py startapp contact  - instala o app
python manage.py runserver - roda o arquivo python
python manage.py shell - acessa o cmd do django


git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT


--------Migrando a base de dados do Django

python manage.py migrate - migra para ter acessos primeiro a executar
python manage.py makemigrations - qualquer alteração no model executar este comando


--------Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser - cria superusuario
python manage.py changepassword USERNAME - reseta a senha se esquecer


--------Trabalhando com o model do Django

# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')