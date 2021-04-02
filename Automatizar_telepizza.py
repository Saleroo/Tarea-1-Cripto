import sys
import time
import pyautogui
import string
import random
from selenium import webdriver

#prueba base64 : +=n0TePeRdoN0+/
#prueba ASCII :C0nTr@seÑ4
#prueba ASCII extendido: ¶▲↓█§÷¹±Û¨┼Û®J■
#prueba UTF-8 : ŵŸŹŽƓƔƕƖƗƘƙƚƛƜ, ѼѽѾѿҀҁ҂҃҄҅҆҇҈҉Ҋ , ݧݨݩݪݫݬݭݮݯݰݱݲݳ
#prueba emoji :   🤲 🙌 👏 🙏 , 😀 😃 😄 😁 , 👯‍♀️ 👯 👯‍♂️



Password =  'C0nTr@seÑ4'
NewPass = 'NeWC0nTr@seÑ4'
Mail = 'milenkoeg@hotmail.com'
Nombre = 'Milenko'
Apellido = 'Espinoza'
Rut = '19.638.767-6'
Telefono = '957321093'
dia ='16'
mes ='05'
año ='1998'



def spawn_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.telepizza.es/')



    time.sleep(5)
    return driver

def Registrarse():

    driver = spawn_browser()
    time.sleep(2)

    pyautogui.moveTo(1559, 132)
    pyautogui.click()


    time.sleep(2)


    mail_input = driver.find_element_by_id('Email')
    mail_input.send_keys(Mail)

    password_input = driver.find_element_by_id('Password')
    password_input.send_keys(Password)

    passwordR_input = driver.find_element_by_id('ConfirmPassword')
    passwordR_input.send_keys(Password)

    telefono_input = driver.find_element_by_id('FirstPhone')
    telefono_input.send_keys(Telefono)

    time.sleep(2)
    pyautogui.moveTo(995, 749)
    pyautogui.click()

    time.sleep(2)

    pyautogui.moveTo(1093, 855)
    pyautogui.click()




def Iniciar_Sesion():

    driver = spawn_browser()

    time.sleep(2)

    pyautogui.moveTo(1559, 132)
    pyautogui.click()
    
    time.sleep(2)

    
    user_input = driver.find_element_by_id('EmailLogin')
    user_input.send_keys(Mail)

    pyautogui.moveTo(1007, 494)
    pyautogui.click()

    password_input = driver.find_element_by_name('PasswordLogin')
    password_input.send_keys(Password)

    time.sleep(2)

    button_iniciar_sesion = driver.find_element_by_id('divLoginSubmit')
    button_iniciar_sesion.click()


#driver.find_element_by_xpath('loginSubmit').click()

def Restablecer_Contraseña():

    driver = spawn_browser()
    time.sleep(2)

    pyautogui.moveTo(1164, 532)
    pyautogui.click()


    mail_recuperar = driver.find_element_by_id('ForgottenPasswordEmail')
    mail_recuperar.send_keys(Mail)

    time.sleep(2)

    pyautogui.moveTo(524, 498)
    pyautogui.click()

def Modificar_Contraseña():

    driver = spawn_browser()

    time.sleep(2)

    pyautogui.moveTo(1559, 132)
    pyautogui.click()
    
    time.sleep(2)

    
    user_input = driver.find_element_by_id('EmailLogin')
    user_input.send_keys(Mail)

    pyautogui.moveTo(1007, 494)
    pyautogui.click()

    password_input = driver.find_element_by_name('PasswordLogin')
    password_input.send_keys(Password)

    time.sleep(2)

    button_iniciar_sesion = driver.find_element_by_id('divLoginSubmit')
    button_iniciar_sesion.click()

    time.sleep(2)

    pyautogui.moveTo(1008, 519)
    pyautogui.click()

    time.sleep(2)

    pass_inut = driver.find_element_by_id('user_new_password')
    pass_inut.send_keys(Password)

    Newpass_input = driver.find_element_by_id('user_confirm_password')
    Newpass_input.send_keys(Password)

    button_guardar = driver.find_element_by_id('submitPersonalData')
    button_guardar.click()

    time.sleep(2)

    confirmar_input = driver.find_element_by_id('passConfirmPopup')
    confirmar_input.send_keys(NewPass)

    pyautogui.moveTo(917, 571)
    pyautogui.click()

def  Fuerza_Bruta():
    contador=0
    driver = spawn_browser()

    time.sleep(3)

    pyautogui.moveTo(1559, 132)
    pyautogui.click()

    while True:
        time.sleep(3)
        lst = [random.choice(string.ascii_letters + string.digits) for n in range(12)]
        trypass= "".join(lst)

        user_input = driver.find_element_by_id('EmailLogin')
        user_input.send_keys(Mail)

        pyautogui.moveTo(1007, 494)
        pyautogui.click()

        password_input = driver.find_element_by_name('PasswordLogin')
        password_input.send_keys(trypass)

        time.sleep(2)

        button_iniciar_sesion = driver.find_element_by_id('divLoginSubmit')
        button_iniciar_sesion.click()
        
        contador = contador + 1
        print("inteto : ", contador )




    








while True:
    print("-----------------------------------------")
    print("(1) Registrarse ")
    print("(2) Iniciar Sesion")
    print("(3) Restablecer Contraseña")
    print("(4) Modificar Contraseña")
    print("(5) Fuerza Bruta")
    print("(6) Salir")
    n = int(input("ingrese la opcion que desea:  "))
    
    if n==1:
        Registrarse()

    elif n==2:
        Iniciar_Sesion()

    elif n==3:
        Restablecer_Contraseña()

    elif n==4:
        Modificar_Contraseña()
    
    elif n==5:
        Fuerza_Bruta()

    elif n==6:
        break

    else:
        print("Opcion invalida")


    
