# -*- coding: utf-8 -*-
import numpy as np
P = 0 #patrimonio a t=0
A = 0 #conto economico di un anno
i = 0 #interessi o tasso di ammortamento annuale /100
f = 0 #tasso di inflazione /100
i_f = i + f + i*f #market interest rate
r = 0 #discount rate per annum /100
t = 0 #tassazione /100
N = 10 #durata in anni dell'investimento
G = 0 #uniform gradient amount (????)



#FIXED COMPOUNDING - annualizzazione di pagamenti singoli
#dato patrimonio attuale, calolo cifra da restituire
def fixed_compounding_future():
    P=input('Patrimonio attuale: ')
    P=int(P)
    N=input("Anni di durata dell'investimento: ")
    N=int(N)
    i_perc=input('Tasso di interesse in percentuale: ')
    i_perc=int(i_perc)
    i=i_perc/100
    Fs = int(P*(1+N*i)) #patrimonio futuro - interesse semplice
    Fc = int(P*(1+i)**N) #patrimonio futuro - interesse composto
    CA = float((1+i)**N) #single payment compound factor
    Ic = int(P*CA-P) #interesse totale sul prestito
    CA_Print=CA*10
    print('Patrimonio futuro con interesse semplice: ',Fs)
    print('Patrimonio futuro con interesse composto: ',Fc)
    print('Tasso di interesse composto: ',CA_Print,'%')
    print('Interesse totale sul prestito: ',Ic)
    
#data cifra da restitire, calcolo patrimonio attuale
def fixed_compounding_present():
    N=input("Anni di durata dell'investimento")
    N=int(N)
    i_perc=input('Tasso di interesse')
    i_perc=int(i_perc)
    i=i_perc/100
    FW=input('Somma da ottenere in futuro')
    PW = 1/(1+i)**N #single present worth factor
    PW_Print=PW*10
    Pc= int(FW*PW) #somma attualizzata
    print('Tasso di interesse composto: ',PW_Print,'%')
    print('Somma attualizzata: ',Pc)

#DISCRETE COMPOUNDING - annualizzazione di flusso di cassa annuale
def discrete_compounding_capitalRecovery():
    P=input('Patrimonio attuale: ')
    P=int(P)
    N=input("Anni di durata dell'investimento: ")
    N=int(N)
    i_perc=input('Tasso di interesse in percentuale: ')
    i_perc=int(i_perc)
    i=i_perc/100
    CRF = (i*(1+i)**N)/((1+i)**N-1) #capital recovery factor - guadagni annuali 
    #costanti per ripagare P
    CRF_Print=CRF*10
    A = int(CRF*P)
    print('Capital recovery factor: ',CRF_Print,'%')
    print('Entrate annuali necessarie: ', A)

def discrete_compounding_presentWorth():
    A=input('Conto economico di un anno: ')
    A=int(A)
    N=input("Anni di durata dell'investimento: ")
    N=int(N)
    i_perc=input('Tasso di interesse in percentuale: ')
    i_perc=int(i_perc)
    i=i_perc/100
    SPW = ((1+i)**N-1)/(i*(1+i)**N) #series present worth factor - dato rendimento 
    #annuale A trovo P che posso prendere in prestito
    P = int(A*SPW)
    print('Series present worth factor: ',SPW)
    print('Patrimonio iniziale disponibile: ', P)

def discrete_compounding_futureWorth():
    A=input('Conto economico di un anno: ')
    A=int(A)
    N=input("Anni di durata dell'investimento: ")
    N=int(N)
    i_perc=input('Tasso di interesse in percentuale: ')
    i_perc=int(i_perc)
    i=i_perc/100
    SCA = (1+i)**N/i #uniform series compound amount factor - dato rendimento 
    #annuale A trovo F da ripagare futuro
    SCA_Print=SCA*10
    F = int(A*SCA)
    print('Uniform series compound amount factor: ', SCA_Print)
    print('Patrimonio futuro ottenibile: ',F)

#CALCOLO INFLAZIONE
def inflazione():
    N=input("Anni: ")
    N=int(N)
    f_perc=input('Tasso di inflazione in percentuale: ')
    f_perc=int(f_perc)
    f=f_perc/100
    RN=input('Valore attuale: ')
    RN=int(RN)
    CN = RN*(1+f)**N #valore futuro
    CN=int(CN)
    print('Valore a ',N,' anni:',CN)

#tabella valore in dollari attuali vs dollari futuri
#
# . OK


D = 0 #tasso di ammortamento
GI = 0 #reddito lordo
OE = 0 #costi operativi
EBIT = GI-OE #utile operativo
EBITDA = EBIT-D #margine operativo lordo (guadagno tassabile)
TAXES = EBITDA*t #imposte sul reddito
NPAT = EBITDA-TAXES #utile al netto delle imposte
CRF = 0
CRF_1 = CRF*(1-t)+t/N #fattore di recupero del capitale al netto delle imposte

S = 0 #che cos'è????
A_2 = GI-OE-P+S #flusso di cassa al lordo delle imposte = A
A_1 = A_2-t*EBITDA #flusso di cassa al netto delle imposte = A'

#CASHFLOW MODELLING
H = 5 #durata in anni del prestito
Q = 8 #durata in anni dell'ammortamento
Ib = 0 #boh
# for i in range(0, N):
#     if i<H:
#         #durante il periodo del prestito 0<H
#         A_1(i) = A_2*(1-t)+t*Ib+t*P/Q
#     else if H<=i, i<Q:
#         #durante il periodo di ammortamento H-Q
#         A_1(i) = A_2*(1-t)+t*P/Q
#     else
#         #per il rimanente periodo di ammortamento
#         A_1(i) = A_2(1-t)
#bisogna inizializzare array con N valori
