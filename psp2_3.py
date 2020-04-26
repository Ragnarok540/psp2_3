import sys
from dist_t import simpsons_rule

def main(x, dof):
    try:
        print(f"El valor de p es: {simpsons_rule(float(x), float(dof))}")
    except ValueError:
        print("ERROR: Todos los parámetros deben ser números reales o enteros.")
        sys.exit()
    except RecursionError:
        print("ERROR: El valor de grados de libertad debe ser entero positivo y mayor a cero.")
        sys.exit()


if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print("""ERROR: Se requiere el valor de x y los grados de libertad,
por ejemplo: '1.1 9'.""")
        sys.exit()
