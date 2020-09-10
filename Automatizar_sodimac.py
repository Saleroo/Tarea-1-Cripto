import sys
import time
import pyautogui
import string
import random
from selenium import webdriver
#prueba base64 : /+=n0TePeRdoN0+/
#prueba ASCII :C0nTr@seÑ4
#prueba ASCII extendido: C0nTr@seÑ4¶▲↓█§÷¹±Û┘¨┼‗Û®J{■
#prueba UTF-8 : ŴŵŶŷŸŹźŻżŽƓƔƕƖƗƘƙƚƛƜ
#prueba emoji : 😀 😃 😄 😁 😆 😅 😂 🤣 😇 😉


Usarname = 'Salero'
Password =  'C0nTr@seÑ4'
NewPass = 'NeWC0nTr@seÑ4'
Mail = 'mfranciscoeg@hotmail.com'
Nombre = 'Milenko'
Apellido1 = 'Espinoza'
Apellido2 = 'Guajardo'
Rut = '19.638.767-6'
Telefono = '957321093'


def spawn_browser(n):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    if n==2:
        driver.get("https://www.sodimac.cl/sodimac-cl/myaccount/login?successUrl=/myaccount")
    
    elif n==3 :
        driver.get("https://www.sodimac.cl/sodimac-cl/myaccount/forgotpassword?isPersonal=true")

    elif n==4 :
        driver.get("https://www.sodimac.cl/sodimac-cl/myaccount/login?successUrl=/myaccount")
    elif n==5 :
        driver.get("https://www.sodimac.cl/sodimac-cl/myaccount/login?successUrl=/myaccount")

    time.sleep(5)
    return driver

def Registrarse():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.sodimac.cl/sodimac-cl/myaccount/register/personal')

    correo_input = driver.find_element_by_id('testId-email')
    correo_input.send_keys(Mail)

    Pass_input = driver.find_element_by_id('testId-password')
    Pass_input.send_keys(Password)

    Nombre_input = driver.find_element_by_id('testId-firstName')
    Nombre_input.send_keys(Nombre)

    Apellido1_input = driver.find_element_by_id('testId-lastName')
    Apellido1_input.send_keys(Apellido1)

    Apellido2_input = driver.find_element_by_id('testId-middleName')
    Apellido2_input.send_keys(Apellido2)

    dia_button = driver.find_element_by_id('testId-Dropdown-testId-date-value')
    dia_button.click()

    Dia_button = driver.find_element_by_id('testId-li-testId-DropdownList-testId-Dropdown-testId-date-dropdown-list-item-16')
    Dia_button.click()

    mes_button = driver.find_element_by_id('testId-Dropdown-testId-month-value')
    mes_button.click()

    Mes_button = driver.find_element_by_id('testId-li-testId-DropdownList-testId-Dropdown-testId-month-dropdown-list-item-5')
    Mes_button.click()    

    año_button = driver.find_element_by_id('testId-Dropdown-testId-year-value')
    año_button.click()
 
    Año_button = driver.find_element_by_id('testId-li-testId-DropdownList-testId-Dropdown-testId-year-dropdown-list-item-90')
    Año_button.click()

    Rut_input = driver.find_element_by_id('testId-document')
    Rut_input.send_keys(Rut)

    Telefono_input = driver.find_element_by_id('testId-input-phoneNumber')
    Telefono_input.send_keys(Telefono)

    Terminos_button = driver.find_element_by_id('checkbox-testId-acceptTermsAndConditions')
    Terminos_button.click()

    Registrarse_button = driver.find_element_by_id('testId-btn-registration-submit')
    Registrarse_button.click()



def Iniciar_Sesion(n):

    driver = spawn_browser(n)

    user_input = driver.find_element_by_id('inputEmail')
    user_input.send_keys(Mail)

    password_input = driver.find_element_by_id('loginPassword')
    password_input.send_keys(Password)
    time.sleep(2)
    pyautogui.press("enter")


#driver.find_element_by_xpath('loginSubmit').click()

def Restablecer_Contraseña(n):

    driver = spawn_browser(n)
    time.sleep(2)
    mail_recuperar = driver.find_element_by_id('forgotPassword_Email')
    mail_recuperar.send_keys(Mail)

    time.sleep(6)

    pyautogui.press("enter")

def Modificar_Contraseña(n):

    driver = spawn_browser(n)

    user_input = driver.find_element_by_id('inputEmail')
    user_input.send_keys(Mail)

    password_input = driver.find_element_by_id('loginPassword')
    password_input.send_keys(Password)
    time.sleep(2)
    pyautogui.press("enter")

    time.sleep(2)

    CambiarPASS_button = driver.find_element_by_id('testId-link-updatePasswordLink')
    CambiarPASS_button.click()

    time.sleep(2)

    Pass_input = driver.find_element_by_id('testId-currentPassword')
    Pass_input.send_keys(Password)

    NewPass_input = driver.find_element_by_id('testId-newPassword')
    NewPass_input.send_keys(NewPass)

    time.sleep(2)
    
    button_CambiarPass = driver.find_element_by_id('testId-btn-update-password-button')
    button_CambiarPass.click()

def  Fuerza_Bruta(n):
    contador=0
    driver = spawn_browser(n)
    while True:
        time.sleep(3)
        lst = [random.choice(string.ascii_letters + string.digits) for n in range(12)]
        trypass= "".join(lst)


        user_input = driver.find_element_by_id('inputEmail')
        user_input.send_keys(Mail)
        
        password_input = driver.find_element_by_id('loginPassword')
        password_input.send_keys(trypass)

        time.sleep(2)
        pyautogui.press("enter")

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
        Iniciar_Sesion(n)

    elif n==3:
        Restablecer_Contraseña(n)

    elif n==4:
        Modificar_Contraseña(n)
    
    elif n==5:
        Fuerza_Bruta(n)

    elif n==6:
        break

    else:
        print("Opcion invalida")


    
