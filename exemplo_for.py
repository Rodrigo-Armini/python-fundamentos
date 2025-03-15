import time

def exemplo_apresentar_contagem_regressiva():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1) # delay 1

def exemplo_relogio():
    #
    for hora in rang(0, 24):
        for minuto in range(0, 60):
            for segundo in range(0, 60):
                print(hora, minuto, segundo, sep=":")
                time.sleep(1)

if __name__ == "__main__":
    import os
    os.system("cls")
    exemplo_relogio()