# Dieses Programm berechnet die perfekten Zutanten für ein Eis
# für die Eismaschine mit Dr. Almonds Eiscremezauber
# DrITCodEr by 27th June

print("**************************************************************************************\n")
print("            * E * I * S * * * K * A * L * K * U * L * A * T * O * R * ! * \n")
print("**************************************************************************************\n")

Sorte = int(input("Welche Sorte Eis möchtest Du zubereiten?\n\nVanille  = 1\nSchoko   = 2\nErdbeere = 3\n\n"))

if Sorte == 1:
    print("\nDu magst also Vanille, ich auch ;-)\n\n")
    MengeEis = int(input("\n Wieviel Vanille Eis (in g) möchtest Du zubereiten? "))
    MengeEiscremezauber = MengeEis // 6
    MengeSahne = MengeEis // 2
    MengeWasser = MengeEis // 3
    print("\n Für %d g Vanille Eis benötigst Du: \n\n %d g Eiscremezauber \n %d g flüssige Sahne und\n %d g Wasser.\n\n Guten Appetit!" % (MengeEis, MengeEiscremezauber, MengeSahne, MengeWasser))
elif Sorte == 2:
    print("\nDu magst also Schoko … hmmm … ich auch ;-)  \n\n")
    MengeEis = int(input("\n Wieviel Schoko Eis (in g) möchtest Du zubereiten? "))
    MengeEiscremezauber = MengeEis * 100 // 580
    MengeSahne = MengeEis * 250 // 580
    MengeWasser = MengeEis * 200 // 580
    MengeKakao = MengeEis * 30 // 580
    print("\n Für %d g Schoko Eis benötigst Du: \n\n %d g Eiscremezauber \n %d g flüssige Sahne\n %d g Wasser und\n %d g Kakao Pulver.\n\n Guten Appetit!" % (MengeEis, MengeEiscremezauber, MengeSahne, MengeWasser, MengeKakao))
elif Sorte == 3:
    print("\nDu magst also Erbeere. Na klar, ich sowieso ;-) \n\n")
    MengeEis = int(input("\n Wieviel Erdbeer Eis (in g) möchtest Du zubereiten? "))
    MengeEiscremezauber = MengeEis * 100 // 700
    MengeSahne = MengeEis * 300 // 700
    MengeErdbeer = MengeEis * 300 // 700
    print("\n Für %d g Erdbeer Eis benötigst Du: \n\n %d g Eiscremezauber \n %d g flüssige Sahne und\n")
    
