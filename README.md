# tango_with_django_project

Tutorial feito na disciplina Desenvolvimento WEB II

Instituto Federal Catarinense Câmpus Araquari

Curso de Bacharelado em Sistemas de Informação

* **Autor:** Wagner Esser
* **Tutorial:** [Tango With Django](http://www.tangowithdjango.com/book17/).
* **Linguagem:** Python
* **Framework:** Django

---
# TUTORIAL PARA RODAR O PROJETO
Copie o projeto no GIT:

`$ git clone https://github.com/WagnerEsser/tango_with_django_project.git`

`$ cd tango_with_django_project/`

Crie uma *Virtualenv*:

`$ mkvirtualenv rango`
> Para utilizar esse comando, *virtualenvwrapper* deve estar ativado, para ativar utilize o comando *source virtualenvwrapper.sh*

Com a *virtualenv* ativada: *(Para ativar a virtualenv: `$ workon tango`)*

`$ pip install -r requirements.txt`

`$ pip install --upgrade pip`

`$ python manage.py makemigrations`

`$ python manage.py migrate`

Crie um super usuário (administrador):

`$ python manage.py createsuperuser`

Execute com python o arquivo *populate_rango.py* (população do banco de dados):

`$ python populate_rango.py`

> Caso tenha a BING API KEY, adicione-a ao arquivo *rango/keys.py*, dentro das aspas, como segue o exemplo abaixo, caso contrário, a pesquisa não irá funcionar:
`BING_API_KEY='XXXXX'`

Execute o servidor:

`$ python manage.py runserver`

Acesse-o com http://127.0.0.1:8000/.

# ANOTAÇÕES DO TUTORIAL
---

## Virtualenv

Habilitar o *Virtualenvwrapper* na inicialização:

*Na pasta do usuário:*

`$ nano .bashrc`

*Acrescente essa linha*

`$ source virtualenvwrapper.sh`
> Virtualenvwrapper é um pacote adicional que cria um ambiente utilizável para o virtualenv, possibilita utilizar comandos como ls no virtualenv."

###### Criar um ambiente virtual
`$ mkvirtualenv nome_do_ambiente`
###### Listar *virtualenvs*
`$ lsvirtualenv`
###### Entrar na *virtualenv*
`$ workon nome_do_ambiente`
###### Sair da *virtualenv*
`$ deactivate`
###### Remover a *virtualenv*
`$ rmvirtualenv`

## Preparação do ambiente virtual (*virtualenv ativada*)

###### Listar pacotes instalados
`$ pip list`
###### Instalação de pacotes
`$ pip install pacote_a_ser_instalado`
###### Listar pacotes instalados a parte do *pip*
`$ pip freeze`

## GitHub

###### Instalar o GitHub
`$ apt-get install git`
###### Inicializar um repositório local (Somente para inicialização do projeto)
`$ git init`
*Para GitHub:*

`$ git config user.name "username"`

`$ git config user.email you@example.com`

*Para Bitbucket:*

`$ git config --global user.email "you@example.com"`

`$ git config --global user.name "Your Name"`
###### Status do GitHub
`$ git status`
###### Adicionar arquivos ao próximo *commit*
`$ git add -A`

`$ git add --all`
###### *Commit* das mudanças
`$ git commit -m "mensagem de descrição dessa atualização"`
###### Enviando o código para o Git (1ª vez)
`$ git remote add origin https://github.com/<your-github-username>/my-first-blog.git`

`$ git push -u origin nome`
###### Enviando o código para o Git
`$ git push`
###### Puxar código do Git (1ª vez - em outro computador)
`$ git clone https://github.com/<your-github-username>/<your-repository-name>.git`
###### Para *branch* específica
`$ git clone -b branch_name https://github.com/<your-github-username>/<your-repository-name>.git`
###### Atualizar repositório atual (pegar do Git)
`$ git pull`
###### Forçar `git pull`
*Busca os arquivos do Git, mas sem substituir os da máquina local ainda:*

`git fetch --all`

*Reseta os arquivos da máquina local para os arquivo do Git:*

`$ git reset --hard origin/branch_name`

## Criar arquivo *requirements.txt* - Pacotes requeridos para rodar o projeto

###### Colocar lista de pacotes instalados na *virtualenv* no arquivo
`$ pip freeze > requirements.txt`
###### Numa nova *virtualenv*, instalará todos os pacotes do arquivo
`$ pip install -r requirements.txt`
>Sempre que modificar os pacotes instalados (instalar/desinstalar), atualizar o requirements.txt

## Criar arquivo *contributors.txt* - Lista de contribuidores

###### Crie na pasta do projeto o arquivo *contributors.txt*
`$ nano contributors.txt`

*Adicione os nomes dos contribuidores do projeto*

## Criar e configurar o projeto

###### Criar projeto Django
`$ django-admin.py startproject nome_projeto`
###### Abrir *settings.py* e edite para:
~~~~
TIME_ZONE = 'America/Sao_Paulo'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
~~~~

## Arquivos do projeto

###### `__inti__.py`
*Um script Python em branco cuja presença indica ao interpretador Python que o diretório é um pacote de Python.*

###### `wsgi.py`
*Um script Python usado para ajudar a executar o seu servidor de desenvolvimento e implantar seu projeto para um ambiente de produção.*

## Criar arquivo *.gitignore* - Lista de arquivos que serão ignorados no *commit* pelo Git

###### Crie na pasta do projeto um arquivo *.gitignore*
`$ nano .gitignore`

*Adicione arquivo e diretórios que serão ignorados no push*
###### Convenção do *.gitignore*
~~~~
#Pasta media
media/

#DB
db.sqlite3

#migrations
00*_*

#Pycharm
.idea

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template 
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.cache
nosetests.xml
coverage.xml

# Translations
*.mo
*.pot

# Django stuff:
*.log

# Sphinx documentation
docs/_build/

# PyBuilder
target/
~~~~

## Criar e configurar o aplicativo

###### Criar o app
`$ python manage.py startapp nome_app`
###### Abrir *settings.py*
Adicionar o nome do app:
~~~~
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'nome_app',
)
~~~~
###### Criar o banco de dados (sem modelos criados)
`$ python manage.py migrate`
###### Rodar servidor
`$ python manage.py runserver`
###### Criação de super usuário (habilita o acesso ao painel de administração do Django)
`$ python manage.py createsuperuser`
###### Criar *urls.py* na pasta do app, e então adicionar essa linha ao *urls.py* do projeto
`url(r'^rango/', include(‘nome_app.urls'), namespace="nome_app")),`
###### Adicione as linhas abaixo para a página principal redirecionar para seu *app*
~~~~
from nome_app import views

url(r'^$', views.index, name='index'),
~~~~

## Configurar o PyCharm

1. Acesse o menu *File > Open* e selecione a pasta do projeto.
2. Acesse o menu *File > Settings* e acesse a opção *Project: project_name > Project interpreter*.
3. Selecione a *Virtualenv* desejada ou crie uma nova.
4. Acesse agora a opção *Languages & Frameworks* e selecione *Django*.
5. Habilite a opção *Enable Django Support*, selecione a pasta raiz do projeto, selecione o arquivo *settings.py* e *manage.py*.

## Banco de Dados - Criação de Modelo (*classes*)

Criar modelo no *models.py*. Exemplo:
~~~~
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
    	self.published_date = timezone.now()
    	self.save()

	def __str__(self):
    	return self.title
~~~~
Adicionar novo modelo ao *admin.py*. Exemplo:
~~~~
from .models import Post, Comment

admin.site.register(Post)
~~~~
Preparar arquivo de atualização da base de dados, adicionando os novos modelos criados (*models.py*):

`$ python manage.py makemigrations nome_app`

Implementar o arquivo de atualização no banco de dados:

`$ python manage.py migrate nome_app`

## Apresentar conteúdo

Defina uma URL no arquivo *urls.py* para que se possa acessar sua página na chamada do *link*, essa URL chamará uma *view*, crie a *view* no *views.py*, como exemplo:
~~~~
def index(request):
~~~~
Essa *view* renderizá sua página HTML, nela chama-se um template HTML, que estará em sua pasta *templates*, no return da função, passa-se 3 parâmetros, sendo eles:

+ *request*: a requisição
+ A localização do template (Ex: *index.html*)
+ Um dicionário passando todas os dados que serão utilizados na página.

Crie então um template, ex: *index.html*, e utilize as variáveis do dicionário criado.

## Criar formulário

Criar um formulário em *forms.py* conforme o modelo do banco de dados

Criar em *urls.py*, exemplo:

`url(r'^sobre/$', views.sobre, name='sobre’),`

Como essa *view* mostrará o formulário para inserir dados ou processará um formulário já requisitado (*request.POST*), logo deverá conter a verificação para gerar o formulário ou processar uma requisição:

`if request.method == 'POST':`

Por final criar a página que mostrará o formulário.
