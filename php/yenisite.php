<!DOCTYPE html>
<html>

    <head>

    </head>

    <body>

        <?php 
    
            // echo "echo kullanımı";
            // print("Print kullanımı");
            // printf("Printf kullanımı");

            // phpinfo(); #Kullanılan php versiyonu hakkında bilgi verir.

            //# Değişken Tanımlamaları
            // $degisken = 1;
            // echo $degisken;

            #-----------------------------------------------------------------

            // $okul = "İstinye Üniversitesi";
            // $okul1 = "$okul Bilgisayar Programcılığı";

            // echo $okul1;
            
            // $okul2 = 'İstinye Üniversitesi';
            // $okul3 = '$okul2 Bilgisayar Programcılığı'

            // echo $okul3;

            #-----------------------------------------------------------------

            // echo pi();

            // #Sabit Değişken
            // define("degisken",1); #Sabit değişken tanımlar
            // echo degisken;

            // $x = 3;
            // echo gettype($x); #Değişkenin tipini gösterir
            // echo "<br>";
            // var_dump($x);

            // $x = 45;
            // settype($x,"string"); #Değişkenin tipini değiştirir
            // print("türü:".gettype($x));

            // $x = 45;
            // echo $x;
            // unset($x); #Değişkeni hafızadan siler
            // echo $x;

            #-----------------------------------------------------------------

            // $t = "a";

            // if (empty($t)) {
            //     echo "İçerik Yok";
            // }
            // else{
            //     echo "İçerik Var";
            // }

            #-----------------------------------------------------------------

            // $t = "  a     ";
            // echo trim($t); #Sağ ve soldan boşluk siler
            // echo "metin";

            // $t = "  a     ";
            // echo rtrim($t); #Sağdan boşluk siler
            // echo "metin";

            // $t = "  a     ";
            // echo ltrim($t); #soldan boşluk siler
            // echo "metin";

            //$ad = "Ali";
            //$soyad = "Karagöz";
            //$adsoyad =$ad.$soyad;

            #-----------------------------------------------------------------
            
            // $degisken = "DEGISKEN";
            // $degisken2 = "DEĞİŞKEN";
            // echo strtolower($degisken);
            // echo mb_strtolower($degisken2,'utf-8');

            #-----------------------------------------------------------------

            // $degisken = "DEGISKEN";
            // $degisken2 = "DEĞİŞKEN";
            // echo strtoupper($degisken);
            // echo mb_strtoupper($degisken2,'utf-8');

            #-----------------------------------------------------------------

            // ucfirst() #İlk karakteri büyütür
            // ucwords() #Tüm kelimelerin baş harfini büyütür
            //$metin = "çerezleri kullanmak Birçok Konuda fayda sağlar.";
            //echo mb_convert_case($metin, MB_CASE_UPPER,"UTF-8");
            //echo mb_convert_case($metin, MB_CASE_LOWER,"UTF-8");
            //echo mb_convert_case($metin, MB_CASE_TITLE,"UTF-8"); 

            #-----------------------------------------------------------------

            //$metin = "çerezleri kullanmak Birçok Konuda fayda sağlar.";
            //explode(" ",$metin);
            //print_r($metin)

            //$dizi = array("çerezleri","kullanmak","Birçok","Konuda","fayda","sağlar");
            //echo implode($dizi);
            //echo implode(" ",$dizi);

            #-----------------------------------------------------------------

            // isset() #Değişken hafızada tanımlı mı değil mi ? TRUE-FALSE
            //str_word_count()
            //addcslashes($metin,'M')
            //chr() girilen değerin ascii kodunu verir
            //ord() chr fonksiyonunun tersini yapar
            //nl2br() Nl2br satırlardaki boşluklarla birlikte metni yazdırır.
            //str_repeat()
            //str_replace()
            //strcasecmp() kıyaslama

            //Tek Çift Sayı Kontrolü
            $sayi = 1;
            if($sayi % 2 == 0){echo "Sayi Çifttir";}
            else{echo "Sayi Tektir";}

            echo "<br>";

            if($sayi > 0){echo "Sifirdan buyuktur";}
            else{echo "Sifirdan kucuktur";}

            echo "<br>";

            $secim = FALSE;

            $secim == TRUE ? 'Üye Girişi Başarılı' : 'Üye Girişi Başarısız';
            echo $secim;

            



        ?>

    </body>

</html>