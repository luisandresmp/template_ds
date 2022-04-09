# Template Cookiecutter for Data Science

<!-- badges: start -->
[![@luisandresmp](https://img.shields.io/badge/@luisandresmp-Linkedin-blue?&logoColor=white)](https://www.linkedin.com/in/luisandresmartinezperaza/) 
[![Platzi](https://img.shields.io/badge/Curso_Platzi-Configuración_Avanzada_...-green&logoColor=white)](https://platzi.com/datos/)
<!-- badges: end -->

Template cookiecutter created in course 'Configuración Profesional de Entorno de Trabajo para Ciencia de Datos' of Platzi.

## Requirements

- [Python](https://www.python.org/downloads/) >= 3.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:

``` bash
pip install cookiecutter
```

## Create a new Project

En el directorio en el que quieras guardar tu proyecto generado:
The path in you want save your generate project:

```bash
cookiecutter https://github.com/luisandresmp/template_ds
```


## Estructura de directorios y archivos resultantes

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        ├── main
        │   ├── main.py        <- The final, canonical data sets for modeling.
        │   └── log.txt            <- The original, immutable data dump.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
Projects replied and adapted of [Course](https://github.com/platzi/curso-entorno-avanzado-ds) de [Platzi](https://platzi.com/) por [@jvelezmagic](https://twitter.com/jvelezmagic).
