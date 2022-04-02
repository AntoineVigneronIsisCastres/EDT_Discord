from selenium import webdriver
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def set_matiere_heure(driver, matiereparse):

    # 8h15
    hour_css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 0px;'][style*='left: 12px;']"
    matierehour = driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector)
    matierehour = BeautifulSoup(matierehour.get_attribute('innerText'), 'html.parser')
    if matierehour and matierehour == matiereparse:
        print("le premier élément de lundimatieres et le css selector = 10h30")
        print(matierehour)
        print(matiereparse)
        print(driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector))
        matiereparse.append(BeautifulSoup('\n8h15','html.parser'))

    # 10h30
    hour_css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 0px;'][style*='left: 122px;']"
    matierehour = driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector)
    matierehour = BeautifulSoup(matierehour.get_attribute('innerText'), 'html.parser')
    if matierehour and matierehour == matiereparse:
        print("le premier élément de lundimatieres et le css selector = 10h30")
        print(matierehour)
        print(matiereparse)
        print(driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector))
        matiereparse.append(BeautifulSoup('\n10h30','html.parser'))

    # 13h45
    hour_css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 0px;'][style*='left: 280px;']"
    matierehour = driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector)
    matierehour = BeautifulSoup(matierehour.get_attribute('innerText'), 'html.parser')
    if matierehour and matierehour == matiereparse:
        print("le premier élément de lundimatieres et le css selector = 10h30")
        print(matierehour)
        print(matiereparse)
        print(driver.find_element(by=By.CSS_SELECTOR, value=hour_css_selector))
        matiereparse.append(BeautifulSoup('\n10h30','html.parser'))
    
    return matiereparse


def get_page(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(url)
    # sendWebhook()
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input").send_keys("fia3")
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/em/button/img").click()

    time.sleep(3)
    data = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[4]").get_attribute('innerHTML')
    planning = BeautifulSoup(data, 'html.parser')
    print(planning)
    test = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]").get_attribute('innerHTML')
    dates = BeautifulSoup(test,'html.parser').findAll(class_="labelLegend")
    edt = {}
    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 0px;']"
    lundimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)

    print("ça c'est lundi")
    print(lundimatieres)
    lundi = []
    for matiere in lundimatieres:
        matierehtml = BeautifulSoup(matiere.get_attribute('outerHTML'), 'html.parser')
        print(matierehtml)
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        print(matiereparse)
        set_matiere_heure(driver, matiereparse)
        lundi.append(matiereparse)

    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 91px;']"
    mardimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    print("ça c'est mardi")
    print(mardimatieres)
    mardi = []
    for matiere in mardimatieres:
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        print(matiereparse)
        mardi.append(matiereparse)

    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 182px;']"
    mercredimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    print("ça c'est mercredi")
    print(mercredimatieres)
    mercredi = []
    for matiere in mercredimatieres:
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        print(matiereparse)
        mercredi.append(matiereparse)

    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 274px;']"
    jeudimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    print("ça c'est jeudi")
    print(jeudimatieres)
    jeudi = []
    for matiere in jeudimatieres:
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        print(matiereparse)
        jeudi.append(matiereparse)

    css_selector = "div[style*='cursor: auto; position: absolute;'][style*='top: 365px;']"
    vendredimatieres = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    print("ça c'est vendredi")
    print(vendredimatieres)
    vendredi = []
    for matiere in vendredimatieres:
        matiereparse = BeautifulSoup(matiere.get_attribute('innerText'), 'html.parser')
        print(matiereparse)
        vendredi.append(matiereparse)

    semaine = [lundi,mardi,mercredi,jeudi,vendredi]
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    i = 0
    for date in dates:
        if(i < 5):
            print(date.text)
            edt[date.text] = semaine[i]
            print(i)
            i += 1
    
    print("on fait un test en deuspi")
    print(edt)

    sendWebhook(edt)
    time.sleep(1000)

def sendWebhook(embed_Cours):

    embed = DiscordEmbed(title='__***' + "EdT Scrapper" + '***__',
                         url=url,
                         #  description='[Item](' + url + ')',
                         color=4894178)

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/931482193170157589/931492488332603402/logo.png?width=779&height=670")

    for date in embed_Cours:
        i = 0
        print("ayooooooo")
        print(embed_Cours)
        print(date)
        coursjournee = ""
        title = ""
        for cours in embed_Cours[date]:
            if i == 0:
                title = ':straight_ruler: '+date
            else:
                title = '\u200b'
            print(str(cours))
            coursjournee = str(cours)
            i += 1
            embed.add_embed_field(name=title,
                                  value="```\n" + coursjournee + "``` ",
                                  inline=True)
        #embed.add_embed_field(name='\u200b', value='\u200b')
    embed.set_footer(text="ISIS Emploi du temps FIA3",
                     icon_url="https://cdn.discordapp.com/attachments/931482193170157589/931486861459869756/ISIS-logo-verti-RVB.png")

    embed.set_timestamp()

    webhook = DiscordWebhook(url=urlWebhook, username="ISIS",
                             avatar_url="https://media.discordapp.net/attachments/848264360119238706/849298764530974760/webhook_2_2.png")
    webhook.add_embed(embed)
    webhook.execute()
    print("Webhook sent!")

urlWebhook = "https://discord.com/api/webhooks/957043914735509624/HQyBkGpyTfBNYwNMSkKnfze5jlvaRzd2sznFD3szdJh4H1sP55AEWduvdjmqlczPmOmm"
url = "https://adecampus.univ-jfc.fr/direct/index.jsp?data=02427bf08a4e3905df54e3828781966417a0456235d61df4705fb52a51c95d7ffb650adbf17b96d5d97cc32ac608bd13facd4837bfc6fce1bd5d96a07a04824c5823238300f7365f22d90e079254e14d6a818c4c1a069cb98a008d7020f28ba25b66babf80b753289969c1b1e23d701d8a96fc2bd08f9dcf79c796321f919fe8bce01058236ed18878168cf46b2a937d2d2d5b9bb5b4cfc3e41a0fb5035c09561ec7656b708e82cc6634e50913e2a166074e24568258ccc0a0cbc04889b0dae1,1"
get_page(url)
