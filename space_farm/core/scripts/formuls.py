from math import sin, pi

#1 единица топлива стоит 10 кредитов, одна единица кислорода стоит 7 кредитов


def V(W, Sh, Oxi, T):   #Максимальная скорость, Мощность, Масса
    try:
        return 2*(W/80)*(200/(192+Sh+Sh*sin(-(pi/2)+(pi*(T+0.5*(Oxi/Sh)))/(40))))
    except:
        return 2


def SHnew(G0, T, Oxi): #новое значение Sh
    try:
        return G0 + G0*sin(-(pi/2)+(pi*(T+0.5*(Oxi/G0)))/(40))
    except:
        return 30


def E(T):
    sum = 0
    for i in range(0, T):
        sum += i
    return sum
