from math import sqrt, pow, pi

def _gamma(x):
    if x == 1:
        return 1
    if x == 0.5:
        return sqrt(pi)
    return (x - 1) * _gamma(x - 1)

def _dist_t(x, dof):
    numerator = _gamma((dof + 1) / 2)
    denominator = sqrt(dof * pi) * _gamma(dof / 2)
    factor = pow(1 + pow(x, 2) / dof, -(dof + 1) / 2)
    return numerator / denominator * factor

def _sum_simp(x, dof, ns, even, f=_dist_t):
    w = x / ns
    
    if even:
        ran = range(2, ns - 1, 2)
        factor = 2
    else:
        ran = range(1, ns, 2)
        factor = 4

    return sum(factor * f(x * w, dof) for x in ran)

def _simp_rule(x, dof, ns, f=_dist_t):
    w = x / ns

    sums = f(0, dof)
    sums += _sum_simp(x, dof, ns, False, f)
    sums += _sum_simp(x, dof, ns, True, f)
    sums += f(x, dof)

    return (w / 3) * sums

def simpsons_rule(x, dof):
    error = 0.00001
    ns = 4
    result1 = _simp_rule(x, dof, ns)
    ns *= 2 
    result2 = _simp_rule(x, dof, ns)

    while error < result2 - result1:
        result1 = _simp_rule(x, dof, ns)
        ns *= 2
        result2 = _simp_rule(x, dof, ns)

    return result2
