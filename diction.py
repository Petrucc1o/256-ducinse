dict = {
    '1': ['sussybaka', 'amogus'],
    '2': ['algosidj', 'sdflksdfj'],
    '3': ['valr']
}

#for c in dict:
#    print(dict[c][0])

nddict = {
    'simba': {
        'sexo': 'macho',
        'cor': 'laranja',
        'idade': 10
    },
    'geisa': {
        'sexo': 'fêmea',
        'cor': 'tricolor',
        'idade': 30
    },
    'bituca': {
        'sexo': 'macho',
        'cor': 'marrom',
        'idade': 20
    }
}

#for c in nddict:
#    print(nddict[c])
    
simbow = {
    'petrvccio': {
        'simba': {
            'sexo': 'macho',
            'cor': 'laranja',
            'idade': 10
            }
        },
    'rosa': {
        'geisa': {
            'sexo': 'fêmea',
            'cor': 'tricolor',
            'idade': 30
            }
        },
    'marcos':{
        'bituca': {
            'sexo': 'macho',
            'cor': 'marrom',
            'idade': 20
        }
    }
}

#print(simbow)
#for c in simbow:
#    print(c)
#    print(simbow[c])

for a in simbow:
    if a != 'petrvccio':
        for c in simbow[a]:
            print(c)
            print(simbow[a])
    


            
#print(simbow['petrvccio'])


