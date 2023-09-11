d
nemjo=True
while nemjo:
    szam_str=input("szam=")
if szam_str.isdecimal():
    nemjo=False
    szam=int(szam_str)

if szam <3:
    print('szam kisebb 3')
elif szam >3:
    print("szam nagy 3")