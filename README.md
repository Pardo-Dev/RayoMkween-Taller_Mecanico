# Como cargar el proyecto

### 1- Crea un entorno virtual

python -m venv <nombre_entorno>

### Activa el entorno

| ***Activar el entorno virtual***| ***Desactivar el entorno virtual***|
| :- | :-|
| <nombre_entorno>\Scripts\activate | <nombre_entorno>\Scripts\deactivate |

### Instala las dependencias
`python.exe -m pip install -r requerimientos.txt`

### Crear un usuario en sql developer
`CREATE USER rayomkween IDENTIFIED BY rayomkween ACCOUNT UNLOCK;`

`GRANT connect, resource, sysdba to rayomkween;`

### Crear un super usuario
`python manage.py createsuperuser`

### Arrancar servidor local
`python manage.py runserver 8000`
