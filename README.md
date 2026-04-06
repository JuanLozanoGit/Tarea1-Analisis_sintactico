# Tarea 1: Analizador Sintáctico y Generación de AST

## Requisitos del Sistema:

1.  **Python 3.1**
2.  **Graphviz** (Motor de dibujo del sistema):
    * En Linux: `sudo apt update && sudo apt install graphviz -y`

## Instalación de Librerías:

Si estás en Kali Linux o un entorno gestionado, usa el flag `--break-system-packages`:

```bash
pip install lark pydot --break-system-packages
```

## Guía de Uso Rápido:

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

## Notas de Implementación:

* **Gramática:** Se implementaron los tokens `pari` (paréntesis izquierdo) y `pard` (paréntesis derecho) según las diapositivas del curso para manejar la agrupación.
* **AST:** El árbol generado es un "Abstract Syntax Tree". Esto significa que Lark elimina nodos redundantes y solo muestra la estructura lógica de la operación.
* **Precedencia:** La gramática está estructurada para que la multiplicación (`*`) y división (`/`) tengan mayor jerarquía que la suma (`+`) y resta (`-`).

---
