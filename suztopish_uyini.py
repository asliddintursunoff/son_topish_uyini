print(f"*_*_*_*_*_*_*_*_*_*_*_*_*\n*   So'z topish o'yini  *\n*_*_*_*_*_*_*_*_*_*_*_*_*")
import random as r
from finded import find
def son_kirit():
    while True:
        
        choose_number=r.randint(0,10)
        print(f"Men uylgan son 0 dan 10 gacha. \n \nMen uylagan sonni toping \n")
        n=0
        while True:
            a=int(input("men uylagan sonni kiriting: "))
            n+=1
            if a==choose_number:
                print(f"tugri topdingiz, urinishlar soni {n} ta \n")
                find()
                break
            elif a>choose_number:
                print(f"Men uylagan son kichikroq , urinishlar soni {n} ta \n")
            else:
                    print(f"Men uylagan son kattaroq , urinishlar soni {n} ta \n")
     
        af=input("yana uynaysizmi: yes/no :".lower())
        if af=="no":
            break
son_kirit()  
                
                
            
    
