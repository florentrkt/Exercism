def to_rna(dna_strand):
    
    s=''

    for ctr in dna_strand :
        if ctr == 'G' :
            s+='C'
        if ctr == 'C' :
            s+='G'
        if ctr == 'T' :
            s+='A'
        if ctr == 'A' :
            s+='U'
        if ctr not in 'GCTA' :
            s=''
            return s

    return s
