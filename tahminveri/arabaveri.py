from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

import pypyodbc

veritabani = pypyodbc.connect(  #Veritabanına bağlanıyorum
    'Driver={SQL Server};'
    'Server=DESKTOP-3R0RFV2\SQLEXPRESS;'
    'Database=tahminverileri;'
    'Trusted_Connection=True;'
)

imlec = veritabani.cursor() #Veritabanında sorgu çalıştırmak için imleç oluşturuyorum

arabalar = [] # Marka Seri Yil YakitTipi MotorGucu Kilometre Fiyat Bilgilerinin geldiği liste



def sahibinden():
    link = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&pagingSize=50&category=3530"
            

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
    browser.get(link) #siteye gir
    browser.maximize_window()
    time.sleep(10) #siteye girdikten sonra 10sn bekle
    sayfa=1

    while(True):

        for i in range(1,52): #50 ilanın bilgilerini alır
            if(i==4):
                pass

            else:

                
                #ilana tikla
                try:
                    ilan = browser.find_element_by_xpath("/html/body/div[5]/div[4]/form/div/div[3]/table/tbody/tr[{}]".format(str(i))) #ilan sırası
                    time.sleep(5)
                    browser.execute_script("arguments[0].scrollIntoView();",ilan )
                    ilan.click()
                    print("{}. ilana tıklandı.".format(i))



                    #bilgileri al
                    ilanbilgileri = []
                    ilanbilgileri.append(browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div[2]/div[2]/ul/li[3]/span").text) #Marka
                    ilanbilgileri.append(browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div[2]/div[2]/ul/li[4]/span").text) #Seri
                    ilanbilgileri.append(browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div[2]/div[2]/ul/li[6]/span").text) #Yil
                    ilanbilgileri.append(browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div[2]/div[2]/ul/li[7]/span").text) #YakitTipi
                    ilanbilgileri.append((browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div[2]/div[2]/ul/li[11]/span").text).split(" ")[0]) #MotorGucu
                    ilanbilgileri.append( (browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div[2]/div[2]/ul/li[9]/span").text).replace(".","") ) #Kilometre
                    ilanbilgileri.append(((browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div[2]/div[2]/h3").text).split("\n"))[0].replace(".","").split(" ")[0]) #Fiyat
                except:
                    print("Sayfa numarası:",sayfa)
                    print("Bir yerde bir sorun yaşadınız.")
                    continue
                    


                #INSERT KISMI

                imlec.execute("INSERT INTO Arabalar VALUES(?,?,?,?,?,?,?)",ilanbilgileri)
                veritabani.commit()

                #------------------------------------------------------------------------------------------#
                print(ilanbilgileri)
                ilanbilgileri.clear() # yeni ilan bilgilerini almak için eski ilan bilgilerini sil

                #geri don
                browser.back()
                print("{}. sayfaya geri dönüldü.".format(sayfa))

        try:
            if(sayfa == 20 or 2<=sayfa<=5):
                sonrakibutonu = browser.find_element_by_xpath("/html/body/div[5]/div[4]/form/div/div[3]/div[3]/div[1]/ul/li[13]/a")
                sonrakibutonu.click()
                sayfa+=1
                time.sleep(10)

            elif(sayfa == 1):
                sonrakibutonu = browser.find_element_by_xpath("/html/body/div[5]/div[4]/form/div/div[3]/div[3]/div[1]/ul/li[12]/a")
                sonrakibutonu.click()
                sayfa+=1
                time.sleep(10)

            elif(6<=sayfa<=14):
                sonrakibutonu = browser.find_element_by_xpath("/html/body/div[5]/div[4]/form/div/div[3]/div[3]/div[1]/ul/li[15]/a")
                sonrakibutonu.click()
                sayfa+=1
                time.sleep(10)
            
            elif(15<=sayfa<=19):
                sonrakibutonu = browser.find_element_by_xpath("/html/body/div[5]/div[4]/form/div/div[3]/div[3]/div[1]/ul/li[14]/a")
                sonrakibutonu.click()
                sayfa+=1
                time.sleep(10)
        except:
            print("*********Başarılı!********")
            break #eğer sonraki butonu yok ise döngüyü bitir  



sahibinden()



#SELECT KISMI

imlec.execute("SELECT * FROM Arabalar") #İmleç ile bir SQL sorgusu çağırıyorum
veriler = imlec.fetchall() #Sorgudan dizi olarak dönen sonuçları bir değişkene aktarıyorum
for i in veriler:
    print(i)

#------------------------------------------------------------------------------------------#