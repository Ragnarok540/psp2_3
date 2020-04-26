import sys
from dist_t import simpsons_rule

def main(x, dof):
    try:
        print(f"El valor de p es: {simpsons_rule(float(x), float(dof))}")
    except ValueError:
        print("ERROR: Todos los parámetros deben ser números reales o enteros.")
        sys.exit()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
