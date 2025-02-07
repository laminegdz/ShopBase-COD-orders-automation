from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import random
import string
from selenium.webdriver.common.keys import Keys



algeria_cities = [
    "Algiers", "Oran", "Constantine", "Annaba", "Blida", "Batna", "Djelfa", "Setif", 
    "Sidi Bel Abbes", "Biskra", "Tiaret", "Tlemcen", "Ouargla", "Bejaia", "Skikda", 
    "Mostaganem", "Tizi Ouzou", "Mascara", "Ghardaia", "Relizane", "El Oued", "Boumerdes", 
    "Bouira", "Chlef", "Medea", "Ain Defla", "Laghouat", "Khenchela", "Ain Temouchent", 
    "Tindouf", "Tamanrasset", "Adrar", "Saida", "Illizi", "Tebessa", "El Bayadh", 
    "Naama", "Bordj Bou Arreridj", "Tipaza", "Guelma", "Jijel", "Mila", "Souk Ahras", 
    "Tissemsilt", "El Tarf", "Bechar", "Oum El Bouaghi"
]


with open('data/arabic_latin_names.txt', 'r', encoding='utf-8') as file:
    names = file.readlines()

def generate_algerian_phone_number():
    prefixes = ['078121', '077469', '055534', '067275']
    prefix = random.choice(prefixes)
    remaining_digits = ''.join(random.choices("0123456789", k=4))
    phone_number = f"{prefix}{remaining_digits}"
    return phone_number


def setup_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


order_count = 0




while True:

    
    driver = setup_driver()  

    driver.get("wwww.example.com")
    time.sleep(3)
    

    with open('emails.txt', 'r', encoding='utf-8') as email_file:
        emails = email_file.readlines()

    if not emails:
        print("-------------- EMAILS ARE EMPTY ------------")
        driver.quit()
        break

    current_email = emails[0].strip()
    wait = WebDriverWait(driver, 30)

    
    buy_now=wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Buy now']")))

    try:
        buy_now.click()
    except:
        time.sleep(2)
        buy_now.click()
    
    


    time.sleep(6)

    email=wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
    email.click()
    email.clear()
    email.send_keys(current_email)
    

    first_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First name']")))
    first_name.click()
    first_name.send_keys(random.choice(names))
    time.sleep(0.5)
    
    last_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Last name']")))
    last_name.click()
    last_name.send_keys(random.choice(names))
    time.sleep(1)
    address = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Address']")))
    address.click()
    address.send_keys(random.choice(names))


    city = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='City']")))
    time.sleep(0.5)
    city.click()
    city.send_keys(random.choice(algeria_cities))

    time.sleep(0.5)
    province=wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Region']")))
    province.click()
    random_city=random.choice(algeria_cities)
    select_prv=wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Guadeloupe']")))
    select_prv.click()
    time.sleep(0.5)
    zip=wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Zip Code']")))
    zip.click()
    zip.send_keys("15000")

    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.END)
    body.send_keys(Keys.END)
    body.send_keys(Keys.END)
    body.send_keys(Keys.END)
    body.send_keys(Keys.END)
    time.sleep(0.5)
    body.send_keys(Keys.END)
    body.send_keys(Keys.END)
    body.send_keys(Keys.END)
    body.send_keys(Keys.END)

    time.sleep(1)


    place_order = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='d-block checkout-navigation__btn-title has-text-weight-bold']")))
    time.sleep(0.5)
    place_order.click()
    
    with open('emails.txt', 'w', encoding='utf-8') as email_file:
            email_file.writelines(emails[1:])

    time.sleep(6)
    driver.quit()
    print (" [{order_count}] :  {current_email} sent ")


