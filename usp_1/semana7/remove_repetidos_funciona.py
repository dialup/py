def remove_repetidos(*remove):
    teste = [*remove]
    sem_repetidos = list(set(teste))
    return sorted(sem_repetidos)
