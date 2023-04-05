def check_duplicate_corner(resim, M, N, K):
    # Köşe için hash fonksiyonu
    def hash_kose(x, y):
        hash_degeri = 0
        for i in range(K):
            hash_degeri = (hash_degeri << 8) | resim[x+i][y+K-1]
        return hash_degeri
    
    # Üst satırın hareketli hash fonksiyonu için hash fonksiyonu
    def hash_ust_satir(x, y, onceki_hash):
        hash_degeri = onceki_hash
        for i in range(K):
            hash_degeri = ((hash_degeri << 8) & maske) | resim[x][y+i]
        return hash_degeri
    
    # Hash değerini maskelemek için önceden hesaplanmış maske
    maske = (1 << 8*K) - 1
    
    # Köşenin hash değerini hesapla
    kose_hash = hash_kose(0, N-K)
    
    # Üst satırın hash değerini hesapla
    ust_satir_hash = hash_ust_satir(0, N-K, 0)
    
    # Resmi tarayın
    for i in range(1, M-K+1):
        # Üst satırın hash değerini güncelle
        ust_satir_hash = hash_ust_satir(i, N-K, ust_satir_hash)
        
        # Köşe hash değerini üst satırın hash değeriyle karşılaştır
        if kose_hash == ust_satir_hash:
            # Köşenin gerçekten eşleşip eşleşmediğini kontrol et
            eslesme = True
            for j in range(K):
                if resim[0][N-K+j] != resim[i][N-K+j]:
                    eslesme = False
                    break
            if eslesme:
                return True
    
    # Eşleşme bulunamadıysa, False değerini döndür
    return False
