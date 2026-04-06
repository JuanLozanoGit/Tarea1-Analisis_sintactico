# Tarea 1: Analizador Sintáctico y Generación de AST

Este proyecto implementa un analizador sintáctico basado en la gramática de expresiones aritméticas vista en clase. Utiliza el motor de parsing Earley para transformar expresiones en Árboles de Sintaxis Abstracta (AST) visuales.

## 🛠️ Requisitos del Sistema

Antes de correr el programa, asegúrate de tener instalado:

1.  **Python 3.10+**
2.  **Graphviz** (Motor de dibujo del sistema):
    * En Linux (Kali/Ubuntu): `sudo apt update && sudo apt install graphviz -y`
    * En Windows: Descargar e instalar desde [graphviz.org](https://graphviz.org/download/) (Marcar "Add to PATH").

## 📦 Instalación de Librerías

Si estás en Kali Linux o un entorno gestionado, usa el flag `--break-system-packages`:

```bash
pip install lark pydot --break-system-packages
```

## 🚀 Guía de Uso Rápido

1.  **Preparar las pruebas:**
    Edita el archivo `pruebas.txt` y coloca una expresión por línea. Ejemplo:
    ```text
    2+3*4
    (a+b)*c
    ```

2.  **Ejecutar el analizador:**
    Desde la terminal, dentro de la carpeta del proyecto, ejecuta:
    ```bash
    python analizador.py pruebas.txt
    ```

3.  **Ver los resultados:**
    El programa generará automáticamente archivos `.png` numerados en la raíz de la carpeta:
    * `ast_linea_1.png`
    * `ast_linea_2.png`
    ...etc.

## ⚙️ Notas de Implementación

* **Gramática:** Se implementaron los tokens `pari` (paréntesis izquierdo) y `pard` (paréntesis derecho) según las diapositivas del curso para manejar la agrupación.
* **AST:** El árbol generado es un "Abstract Syntax Tree". Esto significa que Lark elimina nodos redundantes y solo muestra la estructura lógica de la operación.
* **Precedencia:** La gramática está estructurada para que la multiplicación (`*`) y división (`/`) tengan mayor jerarquía que la suma (`+`) y resta (`-`).

---
Desarrollado para la asignatura de Compiladores - Universidad Sergio Arboleda.
```
