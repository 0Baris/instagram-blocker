from utils.blocker import block_accounts, get_block_list_from_file

if __name__ == "__main__":
    print("""
          
            INSTAGRAM BLOCKER

*** 2 Faktörlü doğrulamayı kaldırmadan bu programı başlatamazsınız, işlem bittikten sonra tekrar açabilirsiniz. ***

* Tüm kodları inceleyebilirsiniz hesabınız için herhangi bir sorun teşkil etmez.

* Lütfen tek engelleme adımında 100 hesabı geçmeyin.

** 100 tane hesabı engellediyseniz tahmini 3-3.5 saat sonra yeni bir liste ile tekrar başlatabilirsiniz **
          """)
    
    username = input("Instagram Kullanıcı Adı: ")
    while True:
        password = input("Instagram Şifre: ")
        password_verify = input("Instagram Şifre (Tekrar): ")
        
        if password == password_verify:
            break
        else:
            print("Şifreler eşleşmiyor. Tekrar deneyin.")

    block_list = get_block_list_from_file()
    if block_list:
        block_accounts(username, password, block_list)
    else:
        print("Engellenecek hesap listesi boş, listeyi doldurun!")