a=input("Παρακαλώ δώστε την αλληλουχία RNA: ") #ζητάει από το χρήστη να εισάγει ακολουθία RNA
def validate_rna (rna_seq): #Συναρτηση για τον ελεγχο της εγκυρότητας της ακολουθίας
    seqm = rna_seq.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + seqm.count("U")
    if valid == len (seqm): return True
    else : return False

           
validate=validate_rna(str(a))
print("Η εγκυρότητα της ακολουθίας σας είναι: ", validate) # Εκτυπώνει με True False 


def frequency (seq): #Συναρτηση που ελέγχει πόσες C έχω 

    dic = {}
    for C in seq.upper():
        if C in dic: dic[C] += 1
        
        else : dic[C] = 1
    return dic
dict=frequency(str(a)) #Μου δίνει σε dictionary ολα τα αποτελέσματα
#print(dict)
res = {key: dict[key] for key in dict.keys() & {'C'}} 
print(str(res)) #Επιλέγω να εκτυπώσω μόνο το πλήθος των C

def gc_content (rna_seq): #Συνάρτηση που μετράει πόσα CG υπάρχουν στο RNA

    gc_count = 0
    for i in rna_seq:
        if i in "GCgc": gc_count += 1
    return gc_count
gc=gc_content(str(a))
print("Στην ακολουθία σας περιέχονται ", gc, "νουκλεοτίδια GC")
