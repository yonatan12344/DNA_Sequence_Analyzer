def GC_Content(file):
    file = open(file, 'r')
    file.readline()
    DNA_String = file
    DNA_String = DNA_String.read().replace("\n", "")
    
    DNA_Length = len(DNA_String)
    GC_Content = (DNA_String.count('C') + DNA_String.count('G'))/ DNA_Length
    return (GC_Content * 100)
#print(GC_Content("DNA_Test_App.txt"))

def ATG_Count(file):
    file = open(file, 'r')
    file.readline()
    DNA_String = file
    DNA_String = DNA_String.read().replace("\n", "")
    print(DNA_String)
    n = len(DNA_String)
    k = len("ATG")
    kmer_dict = {}
    ATG_Count = 0
    for i in range(n-k+1):
        if "ATG" in DNA_String[i:i+k]:
                ATG_Count += 1
            
            
    return(ATG_Count)
print(ATG_Count("DNA_Test_App.txt"))
