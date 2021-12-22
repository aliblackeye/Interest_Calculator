from datetime import datetime
import locale #Kütüphaneleri import ediyoruz.

#Satın aldıktan sonra tarihin türkçe olması için kullandığım kod.
locale.setlocale(locale.LC_ALL, '')

#Kullanıcılarımız.
kullanıcılar ={'Ali':'istinye123','Meryem':'4444','a':'a'}

#Envanterimiz.
Envanter = {'Kuşkonmaz': [10,5], 'Brokoli': [15,6], 'Havuç': [18,7],
'Elmalar': [20,5], 'Muz': [10, 8], 'Meyve': [30,3], 'Yumurta': [50,2],
'Karışık meyve suyu': [0,18], 'Balık çubukları': [25,12], 'Dondurma': [32,6],
'Elma suyu': [40,7], 'Portakal suyu': [30,8], 'Üzüm suyu': [10,9]} 

#Sepet sözlüğümüzü tanıtıyoruz.
sepet = {}
Envanter2=','.join(Envanter.keys())
#Envanter keylerini envanter2 ye atıyoruz.

#İsim girdilerini burada alıyoruz.
def isim_girdileri():
    print("**** İstinye Online Market’e Hoşgeldiniz ****\n")
    
    while(True):
        print("Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın: \n")

        print("Kullanıcı Adınız: ",end="")
        kullanici_adi=input()
        print("Şifreniz: ",end="") 
        sifre=input()

        #Kullanıcı girişi için girilen input değerlerini kontrol ediyoruz.
        a=True
        for i in kullanıcılar.keys():
            if i ==kullanici_adi and kullanıcılar.get(i)==sifre:
                a=False
                print("\nHoşgeldiniz",kullanici_adi,"! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.\n")
                
                Keyler=list(Envanter.keys())
                for i in Keyler:
                    try:
                        if sepet[kullanici_adi].get(Keyler[0])==Keyler[0]:
                            pass
                    except:
                        sepet[kullanici_adi]={}        
                
                return kullanici_adi
                #Kullanıcı adını döndürüyoruz.
        if a:
            print("\nKullanıcı adı veya şifreniz hatalı\n")
        else:
            break

#Ekrana hizmetlerimizi yazdırıyoruz.
def hizmetler():
    while(True):
        print("""Lütfen aşağıdaki hizmetlerden birini seçin: 
        1. Ürün ara 
        2. Sepete git 
        3. Satın al 
        4. Oturum Kapat 
        5. Çıkış yap""")
        
        print("\nSeciminiz: ",end="")
        #Eğer secim 5ten büyükse veya 1 den küçükse hata vermesi için şart koyuyoruz.
        try:
            secim=int(input())
            if secim>5 or secim<1:
                print("Lütfen seçiminizi doğru yapınız")
            else:
                break
        except(ValueError):
            print("Lütfen seçiminizi doğru yapınız")
    #Aldığımız secim değerini return ediyoruz.
    return secim

#Kullanıcının istediği ürünü envanterde arattığımız kısım.
def urun_arama(secim,kullanici_adi):
    kontrol2=True
    while(kontrol2):
        if secim==1: #Secim değişkenimiz hizmetler fonksiyonunda 1 seçilmişse ne arıyorsunuz diye soruyoruz.
            print("Ne arıyorsunuz ?",end="")
            arama_kelimesi=input().strip() #Arayacağı kelimeyi input alıyoruz.
            kontrol3=True
            while(kontrol3):
                if arama_kelimesi in Envanter2: #Envanter2'de arama kelimesini döndürüyoruz.
                    kontrol2=False
                    a=Envanter2.split(',') #a değişkenine envanter2 nin değişkenlerini aralarında virgül olacak şekilde liste yapıyoruz.
                    bulunanlar=[] #Arama kelimesine göre bulunan ürünleri bu listeye atıyoruz.
                    b=0
                    for i in range(len(a)): #a'nın uzunluğuna göre döngüye giriyoruz.
                        if arama_kelimesi in a[i] and Envanter.get(a[i])[0]>0: #a'nın indeksinde arama keliesi var mı ve envanterde a'ın indeksinde ve [0] stok miktarı sıfırdan büyük mü diye bakıyoruz.
                            bulunanlar.append(a[i]) #Şartlar sağlanıyorsa bulunanlar listesine a[i]'ni atıyoruz.
                            b+=1#Şartlar sağlanınca b'yi 1 arttırıyoruz.
                    index=1
                    print("\n"+str(b),"ürün bulundu !\n")
                    for i in range(len(bulunanlar)): #Bulunanların uzunluğuna göre döngü açıyoruz.
                        if Envanter.get(bulunanlar[i])[0]>0: #Envanterden kontrol ediyoruz.
                            print(str(index)+"-)",bulunanlar[i],Envanter.get(bulunanlar[i])[1],"$") #Eklediğimiz ürünü ekrana yazıyoruz.
                            index+=1
                    print("Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin):")
                    try:
                        urun_secimi=int(input())
                    except(ValueError):
                        kontrol3=True
                        print("Lütfen bir sayı giriniz !")
                        continue
                    if urun_secimi==0:
                        print("Ana menüye dönülüyor.")
                        return True
                    elif urun_secimi>len(bulunanlar):
                        kontrol3=True
                        print("Lütfen geçerli bir seçim yapınız !")
                    
                    else:
                        print(bulunanlar[urun_secimi-1],"ekleniyor") #Eklenen ürünü ekrana basıyoruz.
                        while True:
                            print("Kaç tane istiyorsunuz?")
                            miktar_secim=int(input())
                            if miktar_secim==0:
                                print("Miktarı '0' yapamazsınız !")
                            else:
                                break
                        if Envanter.get(bulunanlar[urun_secimi-1])[0]>=miktar_secim: #Miktar_secim stok miktarından küçükse if'e giriliyor.
                            sepet[kullanici_adi][bulunanlar[urun_secimi-1]]=[Envanter.get(bulunanlar[urun_secimi-1])[1]*miktar_secim,miktar_secim]
                            #Sepete aldığımız bilgileri kullanıcıların sepetlerine ekliyoruz. Toplam fiyatını ve miktarı da sepete ekliyoruz.
                            print("Sepetinize",miktar_secim,"adet",bulunanlar[urun_secimi-1],"eklenmiştir.")
                            print("Ana menüye dönülüyor...")
                            return False,True
                        else:
                            kontrol3=True
                            kontrol2=False
                            #Stok miktarını kontrol edip verdiğimiz hata burada.
                            print("\n",bulunanlar[urun_secimi-1],"ürününün stok miktarı,",str(Envanter.get(bulunanlar[urun_secimi-1])[0])+"'dir. Lütfen tekrar deneyiniz !")
                            return True,False
                else:
                    kontrol2=True
                    kontrol3=True
                    print("\nAradığınız ürün mağazamızda bulunamadı. Lütfen tekrar deneyiniz!")    
                    return True,False  
        else:
            return False,False

#Sepete git fonksiyonumuz.
def sepet_git(secim,kullanici_adi):
    if secim==2:
        if sepet[kullanici_adi]=={}: #Sepet boş mu dolu mu kontrol ediyoruz.
            print("Sepetiniz boş...")
            secim=None 
            return True
        else:
            print("\nSepetinizde bunlar bulunuyor -->")
            print("")
            toplam=sepet_yazdır(kullanici_adi) #Sepette bulunanları yazdırdığımız yer.
            print("Genel Toplam -->",toplam,"$")
            secim=str(secim)
            sepet_alt_menu(secim,kullanici_adi)

#Sepet alt menüsüne gidiyoruz.
def sepet_alt_menu(secim,kullanici_adi):
    if secim=="2":
        kontrol7=True
        while (kontrol7): #Seçeneklerimizi ekrana basıyoruz.
            print("\n    Bir seçeneği seçiniz:")
            print("        1. Tutarı güncelleyin" )
            print("        2. Bir öğeyi kaldırın")
            print("        3. Satın alın" )
            print("        4. Ana menüye dönün")
            secim1=input("Seciminiz: ")
            kontrol5=True
            while kontrol5:
                if secim1=="1":
                    if sepet[kullanici_adi]=={}: #Kullanıcının sepeti boşsa sepetiniz boş demesi için sepet yazdır fonksiyonunu çağırıyoruz.
                        sepet_yazdır(kullanici_adi)
                        kontrol7=True
                        kontrol5=False
                    else:
                        sepet_yazdır(kullanici_adi) 
                        miktar_degistirme=int(input("Hangi ürünün miktarını değiştirmek istersiniz? (Sayı olarak giriniz)"))
                        index2=1 
                        for i in range(len(sepet)):
                            if miktar_degistirme==index2:
                                sepet2=list(sepet[kullanici_adi].keys()) #Sepet2 değişkenine kullanıcının anahtarlarını atıyoruz.
                                while True:
                                    while True:
                                        print("Lütfen yapcağınız miktar değişikliğini giriniz !")
                                        degisiklik=int(input())
                                        if degisiklik==0: #Miktar değişikliğimizi alıyoruz.
                                            print("Miktarı '0' yapamazsınız !")
                                        else:
                                            break
                                    if degisiklik>Envanter.get(sepet2[index2-1])[0] or degisiklik<=0: #Miktar değişikliğinin stok miktarını kontrol ediyoruz.
                                        print(sepet2[index2-1],"ürününün stok miktarı,",str(Envanter.get(sepet2[index2-1])[0])+"'dir. Lütfen tekrar deneyiniz !")
                                    else:
                                        #Yukarıdaki şart sağlanmıyorsa yeni miktarla sepeti güncelliyoruz.
                                        sepet_guncel= {sepet2[index2-1]: [sepet[kullanici_adi].get(sepet2[0])[0],degisiklik]}
                                        sepet[kullanici_adi].update(sepet_guncel)
                                        break
                            index2+=1
                        print("Güncel sepetiniz -->")
                        sepet_yazdır(kullanici_adi) #Sepeti yazdırıyoruz.
                        print("Tekrar işlem yapmak için '1', Ana menüye dönmek için '0' yazınız !")
                        secim2=input()
                        if secim2=="1":
                            kontrol7=True
                            kontrol5=True
                        elif secim2=="0":
                            kontrol7=False
                            kontrol5=False
                            kontrol6=True
                            return kontrol6
                if secim1=="2":
                    if sepet[kullanici_adi]=={}:
                        sepet_yazdır(kullanici_adi)
                        kontrol7=True
                        kontrol5=False
                    else:
                        sepet_yazdır(kullanici_adi)
                        secim3=int(input("Hangi öğeyi kaldırmak istiyorsunuz?"))
                        index2=0 #Öge kaldırma seçimi yaptırıyoruz.
                        a=list(sepet[kullanici_adi].keys())
                        for i in a:
                            index2+=1
                            if str(secim3)==str(index2):
                                
                                print(a[secim3-1],"kaldırıldı !\n")
                                sepet[kullanici_adi].pop(a[secim3-1]) #Seçilen ürünü sepetten kaldırıyoruz.
                                print("Güncel sepetiniz -->\n")
                                sepet_yazdır(kullanici_adi)
                                print("Sepet Alt Menüsüne Dönülüyor...")
                                sepet_alt_menu(secim,kullanici_adi)
                        kontrol7=False
                        kontrol5=False
                elif secim1=="3":
                    if sepet[kullanici_adi]=={}:
                        sepet_yazdır(kullanici_adi)
                        kontrol7=True
                        kontrol5=False
                    else:
                        satın_al_2(kullanici_adi)
                        kontrol7=False
                        kontrol5=False
                elif secim1=="4":
                    kontrol7=False
                    kontrol5=False
                    print("Ana menüye dönülüyor...")
                    main_cagır(kullanici_adi)
                else:
                    kontrol7=True
                    kontrol5=False
                    print("Lütfen [1-5] arasında bir sayı girin.")

#Kullanıcının ürünleri satın alacağı zaman çağırdığımız fonksiyonlar.
def satın_al(secim,kullanici_adi):
    if secim==3:
        if sepet[kullanici_adi]=={}: #Sepet boşsa satın alma kısmına geçmiyor.
            sepet_yazdır(kullanici_adi)
        else: #Sepet boş değilse satın alıyoruz.
            satın_al_2(kullanici_adi)
def satın_al_2(kullanici_adi):
        print("\nMakbuzunuz işleniyor ...\n")
        print("******* İstinye Online Market ********")
        print("*************************************")
        print("    0850 283 6000")
        print("    istinye.edu.tr")
        print("————————————————————————————————————")
        toplam=sepet_yazdır(kullanici_adi)
        print("Genel Toplam -->", toplam, "$")
        print("————————————————————————————————————")
        an = datetime.now()
        tarih=datetime.strftime(an, '%d %B %Y %X')
        print("Tarih :",tarih,"\n")
        
        print("Satın alımınız için teşekkürler !")
        for i in sepet[kullanici_adi].keys():
            yeni_stok=Envanter.get(i)[0]-sepet[kullanici_adi].get(i)[1]
            envanter_guncelleme={i: [yeni_stok,Envanter.get(i)[1]]}
            Envanter.update(envanter_guncelleme)

        sepet[kullanici_adi].clear()
        tekrar_islem()

#Tekrar işlem yapıp yapmak istemediğini soruyoruz.
def tekrar_islem():
    print("Tekrar işlem yapmak ister misiniz ?")
    print("      1-) EVET 2-) HAYIR")
    secim4=input()
    secim4=secim4.upper()
    secim4=secim4.strip()
    if secim4=="1" or secim4=="EVET":
        print("Ana menüye dönülüyor...")
    elif secim4=="2" or secim4=="HAYIR":
        print("Bizleri tercih ettiğiniz için teşekkürler :)")
        exit()

#Sepeti yazdırıyoruz.
def sepet_yazdır(kullanici_adi):
    if sepet[kullanici_adi]=={}:
        print("Sepetiniz boş...\n")
    index=0
    toplam=0
    for i in sepet.keys():
        if i==kullanici_adi:
            for i in sepet[kullanici_adi].keys():
                index +=1 #Sıralayarak sepeti ekrana basıyoruz.
                print(str(index)+"-)",sepet[kullanici_adi].get(i)[1],"Adet,",i,"aldınız. Fiyat=",sepet[kullanici_adi].get(i)[0],"$")
                toplam+=sepet[kullanici_adi].get(i)[0] #Toplam fiyatı elde ediyoruz.
    return toplam #Toplamı döndürüyoruz.

#Oturumu kapatma fonksiyonu.
def oturum_kapat():
    print("Oturumunuz sonlanmıştır!")
    kullanici_adi=isim_girdileri()
    return kullanici_adi

#Uygulamayı kapattığımız fonksiyon.
def cikis_yap():
    print("Programdan çıkış yapılıyor...")

#Bütün foksiyonları dögülerle beraber çağırdığımız kısım.
def main_cagır(kullanici_adi):
    kontrol6=True
    while (kontrol6):
        kontrol7=True
        while (kontrol7):
            kontrol4=True
            while(kontrol4):
                secim=hizmetler()
                if secim==4:
                    kullanici_adi=oturum_kapat()
                if secim==5:
                    cikis_yap()
                    quit() #Quit fonksiyonu direkt olarak uygulamayı kapatıyor.
                kontrol8=True
                while (kontrol8):
                    kontrol8,kontrol4=urun_arama(secim,kullanici_adi)
                    kontrol4=sepet_git(secim,kullanici_adi)
                    satın_al(secim,kullanici_adi)
            kontrol6=sepet_alt_menu(secim,kullanici_adi)

#İsim girdilerini çağırıyoruz.
kullanici_adi=isim_girdileri()
#Ana fonksiyonumuzu çağırıyoruz.
main_cagır(kullanici_adi)