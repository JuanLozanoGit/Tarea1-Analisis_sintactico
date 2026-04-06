import sys
import os
from lark import Lark, tree

grammar = """
    ?start: e

    ?e: t
      | e opsuma t    -> suma

    ?t: f
      | t opmul f     -> multiplicacion

    ?f: id
      | num
      | "pari" e "pard"

    opsuma: "+" | "-"
    opmul: "*" | "/"
    id: /[a-zA-Z_][a-zA-Z0-9_]*/
    num: /\d+/

    %import common.WS
    %ignore WS
"""

def procesar_archivo(ruta_txt):
    if not os.path.exists(ruta_txt):
        print(f"Error: No se encuentra el archivo {ruta_txt}")
        return

    parser = Lark(grammar, start='start', parser='earley')
    
    with open(ruta_txt, 'r') as f:
        lineas = f.readlines()

    for i, linea in enumerate(lineas):
        cadena = linea.strip()
        if not cadena:
            continue
            
        try:
            # Reemplazo de parentesis por tokens de la gramatica
            proc = cadena.replace("(", "pari").replace(")", "pard")
            arbol = parser.parse(proc)
            
            nombre_salida = f"ast_linea_{i+1}.png"
            tree.pydot__tree_to_png(arbol, nombre_salida)
            print(f"Linea {i+1} OK: {cadena} -> {nombre_salida}")
        except Exception as e:
            print(f"Error en linea {i+1} ({cadena}): {e}")

if __name__ == "__main__":
    # Lineas de codigo para aceptar archivos
    archivo = sys.argv[1] if len(sys.argv) > 1 else "pruebas.txt"
    procesar_archivo(archivo)
