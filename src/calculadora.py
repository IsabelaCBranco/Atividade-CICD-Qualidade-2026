def juros_compostos(principal, taxa, periodos):
    if principal < 0:
        raise ValueError("principal nao pode ser negativo")
    if periodos < 0:
        raise ValueError("periodos nao pode ser negativo")
    montante = principal * (1 + taxa) ** periodos
    return round(montante, 2)

def soma(a, b):
    return a + b