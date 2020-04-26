# Members API Project

## Table of Contents
1. [Project Motivation](#Motivation)
2. [Getting Started](#getting_started)
	1. [Dependencies](#dependencies)
	2. [Installing](#installing)
	3. [Executing Program](#executing)
3. [API Documentation](#Documentation)
4. [Authors & Licensing](#authors)

<a name="Motivation"></a>
## Motivation
The main motivation for this project it's enhance my knowledge in API's.
 
<a name="getting_started"></a>
## Getting Started

<a name="dependencies"></a>
### Dependencies
* Python 3.5+ (I used Python 3.7)
* Data Base libraries: SQLite3
* API libraries: Flask
* General libraries: Functools

<a name="installing"></a>
### Installing
Clone this GIT repository:
```
git clone https://github.com/gabrielboehme/Disaster-Response-Painel.git
```

<a name="executing"></a>
### Executing Program:
1. Run the following commands in the project's root directory to set up your database and API.
```
  python app.py
```  
  
<a name="Documentation"></a>

## API Documentation

### Authentication
* username: rootadmin
* password: goodpass

### Retrieving Data (Method GET)
* All users: /members
* Specific user: /members/id 

### Inserting Data (Method POST)
* Insert: /member
'''
{"name" : name, "email" : email, "level" : level}
'''

### Updating Data (Method PUT/PATCH)
* Update: /member/id
'''
{"name" : name, "email" : email, "level" : level}
'''

### Deleting Data (Method DELETE)
* Delete: /member/id


<a name="Author"></a>

## Authors

* [Gabriel Boehme](https://github.com/gabrielboehme/)

<a name="acknowledgement "></a>
## Acknowledgements

* [Flask Project](https://flask.palletsprojects.com/en/1.1.x/)
