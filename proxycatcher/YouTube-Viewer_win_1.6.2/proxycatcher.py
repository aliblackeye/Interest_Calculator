from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKGREEN + """



██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗  ░█████╗░░█████╗░████████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░██║██╔════╝██╔══██╗
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░  ██║░░╚═╝███████║░░░██║░░░██║░░╚═╝███████║█████╗░░██████╔╝
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░  ██║░░██╗██╔══██║░░░██║░░░██║░░██╗██╔══██║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░  ╚█████╔╝██║░░██║░░░██║░░░╚█████╔╝██║░░██║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝



"""+ bcolors.ENDC)

#######################################

http_proxies = []
socks4_proxies = []
socks5_proxies = []
all_proxies = []

#######################################

def proxyscraper_http():
    proxies2 = []
    link = "https://proxyscrape.com/share/l5ty3b9"

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    while(True):

        proxies2 = browser.find_element_by_tag_name("textarea").text

        if proxies2=="Loading...":
            continue

        else:
            proxies2 = proxies2.split("\n")
            browser.close()
            return proxies2

def proxyscraper_socks4():
    proxies2 = []
    link = "https://proxyscrape.com/share/qyirn63"

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)
    browser.get(link)


    while(True):

        proxies2 = browser.find_element_by_tag_name("textarea").text

        if proxies2=="Loading...":
            continue

        else:
            proxies2 = proxies2.split("\n")
            browser.close()
            return proxies2

def sslproxies_all():
    proxies = []
    link = "https://www.sslproxies.org"
    kaynak = requests.get(link)
    veriCek = BeautifulSoup(kaynak.text,"html.parser")

    for i in veriCek.find_all("tr")[:101]:

        try:
            data = i.find_all("td")
            ip = data[0].text

            port = data[1].text
            type_ = data[4].text

            proxy = ip + ":" + port
            proxies.append(proxy)
            
        except:
            pass
    
    return proxies

def freeproxycz_all():
    proxies3 = []
    
    link = "http://free-proxy.cz/en/proxylist/country/all/https/ping/all/"
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    linkler = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/span")
    linkler.click()

    proxyler = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[6]")
    adresler = []
    adresler = proxyler.text.split("\n")

    #-------------------------------------IKINCI SAYFA------------------------------------------#

    browser.get("http://free-proxy.cz/en/proxylist/country/all/https/ping/all/2")

    linkler2 = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/span")
    linkler2.click()

    proxyler2 = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[6]")
    adresler2 = []
    adresler2 = proxyler2.text.split("\n")

    browser.close()
    
    for i in adresler:
        proxies3.append(i)

    for i in adresler2:
        proxies3.append(i)
    #-------------------------------------------------------------------------------------------#
    return proxies3

def advancedname_all():
    proxies = []
    link = "https://advanced.name/freeproxy"

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    for i in range(1,101):
        xpath_ip = "/html/body/section[2]/div[4]/table/tbody/tr[{}]/td[2]".format(i)
        xpath_port = "/html/body/section[2]/div[4]/table/tbody/tr[{}]/td[3]".format(i)

        ip = browser.find_element_by_xpath(xpath_ip).text
        port = browser.find_element_by_xpath(xpath_port).text
        
        proxies.append(ip+":"+port)

    browser.close()
        

    return proxies

def spysone_all():
    proxies = []
    link = "https://spys.one/en/free-proxy-list/"

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)
    browser.get(link)    

    for i in range(4):
        secim = Select(browser.find_element_by_xpath("/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/font/select[1]"))
        secim.select_by_index(5)
        
    for i in range(3,503):
        temp = browser.find_element_by_xpath("/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[{}]/td[1]/font".format(str(i)))
        proxies.append(temp.text)


    browser.close()
    
    return proxies

def proxyscanio_all():
    proxies = []
    link = "https://www.proxyscan.io"
    kaynak = requests.get(link)
    veriCek = BeautifulSoup(kaynak.text,"html.parser")

    for i in veriCek.find("tbody",{"id":"loadPage"}).find_all("tr"):
        ip = i.find("th").text
        port = i.find("th").find_next().text
        proxies.append(ip+":"+port)
        
    return proxies


def proxylistdownload_http():
    proxies = []
    link = "https://www.proxy-list.download/HTTP"
    kaynak = requests.get(link)
    veriCek = BeautifulSoup(kaynak.text,"html.parser")

    for i in veriCek.find("tbody",{"id":"tabli"}).find_all("tr"):
        ip = (i.find_all("td")[0].text)
        port = (i.find_all("td")[1].text)

        proxies.append(ip+":"+port)

    kaynak = requests.get("https://www.proxy-list.download/HTTPS")
    for i in veriCek.find("tbody",{"id":"tabli"}).find_all("tr"):
        ip = (i.find_all("td")[0].text)
        port = (i.find_all("td")[1].text)

        proxies.append(ip+":"+port)

    return proxies


def proxylistdownload_socks4():
    proxies = []
    link = "https://www.proxy-list.download/SOCKS4"
    kaynak = requests.get(link)
    veriCek = BeautifulSoup(kaynak.text,"html.parser")

    for i in veriCek.find("tbody",{"id":"tabli"}).find_all("tr"):
        ip = (i.find_all("td")[0].text)
        port = (i.find_all("td")[1].text)

        proxies.append(ip+":"+port)

    return proxies


def proxylistdownload_socks5():
    proxies = []
    link = "https://www.proxy-list.download/SOCKS5"
    kaynak = requests.get(link)
    veriCek = BeautifulSoup(kaynak.text,"html.parser")

    for i in veriCek.find("tbody",{"id":"tabli"}).find_all("tr"):
        ip = (i.find_all("td")[0].text)
        port = (i.find_all("td")[1].text)

        proxies.append(ip+":"+port)

    return proxies

    
# def openproxyspace_all():
#     proxies = []
#     link = "https://openproxy.space/list"

#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
#     options = webdriver.ChromeOptions()
#     options.headless = True
#     options.add_argument(f'user-agent={user_agent}')
#     options.add_argument("--window-size=1920,1080")
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--allow-running-insecure-content')
#     options.add_argument("--disable-extensions")
#     options.add_argument("--proxy-server='direct://'")
#     options.add_argument("--proxy-bypass-list=*")
#     options.add_argument("--start-maximized")
#     options.add_argument('--disable-gpu')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--no-sandbox')
#     browser = webdriver.Chrome(options=options)
#     browser.get(link)

#     amcik = browser.find_elements_by_class_name("lists")[0].find_elements_by_tag_name("a")
#     print(amcik)


#     browser.close()


# openproxyspace_all()


#######################################

while(True):

    try:
        answer = int(input(bcolors.OKCYAN +"HTTP = '1' | SOCKS4 = '2' | SOCKS5 = '3' | ALL = '4'\nPlease select a protocol = "+ bcolors.ENDC))

        if answer == 1: #http
            print(bcolors.BOLD +"""
            ------------
                HTTP
            ------------
            """+bcolors.ENDC)

            for i in proxylistdownload_http():
                http_proxies.append(i)

            for i in proxyscraper_http():
                http_proxies.append(i)

            with open("http_proxies.txt","w") as proxies_http:
                for http_proxy in http_proxies:
                    proxies_http.write(http_proxy+"\n")

                proxies_http.close()

            print(bcolors.BOLD + """

            --------------------------
             CAPTURED PROXIES : {}
            --------------------------
            
            """.format(len(http_proxies)))


            break

        elif answer == 2: #socks4
            print(bcolors.BOLD +"""
            ------------
               SOCKS4
            ------------
            """+bcolors.ENDC)

            for i in proxyscraper_socks4():
                socks4_proxies.append(i)

            with open("socks4_proxies.txt","w") as proxies_socks4:
                for socks4_proxy in socks4_proxies:
                    proxies_socks4.write(socks4_proxy+"\n")

                proxies_socks4.close()

            print(bcolors.BOLD +"""

            --------------------------
             CAPTURED PROXIES : {}
            --------------------------
            
            """.format(len(socks4_proxies)))

            break

        elif answer == 3: #henuz eklenmedi
            print(bcolors.BOLD +"""
            ------------
               SOCKS5
            ------------
            """+bcolors.ENDC)

            for i in proxylistdownload_socks5():
                socks5_proxies.append(i)


            with open("socks5_proxies.txt","w") as proxies_socks5:
                for socks5_proxy in socks5_proxies:
                    proxies_socks5.write(socks5_proxy+"\n")     

                proxies_socks5.close()


            break

        elif answer == 4: #all
            
            print(bcolors.BOLD +"""
            -------------
             ALL PROXIES
            -------------
            """+bcolors.ENDC)

            for i in sslproxies_all():
                all_proxies.append(i)
            
            for i in freeproxycz_all():
                all_proxies.append(i)

            for i in advancedname_all():
                all_proxies.append(i)

            for i in proxyscraper_http():
                all_proxies.append(i)

            for i in proxyscraper_socks4():
                all_proxies.append(i)

            for i in spysone_all():
                all_proxies.append(i)

            for i in proxyscanio_all():
                all_proxies.append(i)

            for i in proxylistdownload_http():
                all_proxies.append(i)

            for i in proxylistdownload_socks4():
                all_proxies.append(i)

            for i in proxylistdownload_socks5():
                all_proxies.append(i)



            print(bcolors.BOLD +"""

            --------------------------
             CAPTURED PROXIES : {}
            --------------------------
            
            """.format(len(all_proxies)))



            with open("all_proxies.txt","w") as proxies_all:
                for all_proxy in all_proxies:
                    proxies_all.write(all_proxy+"\n")

                proxies_all.close()

            break

        else:
            print(bcolors.BOLD +"Invalid, please try again.\n"+bcolors.ENDC)

    except ValueError:
        print(bcolors.BOLD +"Invalid, please try again.\n"+bcolors.ENDC)





