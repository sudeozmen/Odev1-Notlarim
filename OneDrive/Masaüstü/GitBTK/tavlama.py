import numpy as np

def simann(a, us, d, delta, T, Tend, sk):
    
    #rastgele bir çözüm üretilir ve amaç fonk hesaplanır.
    cozum = np.random.uniform(a, us, d)
    obj = np.sum(cozum ** 2)
    iterasyon = 1
    objit = [obj]
    objeniyi = obj
    cozumeniyi = np.copy(cozum)


    while T > Tend:
        #rastgele değişim miktarı oluşturularak cozumle toplanır ve komsuluk bulunur.
        degisim_miktari = np.random.uniform(-(us - a) * delta / 2, (us - a) * delta / 2, d)
        komsu = cozum + degisim_miktari
        obj_komsu = np.sum(komsu ** 2)

        #komsunun amaç fonk daha iyiyse yeni çözüm kabul edilir.
        if obj_komsu <= obj:
            cozum = komsu
            obj = obj_komsu

        #komşunun amaç fonk daha iyi değilse kabul olasılığına bakılır sağlıyorsa yeni çözüm kabul edilir. 
        else:
            de = obj_komsu - obj
            pa = np.exp(-de / T)
            rs = np.random.uniform(0, 1)
            if rs < pa:
                cozum = komsu
                obj = obj_komsu

        T = T * sk
        iterasyon += 1

        while len(objit) <= iterasyon:
            objit.append(obj)

        if objit[iterasyon] < objeniyi:
            cozumeniyi = np.copy(cozum)
            objeniyi = obj

    return cozumeniyi, objeniyi, iterasyon, objit

a = -5
us = 5
d = 3
delta = 0.5
T = 100
Tend = 75
sk = 0.9
cozumeniyi, objeniyi, iterasyon, objit = simann(a, us, d, delta, T, Tend, sk)
print("En iyi çözüm:", cozumeniyi)
print("En iyi objektif değeri:", objeniyi)
print("Toplam iterasyon sayısı:", iterasyon)
