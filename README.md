<h1 align="center">
  <br>
  <a href="http://www.dcs.ar"><img src="https://i.imgur.com/GgjNXNl.png" alt="DCSolutions" width="200"></a>
  <br>
Auto Change State to In Progress
  <br>
</h1>

<h4 align="center">Script que actualiza el estado de los tickets creados en aranda a In Progress

<p align="center">
  <a href="#Funciones">Funciones</a> •
  <a href="#Como se usa">Como se usa</a> •
  <a href="#Creditos">Creditos</a> •
</p>


## Funciones

* Crea el ticket en aranda
* Lo marca como ticket abierto
* Pasados un intervalo de 4-8 minutos, lo cambia a in progress

## Como se usa

Para clonar esta repositorio, vas a necesitar [Git](https://git-scm.com) y [Python](https://www.python.org/downloads/) (que viene con [pip](https://pypi.org/project/pip/)) intalados en tu PC

```bash
# Clone el repositorio.
$ git clone https://github.com/Implementation-Working-DCS/auto-inprogress-ticket.git

# Ir al repo
$ cd auto-inprogress-ticket

# Instalar dependencias
$ pip install sys
$ pip install requests 
$ pip install re

# Iniciar la app
$ python3 -m main.py
```

## Creditos

- [Matias Dante](https://github.com/matiasdante)
  
![image](https://github.com/Implementation-Working-DCS/alertOPS-auto-ack/assets/70301149/af05d4c1-5d7a-411b-86ba-b10ce41a8407)


