import os
from selenium import webdriver
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

urlWebhook = "https://discord.com/api/webhooks/957043914735509624/HQyBkGpyTfBNYwNMSkKnfze5jlvaRzd2sznFD3szdJh4H1sP55AEWduvdjmqlczPmOmm"
url = "https://adecampus.univ-jfc.fr/direct/index.jsp?data=02427bf08a4e3905df54e3828781966417a0456235d61df4705fb52a51c95d7ffb650adbf17b96d5d97cc32ac608bd13facd4837bfc6fce1bd5d96a07a04824c5823238300f7365f22d90e079254e14d6a818c4c1a069cb98a008d7020f28ba25b66babf80b753289969c1b1e23d701dcc7b3d7d5edc1b52b68861b997a2e32fbce01058236ed18878168cf46b2a937d2d2d5b9bb5b4cfc3e41a0fb5035c09561ec7656b708e82cc6634e50913e2a166074e24568258ccc0a0cbc04889b0dae1,1"

def run(promo, semainepro):
    get_page(url, promo, semainepro)

def get_page(url, promo, semainepro):
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    op.add_argument("--headless")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

    driver.get(url)
    # sendWebhook()
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input").send_keys(promo)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/em/button/img").click()
    time.sleep(3)
    if semainepro:
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div/table[4]/tbody/tr[2]/td[2]/em/button").click()
    time.sleep(2)
    data = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[4]").get_attribute('innerHTML')
    planning = BeautifulSoup(data, 'html.parser')
    test = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]").get_attribute('innerHTML')
    dates = BeautifulSoup(test,'html.parser').findAll(class_="labelLegend")
    edt = {}
    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 0px;']"
    lundimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)

    cssheure = "[style*='top: 0px;']"
    lundi = []
    for matiere in lundimatieres:
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        set_matiere_heure(driver, cssheure, matiereparse, lundi)
        lundi.append(matiereparse)

    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 79px;']"
    mardimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    cssheure = "[style*='top: 79px;']"
    mardi = []
    for matiere in mardimatieres:
        matiereparse2 = BeautifulSoup(matiere.get_attribute('outerHTML'), 'html.parser')
        print(matiereparse2)
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        print(matiereparse)
        set_matiere_heure(driver, cssheure, matiereparse, mardi)
        mardi.append(matiereparse)

    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 158px;']"
    mercredimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    cssheure = "[style*='top: 158px;']"
    mercredi = []
    for matiere in mercredimatieres:
        matiereparse2 = BeautifulSoup(matiere.get_attribute('outerHTML'), 'html.parser')
        print(matiereparse2)
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        set_matiere_heure(driver, cssheure, matiereparse, mercredi)
        mercredi.append(matiereparse)

    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 237px;']"
    jeudimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    cssheure = "[style*='top: 237px;']"
    jeudi = []
    for matiere in jeudimatieres:
        matiereparse2 = BeautifulSoup(matiere.get_attribute('outerHTML'), 'html.parser')
        print(matiereparse2)
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        set_matiere_heure(driver, cssheure, matiereparse, jeudi)
        jeudi.append(matiereparse)

    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 316px;']"
    vendredimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    cssheure = "[style*='top: 316px;']"
    vendredi = []
    for matiere in vendredimatieres:
        matiereparse2 = BeautifulSoup(matiere.get_attribute('outerHTML'), 'html.parser')
        print(matiereparse2)
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        set_matiere_heure(driver, cssheure, matiereparse, vendredi)
        vendredi.append(matiereparse)
    semaine = [lundi,mardi,mercredi,jeudi,vendredi]
    i = 0
    for date in dates:
        if(i < 5):
            edt[date.text] = semaine[i]
            i += 1
    print(edt)
    sendWebhook(edt)

def set_matiere_heure(driver, cssheure, matiereparse, jourmatieres):

    # 8h15
    if "8h15" not in str(jourmatieres):
        matierehour = None
        heuredefin = ""
        try:
            hour_css_selector = "div[style*='cursor: auto; position: absolute; left: 7px;']"+cssheure
            matierehour = driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) if driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) else None
            divbrute = BeautifulSoup(matierehour.get_attribute('innerHTML'), 'html.parser')
            if "width:59px" in str(divbrute):
                heuredefin = " - 10h15"
            matierehour = BeautifulSoup(matierehour.get_attribute('innerText'), 'html.parser')
        except:
            print("pas de cours à cette heure là")
        if matierehour and matierehour == matiereparse:
            matiereparse.append(BeautifulSoup('\n+8h15'+heuredefin,'html.parser'))

    # 9h15
    if "9h15" not in str(jourmatieres):
        matierehour = None
        try:
            hour_css_selector = "div[style*='cursor: auto; position: absolute; left: 61px;']"+cssheure
            matierehour = driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) if driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) else None
            matierehour = BeautifulSoup(matierehour.get_attribute('innerText'), 'html.parser')
        except:
            print("pas de cours à cette heure là")
        if matierehour and matierehour == matiereparse:
            matiereparse.append(BeautifulSoup('\n+9h15','html.parser'))

    # 10h30
    if "10h30" not in str(jourmatieres):
        matierehour = None
        heuredefin = ""
        try:
            hour_css_selector = "div[style*='cursor: auto; position: absolute; left: 122px;']"+cssheure
            matierehour = driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) if driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) else None
            divbrute = BeautifulSoup(matierehour.get_attribute('innerHTML'), 'html.parser')
            if "width:59px" in str(divbrute):
                heuredefin = " - 12h30"
            matierehour = BeautifulSoup(matierehour.get_attribute('innerText'), 'html.parser')
        except:
            print("pas de cours à cette heure là")
        if matierehour and matierehour == matiereparse:
            matiereparse.append(BeautifulSoup('\n+10h30'+heuredefin,'html.parser'))

    # 13h45
    if "13h45" not in str(jourmatieres):
        matierehour = None
        heuredefin = ""
        try:
            hour_css_selector = "div[style*='cursor: auto; position: absolute; left: 280px;']"+cssheure
            matierehour = driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) if driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) else None
            divbrute = BeautifulSoup(matierehour.get_attribute('innerHTML'), 'html.parser')
            if "width:60px" in str(divbrute):
                heuredefin = " - 15h45"
            matierehour = BeautifulSoup(matierehour.get_attribute('innerText'), 'html.parser')
        except:
            print("pas de cours à cette heure là")
        if matierehour and matierehour == matiereparse:
            matiereparse.append(BeautifulSoup('\n+13h45'+heuredefin,'html.parser'))

    # 16h00
    if "16h00" not in str(jourmatieres):
        matierehour = None
        heuredefin = ""
        try:
            hour_css_selector = "div[style*='cursor: auto; position: absolute; left: 390px;']"+cssheure
            matierehour = driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) if driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector) else None
            divbrute = BeautifulSoup(matierehour.get_attribute('innerHTML'), 'html.parser')
            if "width:59px" in str(divbrute):
                heuredefin = " - 18h00"
            matierehour = BeautifulSoup(matierehour.get_attribute('innerText'), 'html.parser')
        except:
            print("pas de cours à cette heure là")
        if matierehour and matierehour == matiereparse:
            matiereparse.append(BeautifulSoup('\n+16h00'+heuredefin,'html.parser'))
    
    return matiereparse


def sendWebhook(embed_Cours):

    embed = DiscordEmbed(title='__***' + "EdT Scrapper" + '***__',
                         url=url,
                         #  description='[Item](' + url + ')',
                         color=4894178)

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/931482193170157589/931492488332603402/logo.png?width=779&height=670")

    for date in embed_Cours:
        i = 0
        coursjournee = ""
        title = ""
        for cours in embed_Cours[date]:
            if i == 0:
                title = ':straight_ruler: '+date
            else:
                title = '\u200b'
            coursjournee = str(cours)
            i += 1
            embed.add_embed_field(name=title,
                                  value="```diff\n" + coursjournee + "``` ",
                                  inline=True)

    embed.set_footer(text="ISIS Emploi du temps",
                     icon_url="https://cdn.discordapp.com/attachments/931482193170157589/931486861459869756/ISIS-logo-verti-RVB.png")

    embed.set_timestamp()

    webhook = DiscordWebhook(url=urlWebhook, username="ISIS",
                             avatar_url="https://media.discordapp.net/attachments/848264360119238706/849298764530974760/webhook_2_2.png")
    webhook.add_embed(embed)
    webhook.execute()
    print("Webhook sent!")

