import json

class Node:
    def __init__(self, value, frequency, left, right):
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right


#Zählt die Häufigkeiten der txt Datei
def frequencys(filename):
    dict = {}
    file = open(filename,"r")

    while True:
        byte = file.read(1)
        
        if not byte: #EOF
            break

        else:
            try:
                dict[byte] += 1
            except:
                dict[byte] = 1

    file.close()
    return list(dict.items())


#findet das kleinste element(häufigkeit) in der node liste
def find_smallest(node_list):
    smallest = node_list[0]
    for node in node_list:
        if node.frequency < smallest.frequency:
            smallest = node
    return smallest


#erstellt den Huffman Baum
def build_tree(list_of_tuples):
    #liste vorbereiten#
    #Erstellt aus der tuple liste eine liste aus Node objekten
    tree_list = []
    for tuple in list_of_tuples:
        temp = Node(tuple[0],tuple[1],None,None)
        tree_list.append(temp)

    #erstellt den Tree wie nach der Vorlesung (Huffman)
    length = len(tree_list)
    while length != 1 :
        left = find_smallest(tree_list)
        tree_list.remove(left)
        right = find_smallest(tree_list)
        tree_list.remove(right)
        
        parent = Node( left.value + right.value , left.frequency + right.frequency ,left,right)
        tree_list.append(parent)
        length -=1

    return tree_list[0]


#Erstellt aus dem Huffman Baum eine Liste, welche später, als dict, verwendet wird für die Umwandlung 
def tree_to_huffman_list(node, code=""):
    if node.left == None and node.right == None:
        return [(node.value, code)]
    
    return tree_to_huffman_list(node.left, code + "1") + tree_to_huffman_list(node.right, code + "0")
    

#benutzt die vorigen funktionen um die Huffmankodierung auf eine Datei anzuwenden
def huffmann(filename, target_filename, huffmancode_filename):
    freq = frequencys(filename)
    tree = build_tree(freq)
    tree_dict = dict(tree_to_huffman_list(tree))

    file            = open(filename,"r")
    compressed_file = open(target_filename,"wb")
    code            = open(huffmancode_filename,"w")

    #Speichert den Huffmancode (dict)
    code.write(json.dumps(tree_dict))
    
    while True:
        byte = file.read(1)
        if not byte: #EOF
            break

        else:
            #''.join(map(str, tree_dict[byte])) => list to array. eg: [0,1,1] -> 001
            compressed_file.write(bytes(tree_dict[byte], 'utf-8') )

    code.close()    
    file.close()
    compressed_file.close()


#Hebt die Huffmancodierung auf
def decompress(filename, target_filename, huffmancode_filename): 

    file     = open(filename,"r")
    target_file = open(target_filename, "w")
    huffmancode_file = open(huffmancode_filename, "r")
    
    #lese den huffmancode ein
    huffmancode_str = huffmancode_file.read()
    huffmancode = json.loads(huffmancode_str)

    #reverse dict. eg: {"a" : "001"} -> {"001":a}
    reversecode = {v: k for k, v in list(huffmancode.items())}
    
    #gehe die compresed_file durch und decompress es
    temp = ""
    while True:
        byte = file.read(1)
        temp = temp+byte
        
        if not byte: #EOF
            break
        
        try: #if temp in huffmancode:
            target_file.write(reversecode[temp])
            temp = ""

        except: #else
            pass

    file.close()
    target_file.close()
    huffmancode_file.close()


huffmann("target.txt", "compressed.txt", "code.txt")
#decompress("compressed.txt","decomrpessed.txt", "code.txt")