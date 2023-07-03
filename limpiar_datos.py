import re


def normalizar_dato(dato):
    if re.search(r'\bDOM\w*IO\b', dato, re.IGNORECASE):
        return 'Dominio'
    elif re.search(r'\bMAR\w*A\b', dato, re.IGNORECASE):
        return 'Marca'
    elif re.search(r'\bMOD\w*O\b', dato, re.IGNORECASE):
        return 'Modelo'
    elif re.search(r'\bTIP\w*\b', dato, re.IGNORECASE):
        return 'Tipo'
    elif re.search(r'\bUS\w*\b', dato, re.IGNORECASE):
        return 'Uso'
    elif re.search(r'\bCHA\w*S\b', dato, re.IGNORECASE):
        return 'Chasis'
    elif re.search(r'\bMOT\w*R\b', dato, re.IGNORECASE):
        return 'Motor'
    elif re.search(r'\bPREC\w*TOM\w*\b', dato, re.IGNORECASE):
        return 'Precio Toma'
    elif re.search(r'\bOBS\w*\b', dato, re.IGNORECASE):
        return 'Observaciones'
    else:
        return dato
