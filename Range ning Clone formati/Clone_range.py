def range_clone(son):
    """Bu range funksiyasini clonlangan varianti."""
    if len(son) == 3:
        start = son[0]
        stop = son[1]
        step = son[2]
    elif len(son) == 2:
        start = son[0]
        stop = son[1]
        step = 1
    elif len(son) == 1:
        start = 0
        stop = son[0]
        step = 1
    def clone(start,stop,step):
        sonlar=[]
        while stop>start:
            sonlar.append(start)
            start +=step
        return sonlar
    return (clone(start,stop,step))
n = list(map(int,input().split(",")))
#misol. pastda
for i in range_clone(n):
    print(i)