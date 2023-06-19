# Tsurei
Tsurei is a online library of manga/manhwa, where the administrators upload the content to the website, and the users can freely read. It's the capstone project for the CS50W Web Programming Course.

## How to Run the Project
### Windows Configuration

#### Install Git

    https://git-scm.com/downloads

#### Clone Project

    git clone https://github.com/dudujunior12/cs50w-project5-capstone

#### Change directory

    cd cs50w-project5-capstone

#### Install and Configure Virtual Environment

    pip install virtualenv
    python -m venv venv
    venv/Scripts/activate

#### Download dependencies

    pip install -r requirements.txt

Set .env file

    touch .env

##### With your favorite editor edit the file and include the line below

    SECRET_KEY=*GENERATE A SECRET KEY*

ex: https://djecrety.ir/

#### Migrate django models

    python manage.py makemigrations manga
    python manage.py migrate

#### Run server

    python manage.py runserver
    
### Linux Configuration

#### Install Git

    sudo apt install git

#### Clone Project

    git clone https://github.com/dudujunior12/cs50w-project5-capstone

#### Change directory

    cd cs50w-project5-capstone

#### Install and Configure Virtual Environment

    sudo apt-get python3-virtualenv
    python3 -m venv venv
    source venv/bin/activate

#### Download dependencies

    pip install -r requirements.txt

Set .env file

    touch .env

##### With your favorite editor edit the file and include the line below

    SECRET_KEY=*GENERATE A SECRET KEY*

ex: https://djecrety.ir/

#### Migrate django models

    python3 manage.py makemigrations manga
    python3 manage.py migrate

#### Run server

    python3 manage.py runserver
