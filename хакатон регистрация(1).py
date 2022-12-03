import pandas as pd
import numpy as np



#Логин и пароль управляющего
logA =("12345")
passA = ("55555")
#---------------------------------------------#

#Логин и пароль министерства
logM = ("55555")
passM = ("12345")
#---------------------------------------------#

#Создаем таблицу
df2 = pd.DataFrame(
#        [['12345','55555'], 
#    ['54321','55555']],
        [["-----", "-----"]],
    #Название столбцов
        columns = ['Login','Password'])
#---------------------------------------------#


vib = input ("Выберите Вход, Регистрация, Admin(v/r/a): ")


#Переадресация
if vib == ('a'):
    
    logV = input ("Введите логин: ")
    passV = input ("Введите пароль: ")


#Проверка админок
#------------------------------------------# 
    
    if logV == logA:
        if passV == passA:
            print ("Hello Admin")
            
        else:
        
            print("Ошибка при вводе")
#------------------------------------------#        
    
    elif logV == logM:
        if passV == passM:
            print ("Hello Min")    
             
        else:
        
            print("Ошибка при вводе")
#------------------------------------------#     
    else:
        
            print("Ошибка при вводе")
#------------------------------------------#


            

#Создание и заполнение таблицы для пользовательских логинов и паролей

elif vib == ('r'):

#----------------------------------------------------#
    #df2 = pd.DataFrame(
#        [['12345','55555'], 
#    ['54321','55555']],
        #[["-----", "-----"]],
    #Название столбцов
        #columns = ['Login','Password'])
    print ("ok")
    print(df2.head())
        
    test = (1)

    while test == (1):
        logR = input ("Введите логин: ")
        passR = input ("Введите пароль: ")
        new_row ={'Login': logR,'Password': passR}
        
        df2 = df2.append(new_row, ignore_index=True)

        print(df2.head())
#----------------------------------------------------#
    

        df2.to_csv('submission.csv') #сохранение файла
        
        test1 = input ("Новый пользователь-1, Войти-2, Назад-3: ")
        
        print (test1)
        
        if test1 == ('1') :
            continue

#Если вход
#----------------------------------------------------#
        elif test1 == ('2'):
            logL = input ("Введите логин: ")
            passL = input ("Введите пароль: ")
            
            sravL = ('Login' == logL)
            sravP = ('Password' == passL)

            print (sravL)
            print (sravP)
            
            if sravL == True:
                
                if sravP == True:
                    
                    print ("hi", logL)
                    continue
                
                else:
            #print(df2.head())
            #exit()
                    print ("Неверный логин или пароль")
                    ex = input ("Назад-1: ")
                    if ex == ('1'):
                        break
            
#----------------------------------------------------#
        
    
        
    
elif vib == ('v'):

    for j in logR:
        if j in 'Login':

                    
            for i in passR:
                if i in 'Password':
                            
                    print("True")
                    print ("hi", logR)
            #print(df2.head())
            #exit()
                    ex = input ("Назад-1: ")
                    if ex == ('1'):
                        break
    
    #print ("hi")
    #print(df2.head())



df2.to_csv('submission.csv') #сохранение файла


        
    #logR = input ("Введите логин: ")
    #passR = input ("Введите пароль: ")
        

    #df2 = pd.DataFrame(
#        [['12345','55555'], 
#    ['54321','55555']],
        #[["-----", "-----"]],
    #Название столбцов
        #columns = ['Логин','Пароль'])
        
    #new_row = {'Логин': logR,'Пароль': passR}
    #df2 = df2.append(new_row, ignore_index=True)


