from selenium import webdriver
from selenium.webdriver.common.by import By

def genera_link_paypal(stringa_input):
    link_paypal = f"https://www.paypal.com/paypalme/{stringa_input}"
    return link_paypal

def estrai_informazioni_account(link_paypal):
    try:
        # Configura il driver di Selenium (assicurati di avere il webdriver del browser installato)
        driver = webdriver.Chrome()  # In questo esempio si utilizza Chrome, puoi modificare il driver a seconda del tuo browser

        # Vai al link PayPal.me
        driver.get(link_paypal)

        # Controlla la presenza del tag "img" con il link "https://www.paypalobjects.com/paypal-ui/illustrations/svg/warning.svg"
        elemento_warning_svg = driver.find_elements(By.XPATH, f'//img[@src="https://www.paypalobjects.com/paypal-ui/illustrations/svg/warning.svg"]')

        # Se l'elemento è presente, il link non è attivo
        if elemento_warning_svg:
            print("Il link non è attivo.")
            return None

        # Esempio di come potresti estrarre il nome utente utilizzando la classe CSS "css-12iywa9"
        nome_utente_element = driver.find_element(By.CLASS_NAME, 'css-12iywa9')
        nome_utente = nome_utente_element.text if nome_utente_element else "Informazione non disponibile"

        # Puoi estrarre ulteriori informazioni a seconda della struttura della pagina

        return {
            "Nome utente": nome_utente,
            # Aggiungi altre informazioni se necessario
        }
    except Exception as e:
        print(f"Errore durante l'estrazione delle informazioni: {str(e)}")
        return None
    finally:
        # Chiudi il driver di Selenium
        if driver:
            driver.quit()

# Esempio di utilizzo
input_stringa = input("Inserisci la tua stringa: ")

paypal_link_generato = genera_link_paypal(input_stringa)
print(f"Ecco il possibile link PayPal.me generato: {paypal_link_generato}")

# Verifica la validità del link e ottieni informazioni sull'account se il link è attivo
informazioni_account = estrai_informazioni_account(paypal_link_generato)
if informazioni_account:
    print("Informazioni sull'account:")
    for chiave, valore in informazioni_account.items():
        print(f"{chiave}: {valore}")
else:
    print("Il link non è valido o non è attivo.")
