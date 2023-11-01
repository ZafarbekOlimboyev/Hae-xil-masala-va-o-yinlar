def murakkab_son(n = int):
    """Bu funksiya murakkab sonlarni topib beradi."""
    murakkab_sonlar =[]
    for i in range(4,n):
        s = 1
        for bolinuvchi in range(1,i//2+1):
            if i%bolinuvchi == 0:
                s+=1
            else:
                continue
        if s>=3:
            murakkab_sonlar.append(i)
        else:
            continue
    return murakkab_sonlar
if __name__ == "__main__":
    n = int(input("N ni kiriting: "))
    print(murakkab_son(n))