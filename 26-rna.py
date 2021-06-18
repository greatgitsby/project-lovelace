STATE_MACHINE = {
    'U': {
        'U': {
            'U': 'Phe',
            'C': 'Phe',
            'A': 'Leu',
            'G': 'Leu'
        },
        'C': {
            'U': 'Ser',
            'C': 'Ser',
            'A': 'Ser',
            'G': 'Ser'
        },
        'A': {
            'U': 'Tyr',
            'C': 'Tyr',
            'A': None,
            'G': None
        },
        'G': {
            'U': 'Cys',
            'C': 'Cys',
            'A': None,
            'G': 'Trp'
        }
    },
    'C': {
        'U': {
            'U': 'Leu',
            'C': 'Leu',
            'A': 'Leu',
            'G': 'Leu'
        },
        'C': {
            'U': 'Pro',
            'C': 'Pro',
            'A': 'Pro',
            'G': 'Pro'
        },
        'A': {
            'U': 'His',
            'C': 'His',
            'A': 'Gln',
            'G': 'Gln'
        },
        'G': {
            'U': 'Arg',
            'C': 'Arg',
            'A': 'Arg',
            'G': 'Arg'
        }
    },
    'A': {
        'U': {
            'U': 'Ile',
            'C': 'Ile',
            'A': 'Ile',
            'G': 'Met'
        },
        'C': {
            'U': 'Thr',
            'C': 'Thr',
            'A': 'Thr',
            'G': 'Thr'
        },
        'A': {
            'U': 'Asn',
            'C': 'Asn',
            'A': 'Lys',
            'G': 'Lys'
        },
        'G': {
            'U': 'Ser',
            'C': 'Ser',
            'A': 'Arg',
            'G': 'Arg'
        }
    },
    'G': {
        'U': {
            'U': 'Val',
            'C': 'Val',
            'A': 'Val',
            'G': 'Val'
        },
        'C': {
            'U': 'Ala',
            'C': 'Ala',
            'A': 'Ala',
            'G': 'Ala'
        },
        'A': {
            'U': 'Asp',
            'C': 'Asp',
            'A': 'Glu',
            'G': 'Glu'
        },
        'G': {
            'U': 'Gly',
            'C': 'Gly',
            'A': 'Gly',
            'G': 'Gly'
        }
    }
}

# Translate an RNA sequence into a sequence of amino acids
def amino_acid_sequence(rna):
    curr_state = STATE_MACHINE
    sequence = ''

    # Iterate over each char of rna stream
    for i in range(len(rna)):

        # Get next state
        curr_state = curr_state[rna[i]]

        # Stop codon
        if curr_state is None:
            break

        # Normal amino acid final state
        elif isinstance(curr_state, str):

            # Add to sequence
            sequence += curr_state

            # Reset state machine to root
            curr_state = STATE_MACHINE

    return sequence

# Test
seq = "GCAAGAGAUAAUUGU"
print(seq, "=", amino_acid_sequence(seq))
