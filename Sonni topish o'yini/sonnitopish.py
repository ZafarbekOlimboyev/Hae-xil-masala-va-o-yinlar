import random

def son_toping(son):
    """Bu funksiya foydalanuvchi o'yalagn sonni topadi"""
    oylangan_son = random.randint(1,son)
    print(f"Men 1 dan {son} gacha bo'lgan sonlardan birini o'yadim.Topa olasizmi?")
    urunishlar = 1
    while True:
        oylangan_son1 = int(input(">>"))
        if oylangan_son == oylangan_son1:
            x=input(f"TOPDINGIZ. {oylangan_son} sonini o'yagan edim. {urunishlar} taxminda topdingiz.Tabriklayman. \n1 dan {son} gacha son o'ylang. Men topishga harakat qilib ko'raman.\nAgar o'yalagan bo'lasngiz istalgan tugmani bosing")
            if x == True or x =="":
                topish(son,urunishlar)
                break
        elif oylangan_son > oylangan_son1:
            print("Xato men o'ylagan son bundan kattaroq. Yana kiritiib ko'ring: ")
            urunishlar += 1
        else:
            print("Xato men o'ylagan son bundan kichikroq. Yana kiritiib ko'ring: ")
            urunishlar += 1
def topish(son, urunishlar):
    """Bu funksiya orqali foydalanuvchi dastur o'yalagan sonni topadi."""
    urinishlar1 = 1
    n = 1
    while True:
        topish1 = random.randint(n, son)
        topdim = input(f"Siz {topish1} ni o'yladinggiz. To'g'ri bo'lsa (T),agar bundan kichikroq bo'lsa(-),Kattaroq bo'lsa (+) ni kiriting: ")
        if topdim == "T" or topdim == "t":
            if urunishlar < urinishlar1:
                print(f"Siz yutdingiz. Men {urinishlar1} ta taxmin bilan topdim siz esa {urunishlar} ta taxmin bilan topdinggiz.")
                yana = input("Yana o'ynaymizmi(Yes/No)?: ")
                if yana == "yes" or yana == "Yes":
                    son_toping(son)
                else:
                    break
            elif urinishlar1 < urunishlar:
                print(f"Men {urinishlar1} ta taxmin bilan topdim.")
                if urunishlar > urinishlar1:
                    print(
                        f"Men yutdim. Men {urinishlar1} ta taxmin bilan topdim siz esa {urunishlar} ta taxmin bilan topdinggiz.")
                    yana = input("Yana o'ynaymizmi(Yes/No)?: ")
                    if yana == "yes" or yana == "Yes":
                        son_toping(son)
                    else:
                        break
            else:
                print(f"Men {urinishlar1} ta taxmin bilan topdim.")
                if urunishlar == urinishlar1:
                    print(
                        f"Durrang. Men ham {urinishlar1} ta taxmin bilan topdim siz ham {urunishlar} ta taxmin bilan topdinggiz.")
                    yana = input("Yana o'ynaymizmi(Yes/No)?: ")
                    if yana == "yes" or yana == "Yes":
                        son_toping(son)
                    else:
                        break
        elif topdim == "-" :
            urinishlar1 += 1
            son = topish1 - 1
            n = 1
        else:
            urinishlar1 += 1
            n = topish1 + 1
            son =son
if __name__ == "__main__":
    son_toping(10)

