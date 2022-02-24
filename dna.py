# def DNA_strand(dna):
#     # code here
#     reverse = ''
#     for i in range(0, len(dna)):
#         if dna[i] == 'A':
#             reverse += 'T'
#         elif dna[i] == 'T':
#             reverse += 'A'
#         elif dna[i] == 'C':
#             reverse += 'G'
#         elif dna[i] == 'G':
#             reverse += 'C'
#         else:
#             reverse += ''
#     return reverse

def DNA_strand(dna):
    # code here
    dnaComplement=""
    for string in dna:
        if string=="A":
            dnaComplement+="T"
        elif string =="T":
            dnaComplement+="A"
        elif string =="G":
            dnaComplement+="C"
        elif string == "C":
            dnaComplement+="G"
    return dnaComplement

print(DNA_strand('AAAA'))