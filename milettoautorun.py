import pyautogui
import time

#Biblioteca de automacao para programas baseado em reconhecimento de imagem

#definindo classe com os dados do programa
class Programa:
    def __init__(self, endereco, imagem_aberto, precisa_login=0,email_login=None, senha=None, 
                 botao_login=None, botao_senha=None, login_aceito=None):
        self.__endereco = endereco #endereço do executável do programa
        self.__imagem_aberto = imagem_aberto #imagem do programa
        self.__precisa_login = precisa_login #se precisar de login = 0, se nao 1
        self.__email_login = email_login #email de login
        self.__senha = senha #senha de login
        self.__botao_login = botao_login #imagem do botao de login
        self.__botao_senha = botao_senha #imagem do botao para digitar senha
        self.__login_aceito = login_aceito #imagem confirmando que conseguiu logar

    def get_endereco(self):
        return self.__endereco

    def get_imagem_aberto(self):
        return self.__imagem_aberto

    def get_precisa_login(self):
        return self.__precisa_login

    def get_email_login(self):
        return self.__email_login

    def get_senha(self):
        return self.__senha

    def get_botao_login(self):
        return self.__botao_login

    def get_botao_senha(self):
        return self.__botao_senha

    def get_login_aceito(self):
        return self.__login_aceito

#clica na barra superior da janela, para selecionar a mesma.
def clica_janela():
    pyautogui.moveTo(849, 15, duration=0.1)
    pyautogui.click()
    pyautogui.press("enter")

#Abre o programa referido, click define se tera o click na janela ou não, após abrir o programa
def abre_programa(ponteiro, click=0):
    endereco = ponteiro.get_endereco()
    pyautogui.hotkey("win", "d")
    pyautogui.press("win")
    time.sleep(.5)
    pyautogui.write(endereco)
    time.sleep(.5)
    pyautogui.press("enter")
    time.sleep(5)
    img_prog_aberto = ponteiro.get_imagem_aberto()
    if click == 1:
        clica_janela()
    if programa_aberto(img_prog_aberto):
        print("consegui abrir o programa!")
        return True
    else:
        print("programa não abriu!")
        return False

#Checa se o programa ja abriu, chamando a função de procurar pelo programa
def programa_aberto(img_login_real):
    #login_real = pyautogui.locateOnScreen(img_login_real, confidence=0.8)
    login_real = procura_programa(img_login_real, 7, 1)
    if login_real:
        print("imagem {} encontrada!".format(img_login_real))
        return True
    else:
        print("imagem {} não encontrada".format(img_login_real))
        return False

#Procura o programa entre as janelas abertas, vai dando alt+tab até achar o programa
def procura_programa(imagem, tentativas, delay):
    i=0
    while i <= tentativas:
        img = procura_imagem(imagem)
        if img:
            return img
        else:
            pyautogui.keyDown("alt")
            time.sleep(.2)
            pyautogui.press("tab")
            time.sleep(.2)
            pyautogui.press("tab")
            time.sleep(.2)
            pyautogui.keyUp("alt")
            i+=1
            time.sleep(delay)
    print("numero maximo de tentativas atingido")
    return None

#Verifica se determinada imagem está na tela
def procura_imagem(imagem, tentativas=5, delay=.5):
    i = 0
    while i <= tentativas:
        img = pyautogui.locateOnScreen(imagem, confidence=0.8)
        if img:
            return img
        time.sleep(delay)
    print("Imagem não encontrada. Número maximo de tentativas atingido")
    return None

#função para fazer login, clicando no botão de login.
def fazer_login(ponteiro, delay=3):
    botao_login = ponteiro.get_botao_login()
    if clica_botao(botao_login):
        login = ponteiro.get_email_login()
        pyautogui.write(login)
        botao_senha = ponteiro.get_botao_senha()
        if clica_botao(botao_senha):
            senha = ponteiro.get_senha()
            pyautogui.write(senha)
            pyautogui.press("enter")
            time.sleep(delay)
            login_real = ponteiro.get_login_aceito()
            if programa_aberto(login_real):
                print("login realizado")
                return True
            else:
                print("confirmação de login não realizada")
                return False
        else:
            print("Botao de senha não encontrado!")
            return False
    else:
        print("Botao de login não encontrado!")
        return False

#função que clica em determinado botão, através da imagem do mesmo.
def clica_botao(imagem_botao):
    posicao = procura_imagem(imagem_botao)
    if posicao:
        pyautogui.click(posicao)
        print("botao {} encontrado".format(imagem_botao))
        return True
    else:
        print("botao não encontrado!")
        return False

def obter_emaillogin(ponteiro):
    email = ponteiro.get_email_login()
    return email

def obter_senha(ponteiro):
    senha = ponteiro.get_senha()
    return senha

def executar():
    print("Script Ok")

if(__name__ == '__main__'):
    executar()