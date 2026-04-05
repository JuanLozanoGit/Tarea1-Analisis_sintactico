import sys
from lark import Lark, tree

# Gramática fiel a la diapositiva del curso
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

def generar_ast(cadena, salida="ast_resultado"):
    parser = Lark(grammar, start='start', parser='earley')
    try:
        # Pre-procesamiento para manejar los tokens pari/pard si se usan paréntesis
        cadena_proc = cadena.replace("(", "pari").replace(")", "pard")
        arbol = parser.parse(cadena_proc)
        tree.pydot__tree_to_png(arbol, f"{salida}.png")
        print(f"Archivo {salida}.png generado.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        generar_ast(sys.argv[1])
    else:
        # Pruebas por defecto de la diapositiva
        pruebas = ["2+3*4", "2+3-4", "2+3*(4-5)"]
        for i, c in enumerate(pruebas):
            generar_ast(c, f"resultado_{i+1}")
