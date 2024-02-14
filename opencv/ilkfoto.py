# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

#image read resim okuma anlamında
resim = cv2.imread("regularshow.jpg")
#resim = cv2.imread("regularshow.jpg",0) 
#yukarıdaki kod resmi siyah beyaz yapar


#image show resmi göster anlamında
cv2.imshow("resim penceresi",resim)

plt.imshow(resim,cmap="gray")
plt.show()
#resmin opencv ile okunmuş hali çıkar
#koordinatlara ve rengine bakabilirsin
#kırmızıyı mavi olarak gösterir


k = cv2.waitKey(0)
#resim anlık olarak hızlı geldiğinden durduyoruz
#biz bir tuşa basana kadar resim gösterilir

if k == ord("q"):
    print("q tuşuna basıldı, resim kaydedildi.")
    cv2.imwrite("regularshowgri.jpg",resim)
    #grideyken q ya basarak çıktım ve kaydetti

cv2.destroyWindow("resim penceresi")
#resmi kapatır
#bütün resimleri kapamak için all ekle
#cv2.destroyAllWindow()
