def convert_str_to_float(val):
    """
    Converte uma string para float.

    Args:
        val: Valor a ser convertido.
    """
    try:
        return float(val.replace(",", "."))
    except:
        return val
