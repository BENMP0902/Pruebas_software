# Analizador de Texto

Proyecto básico desarrollado para la materia de **Software Libre**.

El programa permite analizar un texto y obtener información como:

- Número de palabras.
- Número de caracteres.
- Número de oraciones.
- Número de párrafos.

## Tecnologías utilizadas

- Python 3
- `venv` para crear un entorno virtual
- `unittest` para realizar pruebas

## Estructura del proyecto

```text
Pruebas_software/
│
├── .venv/                 # Entorno virtual
├── test_analyzer.py        # Pruebas del analizador
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias del proyecto
└── requirements_dev.txt    # Dependencias de desarrollo
```

## Crear y activar el entorno virtual

Crear el entorno:

```powershell
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución, usa temporalmente:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Después, vuelve a activar el entorno.

## Instalar dependencias

Actualmente el proyecto no utiliza librerías externas, por lo que `requirements.txt` puede permanecer vacío.

Si en el futuro agregas dependencias, instálalas con:

```powershell
pip install -r requirements.txt
```

## Ejecutar las pruebas

Las pruebas estan escritas como funciones simples con `assert` y se
ejecutan directamente como script (no usan `unittest.TestCase`):

```powershell
python test_analyzer.py
```

## Autor

Proyecto realizado para la materia de Software Libre.
