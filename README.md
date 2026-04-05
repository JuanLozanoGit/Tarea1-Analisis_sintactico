# Tarea1-Analisis_sintactico

## Introducción
Este proyecto implementa un analizador sintáctico basado en la gramática de expresiones simples definida en clase. El objetivo es procesar cadenas de entrada y representar su jerarquía mediante un AST, diferenciándolo de un árbol de análisis sintáctico estándar al simplificar nodos redundantes.

## Especificación de la Gramática
La gramática implementada sigue las reglas de precedencia estándar:
* **E**: Expresiones de suma y resta (Menor precedencia).
* **T**: Términos de multiplicación y división.
* **F**: Factores (Identificadores, números o expresiones agrupadas).

## Requisitos Técnicos
Para ejecutar el generador, se requiere Python 3.x y las siguientes dependencias:
```bash
pip install lark pydot
