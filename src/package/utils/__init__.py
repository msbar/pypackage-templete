def chunk_list(lst, chunksize):
    """
    Gerador de chunks de uma lista.
    Yield sucessivos chunks de tamanho chunksize de lst.

    Args:
        lst: Lista a ser dividida em chunks.
    """
    for i in range(0, len(lst), chunksize):
        yield lst[i : i + chunksize]
