import sys
from lark import Lark, tree

# Gramática basada exactamente en la diapositiva de clase
grammar = """
    ?start: e

    ?e: t
      | e opsuma t    -> suma

    ?t: f
      | t opmul f     -> multiplicacion

    ?f: ID            -> id
      | NUMBER        -> num
      | "pari" e "pard"

    opsuma: "+" | "-"
    opmul: "*" | "/"
    
    ID: /[a-zA-Z_][a-zA-Z0-9_]*/
    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

class CompiladorAST:
    def __init__(self):
        self.parser = Lark(grammar, start='start')

    def generar_imagen(self, texto, nombre_archivo="ast_resultado"):
        try:
            # Reemplazo simple para simular los tokens de la diapositiva si se desea
            # o se puede usar la cadena directa si se ajusta la gramática
            arbol = self.parser.parse(texto)
            tree.pydot__tree_to_png(arbol, f"{nombre_archivo}.png")
            print(f"AST generado correctamente en: {nombre_archivo}.png")
        except Exception as e:
            print(f"Error de sintaxis: {e}")

if __name__ == "__main__":
    # Ejemplo de uso con una de las cadenas de la diapositiva
    # Nota: Si usas ( o ), cámbialos por pari o pard según pida el profe
    # o mantén los símbolos si el parser los reconoce.
    test_input = "2 + 3 * 4" 
    
    compilador = CompiladorAST()
    compilador.generar_imagen(test_input)
