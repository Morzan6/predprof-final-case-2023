from math import sin, pi

#1 единица топлива стоит 10 кредитов, одна единица кислорода стоит 7 кредитов


def V(W, Sh):   #Максимальная скорость, Мощность, Масса
    return 2*(W/80)*(200/(192+Sh))


def SHnew(G0, Kp): #новое значение Sh
    return G0 + G0*Kp



def Kp(Oxi, T):
    #Oxi <= 60!!
    return sin(-(pi/2)+(pi*(T+0.5*Oxi))/(40))


def E(T):
    sum = 0
    for i in range(0, T):
        sum += i
    return sum