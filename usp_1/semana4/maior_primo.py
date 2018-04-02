def maior_primo(num):
        if num < 2:
            return False
        else:
            for n in range(2, num):
                while num % n == 0:
                    return num - 1
            return num

