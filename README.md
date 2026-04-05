# Tarea1-Analisis_sintactico

Analizador sintáctico para gramáticas de expresiones simples. Procesa múltiples cadenas desde un archivo de texto y genera los AST correspondientes en formato imagen.

## Requisitos
- Python 3.x
- Graphviz
- Librerías: `pip install lark pydot`

## Uso
1. Colocar las expresiones en `pruebas.txt` (una por línea).
2. Ejecutar:
   `python analizador.py`

También permite especificar un archivo distinto:
`python analizador.py mis_cadenas.txt`

## Funcionamiento
El script lee cada línea, reemplaza paréntesis por tokens `pari`/`pard` y utiliza el motor Earley de Lark para generar una estructura jerárquica libre de nodos redundantes (AST).
