# MlUniverse

Ejercicio Ml - Prediccion de clima.

### Instalacion

Requiere [Python](https://www.python.org/) 3.5+ y [pip](https://pip.pypa.io/en/stable/) para funcionar.
> Se usa python3 como alias para Python 3.5+
> Se usa pip3 como alias para pip

Clonar repositorio.

```sh
~$ git clone [repositorio] mluniverse
~$ cd mluniverse
```

Instalar dependencias.

```sh
~/mluniverse$ pip3 install -r src/requirements/production.txt
```

Iniciar la aplicacion.

```sh
~/mluniverse$ python3 src/runserver.py <puerto>
```
> De no indicarse un puerto se toma el puerto 8080.

### Dependencias

La aplicacion requiere las siguientes dependencias para funcionar

| Nombre | Version |
| ------ | ------ |
| [Flask](http://flask.pocoo.org/) | 0.12.2 |
| [numpy](http://www.numpy.org/) | 1.13.3 |
| [peewee](http://docs.peewee-orm.com) | 2.10.2 |
| [Flask-RESTful](https://flask-restful.readthedocs.io) | 0.3.6 |

licencia
----

MIT
