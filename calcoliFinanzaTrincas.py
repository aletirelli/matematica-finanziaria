#!/usr/bin/env python
# coding: utf-8

# # FIXED COMPOUNDING
# ## annualizzazione di pagamenti singoli
# 
# dato patrimonio attuale, calolo cifra da restituire

# In[2]:


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


# data cifra da restitire, calcolo patrimonio attuale

# In[ ]:


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


# # DISCRETE COMPOUNDING
# annualizzazione di flusso di cassa annuale

# In[ ]:


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
    
discrete_compounding_capitalRecovery()


# In[ ]:


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


# In[ ]:


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


# # CALCOLO INFLAZIONE

# In[ ]:


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

