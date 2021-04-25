# Turns a sequence of DNA into its respective RNA derivative
def rna(dna):

    # Reverse string and replace all T with U
    return dna[::-1].replace('T', 'U')

# Test
print(rna('CCTAGGACCAGGTT'))
