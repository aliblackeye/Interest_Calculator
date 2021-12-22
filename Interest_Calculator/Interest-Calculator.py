#Zamanlayıcı eklentisini programa dahil etmek için kullandığım "Time" kütüphanesi.
import time

#Ekrana programın adını yazıyoruz ve kullanıcıyı karşılıyoruz...
print("\n---------------------------------------------------")
print(".*.*.*.*FAIZ HESAPLAMA ARACINA HOSGELDINiZ*.*.*.*.")
print("---------------------------------------------------\n")

#Burada kullanıcıdan isim girdisi istiyoruz.
print("---------------------------------------------------")
print("Lütfen isminizi girer misiniz :  ")
print("---------------------------------------------------")
isim=str(input("\n"))

#Bu kısım programın kullanıcının isteğine göre tekrar etmesini sağlıyor.
key =True
while(key):

    #Burada kullanıcıyı tekrardan ismiyle beraber karşılıyoruz.
    print("\n---------------------------------------------------")
    print("                 Merhaba",isim,"!                     ")
    print("---------------------------------------------------\n")

    #3 saniyelik bir bekleme süresi. "Time.sleep" 0.5 olduğu için 3 saniyeyi daha kısa sürede geçiyor ve hoş bir görüntü katıyor.
    for i in range(3,0,-1): 
            time.sleep(0.5)
            print("İşleniyor...")

    #Kullanıcıdan kredi miktarı girdisini alıyoruz.
    print("\n---------------------------------------------------")
    print("Alacağın kredi miktarını girer misin",isim,":  ")
    print("---------------------------------------------------\n")
    kredi_miktari=int(input())

    #Daha sonra kullanıcıdan yıllık faiz oranı girdisini alıyoruz.        
    print("\n---------------------------------------------------")
    print("Yıllık faiz oranını girer misin",isim,":  ")
    print("---------------------------------------------------\n")
    yillik_faiz_orani=float(input())

    #Tekrardan zamanlayıcı.
    print("\n")
    for i in range(3,0,-1): 
            time.sleep(0.5)
            print("İşleniyor...")

    #Kullanıcıya teşekkür ediyoruz.
    print("\n---------------------------------------------------")
    print("Teşekkürler !")
    print("---------------------------------------------------")

    #Kullanıcıdan alacağı kredinin zaman girdisini kaydediyoruz.
    print("\n---------------------------------------------------")
    print("ZAMAN UZUNLUĞU ->>")
    print("     Yıl Olarak Kredi vadesi giriniz: ")
    kredi_vadesi_yil=int(input())
    print("     Ay Olarak Kredi vadesi giriniz: ")
    kredi_vadesi_ay=int(input())
    print("     Yineleme sayısı: ")
    yineleme=int(input())
    
    #Tekrardan zamanlayıcı.
    print("\n")   
    for i in range(3,0,-1): 
            time.sleep(0.5)
            print("Sonuçlar çıkartılıyor...")
    print("\n")       

    #"Ay" girdisi ile kullanıcıdan aldıgımız zaman girdisini "YİL" ve "AY" olarak ekrana basıyoruz.
    def print_duration(ay):
        yil=int(ay/12)
        kalan_ay=ay%12
        print("----------------------")
        print(yil,"YIL ",kalan_ay,"AY ")
        print("----------------------")

    #Para miktarını "Örneğin : 20000.0 $ , 100 $"olarak ayarlıyoruz.
    def print_money(para):
        noktali_para=format(para,".1f")
        print(noktali_para,"$")

    #Toplam faizi ana formül ile hesaplıyoruz. Toplam ödenecek tutar ile aylık ödenecek tutarı yeni bir girdiye kaydediyoruz.
    def print_entry(kredi_miktari,kredi_vadesi_ay,yillik_faiz_orani):
        
        toplam_faiz=(kredi_miktari/100)*(yillik_faiz_orani/12)*kredi_vadesi_ay
        
        odenecek_tutar = toplam_faiz + kredi_miktari
        
        aylik_odenecek_tutar=(odenecek_tutar/kredi_vadesi_ay)

    #Ekrana bu girdileri basıyoruz.       
        print("Toplam ödenecek para :")
        print_money(odenecek_tutar)
        print("Aylık ödenecek para :")
        print_money(aylik_odenecek_tutar)

    #Kullanıcının girdiği "YIL", "AY" ve "Yineleme" girdilerini fonksiyonlardan çağırıp ona göre ekrana kaç defa basılacağını ayarlıyoruz.
    def print_full_report (kredi_miktari,kredi_vadesi_ay,yillik_faiz_orani,yineleme,kredi_vadesi_yil):
            
            a=yineleme
            toplam_ay=kredi_vadesi_ay+kredi_vadesi_yil*12
            while(a<=toplam_ay):  
                print_duration(a)
                print_entry(kredi_miktari,a,yillik_faiz_orani)
                a=yineleme+a
                
                #Sonucları yavaş bir şekilde vermesi için tekrardan zamanlayıcı.
                for i in range(3,0,-1): 
                    time.sleep(0.5)
            
    #Fonksiyonları ve girdileri çağırıyoruz.            
    print_full_report (kredi_miktari,kredi_vadesi_ay,yillik_faiz_orani,yineleme,kredi_vadesi_yil)

    #Kullanıcıya teşekkür ediyoruz ve farklı bir işlem yapmak istiyor mu diye soruyoruz.
    print("----------------------")
    print("\n-------------------------------------------------------------------------------------")
    print("Yukarıda verdiğin kredi miktarına göre çıkan ödeme sonuçlarını inceleyebilirsin",isim)
    print("-------------------------------------------------------------------------------------")
    
    #Tekrardan zamanlayıcı.
    for i in range(5,0,-1): 
            time.sleep(1)
            print("Bekleniyor...")
    
    print("-------------------------------------------")
    print("Tekrar işlem yapmak ister misin ?")
    print("1-) EVET    2-) HAYIR")
    print("-------------------------------------------\n")
    secim=(input())
    
    #Kullanıcıya seçim yaptırıyoruz.
    if secim=="1" or secim=="evet" or secim=="Evet" or secim=="EVET":
        key=True
    
    else:
        key=False
        print("\n-------------------------------------------")
        print("Bizi tercih ettiğin için teşekkürler !!")
        print("-------------------------------------------\n")
        #Program ".exe" biçimindeyken kullanıcı hayır'ı seçerse, program aniden kapanmasın diye yazdığım komuttur.
        bos=input()