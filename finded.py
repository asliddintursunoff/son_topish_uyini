# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:46:22 2022

son topish
"""
import random as r
def find():
    input("Biror son o'ylang \nboshlash uchun istalgan tugmani bosing: ")
    boshlanish=0
    tugash=10
    m=1
    while True:
        finded=r.randint(boshlanish,tugash)
        print(f"\nSiz tanlagan raqam {finded} \n \nUrinishlar soni {m} ta \n")
        abs=input("To'g'ri topdimmi yes/no: ".lower())
        if abs=="yes":
            print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
            print(f"\nTabriklaymiz siz {m} ta urinishda topdingiz! \n")
            break
        elif abs=="no":
            print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
            asd=input((f"\nSiz o'ylagan son katta/kichik mi?: "))
        if asd=="katta":
            boshlanish=finded+1
        else:
            tugash=finded-1
        m+=1


        

