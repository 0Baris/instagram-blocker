# Instagram Blocker

Instagram'da toplu engelleme yapmanızı sağlayan basit bir Python uygulaması.
[Click here for English](README_EN.MD)

## İçindekiler
- [Instagram Blocker](#instagram-blocker)
  - [İçindekiler](#i̇çindekiler)
  - [Kurulum](#kurulum)
  - [Önemli Notlar](#önemli-notlar)
  - [Kullanım](#kullanım)
  - [Güvenlik](#güvenlik)
  - [Geliştirici Notları](#geliştirici-notları)
    - [Gereksinimler](#gereksinimler)
    - [Kurulum](#kurulum-1)
    - [Katkıda Bulunma](#katkıda-bulunma)
  - [Hata Bildirimi](#hata-bildirimi)
  - [Lisans](#lisans)

## Kurulum

1. [Releases](https://github.com/0baris/instagram-blocker/releases) sayfasından en son sürümü indirin
2. İndirdiğiniz .zip dosyasını çıkartın
3. `block_list.txt` dosyasını açın ve engellemek istediğiniz hesapları her satıra bir tane gelecek şekilde yazın
4. `instagram-blocker.exe` dosyasını çalıştırın

## Önemli Notlar

- Program çalışmadan önce Instagram hesabınızda 2 Faktörlü Doğrulamayı geçici olarak kapatmanız gerekmektedir
- Tek seferde 100'den fazla hesap engellemeyi denemeyin
- 100 hesap engelledikten sonra yaklaşık 3-3.5 saat bekleyin
- Tüm kodları inceleyebilirsiniz, hesabınız için herhangi bir risk oluşturmaz

## Kullanım

1. Programı çalıştırın
2. Instagram kullanıcı adı ve şifrenizi girin
3. Program otomatik olarak `block_list.txt` içindeki hesapları engellemeye başlayacaktır

## Güvenlik

- Kullanıcı adı ve şifreniz sadece Instagram'a giriş yapmak için kullanılır
- Hiçbir veri saklanmaz veya üçüncü taraflarla paylaşılmaz
- Tüm işlemler yerel bilgisayarınızda gerçekleşir

## Geliştirici Notları

### Gereksinimler
- [Python 3.8+](https://www.python.org/downloads/)

### Kurulum
```bash
# Repository'yi klonlayın
git clone https://github.com/0baris/instagram-blocker.git

# Gerekli paketleri yükleyin
pip install -r requirements.txt

# Programı başlatın
python main.py
```

### Katkıda Bulunma
1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Açıklama'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun
   
## Hata Bildirimi

Herhangi bir hata veya sorunla karşılaşırsanız, GitHub üzerinden issue açabilirsiniz.

## Lisans

MIT License