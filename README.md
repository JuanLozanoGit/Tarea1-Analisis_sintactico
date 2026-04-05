# Tarea1-Analisis_sintactico

Implementación de un analizador sintáctico para la gramática de expresiones simples definida en clase. El programa transforma cadenas de entrada en representaciones gráficas de Árboles de Sintaxis Abstracta (AST).

## Requisitos
- Python 3.x
- Graphviz (binarios del sistema)
- Librerías: `pip install -r requirements.txt`

## Uso
Ejecutar el script pasando la expresión entre comillas:
`python analizador.py "2 + 3 * 4"`

Si se ejecuta sin argumentos, procesará automáticamente las cadenas de ejemplo de la guía.

## Notas Técnicas
Se utiliza el parser Earley de la librería Lark para resolver la recursividad por la izquierda. Las reglas con prefijo '?' eliminan nodos de derivación simple para producir un AST limpio.
