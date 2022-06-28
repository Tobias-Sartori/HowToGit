import pandas as pd

AFC = pd.read_csv('AFC_Pic.csv',  sep=';')
NFC = pd.read_csv('NFC_Pic.csv',  sep=';')

print(f"\n\n")
print("American Football League")
print(AFC)

print(f"\n\n")
print("National Football League")
print(NFC)

print(AFC.head(7))
