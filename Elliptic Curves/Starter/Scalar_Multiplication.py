from Point_Addition import EC,Coord

if __name__=="__main__":
    ec=EC(497,1768,9739)
    P=Coord(x=2339, y=2213)
    print(ec.mul(P,7863))