class Knoten:
    def __init__(self, name, next, breitensuche_value):
        self.name = name
        self.next = next
        self.breitensuche_value = breitensuche_value

def create_graph():
    MZWK = Knoten("MZWK|",[],-1)
    WK = Knoten("WK|MZ",[],-1)
    MWK = Knoten("MWK|Z",[],-1)
    W = Knoten("W|MZK",[],-1)
    K = Knoten("K|MZW",[],-1)
    MZW = Knoten("MZW|K",[],-1)
    MZK = Knoten("MZK|W",[],-1)
    Z = Knoten("Z|MKW",[],-1)
    MZ = Knoten("MZ|WK",[],-1)
    none = Knoten("|MZWK",[],-1)

    #F steht für False, weil diese Wege nicht zum Ziel führen
    ZWK_F = Knoten("ZWK_F",[],-1)
    WZ_F = Knoten("WZ_F",[],-1)
    KZ_F = Knoten("KZ_F",[],-1)
    WK_F = Knoten("WK_F",[],-1)
    MK_F = Knoten("MK_F",[],-1)
    ZW_F = Knoten("ZW_F",[],-1)
    ZK_F = Knoten("ZK_F",[],-1)

    MZWK.next = [WK,ZWK_F,WZ_F,KZ_F]
    WK.next = [MZWK,MWK]
    MWK.next = [WK,W,K]
    W.next = [MWK,MZW,WK_F]
    K.next = [MWK,MZK,MK_F]
    MZW.next = [W,Z,ZW_F]
    MZK.next = [K,Z,ZK_F]
    Z.next = [MZW,MZK,MZ]
    MZ.next = [Z,none]
    none.next = [MZ]

    return MZWK


def breitensuche(graph):
    graph.breitensuche_value = 0
    temp = [graph]

    end = graph ##Important for findpath##

    while temp != []:
        #nehme ersten knoten
        knoten = temp[0]
        temp = temp[1:]
        print(knoten.name)
        for next in knoten.next:
            #makiere knoten, welche noch nicht makiert wurden und teste ihn danach (füge ihn in temp hinzu)
            if next.breitensuche_value == -1:
                next.breitensuche_value = knoten.breitensuche_value + 1
                temp = temp + [next]
                end = next ##Important for findpath##

    return end



def findpath (knoten):
    result = [knoten.name]
    n = end.breitensuche_value
    while n >= 1:
        for next in knoten.next:
            if next.breitensuche_value == knoten.breitensuche_value -1:
                result = [next.name] + result
                knoten = next
                n -= 1
                # . . . wäre auch möglich . . . 
                # n = next.breitensuche_value

    return result


graph = create_graph()
end = breitensuche(graph)
result = findpath(end)
print(result)