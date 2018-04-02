def remove_repetidos(*args):
    sem_rep = []
    for i in args:
        if i not in sem_rep:
            sem_rep.append(i)
    return sorted(sem_rep)

#def p(*l):
#    new_list = []
#    for i in [*l]:
#        if i in [*l]:
#            new_list.append(i)
#    print(new_list)

#def fim(*num):
#    sem_repetidos = [*num]
#    sem = list(set(sem_repetidos))
#    print(sem)
