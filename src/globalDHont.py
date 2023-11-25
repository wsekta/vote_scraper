results = [
    {"name": "KOMITET WYBORCZY PRAWO I SPRAWIEDLIWOŚĆ", "votes": 7640854, "divisor": 1, "deputy": 0},
    {"name": "KOALICYJNY KOMITET WYBORCZY KOALICJA OBYWATELSKA PO .N IPL ZIELONI", "votes": 6629402, "divisor": 1, "deputy": 0},
    {"name": "KOALICYJNY KOMITET WYBORCZY TRZECIA DROGA POLSKA 2050SZYMONA HOŁOWNI - POLSKIE STRONNICTWO LUDOWE", "votes": 3110670, "divisor": 1, "deputy": 0},
    {"name": "KOMITET WYBORCZY NOWA LEWICA", "votes": 1859018, "divisor": 1, "deputy": 0},
    {"name": "KOMITET WYBORCZY KONFEDERACJA WOLNOŚĆ I NIEPODLEGŁOŚĆ", "votes": 1547364, "divisor": 1, "deputy": 0},
    {"name": "KOMITET WYBORCZY BEZPARTYJNI SAMORZĄDOWCY", "votes": 401054, "divisor": 1, "deputy": 0},
    {"name": "KOMITET WYBORCZY POLSKA JEST JEDNA", "votes": 351099, "divisor": 1, "deputy": 0},
    {"name": "KOMITET WYBORCZY WYBORCÓW MNIEJSZOŚĆ NIEMIECKA", "votes": 25778, "divisor": 1, "deputy": 0},
    {"name": "KOMITET WYBORCZY WYBORCÓW RUCHU DOBROBYTU I POKOJU", "votes": 24850, "divisor": 1, "deputy": 0},
    {"name": "KOMITET WYBORCZY NORMALNY KRAJ", "votes": 4606, "divisor": 1, "deputy": 0},
    {"name": "KOMITET WYBORCZY ANTYPARTIA", "votes": 1156, "divisor": 1, "deputy": 0},
    {"name": "KOMITET WYBORCZY RUCH NAPRAWY POLSKI", "votes": 823, "divisor": 1, "deputy": 0}
]

for party in results:
    party["divisor_sl"] = party["divisor"]
    party["deputy_sl"] = party["deputy"]
    party["divisor_dh"] = party["divisor"]
    party["deputy_dh"] = party["deputy"]


overall = 0
for party in results:
    overall += party["votes"]
print(f"overal votes {overall}")

for method in ["_sl", "_dh"]:
    print(f"METHOD {'dHont' if method == '_dh' else 'Sainte-Laguë'}")
    for i in range(460):
        max_score = 0
        max_party = None
        for party in results:
            score = party["votes"] / party["divisor" + method]
            if(score > max_score):
                max_party = party
                max_score = score
        
        max_party["divisor"+ method] += 1 if method == "_dh" else 2
        max_party["deputy" + method] += 1
        if(i == 459):
            print(f"Lesser score has party in method {method} {max_party['name']} with score {max_score}")

    sumary_percent_different = 0
    for party in results:
        party["percent votes"] = party["votes"] / overall * 100
        party["percent_deputy" + method] = party["deputy" + method] / 4.6
        sumary_percent_different += abs(party["percent votes"] - party["percent_deputy" + method])
    print(f"Overall percent different between percent of votes and percent of deputy "
          f"in method {'dHont' if method == '_dh' else 'Sainte-Laguë'} is {sumary_percent_different:2.2f}")

    for party in results:
        if(party["deputy" + method] == 0):
            break

        print(f"\t{party['name']}:\n\t\t"
            f"{party['deputy' + method]} which is {party['percent_deputy' + method]:2.2f}% of deputies "
            f"with {party['votes']} votes which is {party['percent votes']:2.2f}% of all votes")