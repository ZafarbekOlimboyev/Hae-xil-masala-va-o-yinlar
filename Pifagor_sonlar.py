def pifagor(n):
    """Bu funksiya pifagor sonlarini chiqarib beradi."""
    sonlar = []
    pifagor_sonlar = []
    for son in range (n):
        for i in range(son+1,n):
            for c in range (i+1,n):
                if son**2 + i**2 == c**2:
                    sonlar.append(son)
                    sonlar.append(i)
                    sonlar.append(c)
                    d = sonlar.copy()
                    pifagor_sonlar.append(d)
                    sonlar.clear()
    return pifagor_sonlar
if __name__ == "__main__":
    n =int(input())
    print(pifagor((n)))