import pickle

Buffer = [
    {
        "name": "Mgmt Reaction Buffer",
        "use": "Protein",
        "ingredients": ["Tris", "Glycerol", "DTT", "EDTA"],
        "molarity": [50e-3, 5, 1e-3, 1e-3],
        "unit": ["M", "%", "M", "M"],
    },
    {
        "name": "Rad-52 Reaction Buffer",
        "use": "Protein",
        "ingredients": ["Bis-Tris propane", "NaCl", "BME"],
        "molarity": [25e-3, 200e-3, 2e-3],
        "unit": ["M", "M", "M"],
    },
    {
        'name': 'Ammonium Acetate 50mM',
        'use': 'HPLC',
        'ingredients': ['Ammonium Acetate'],
        'molarity': [0.05],
        'unit': ['M'],
    },
    {
        'name': 'KRAS (G12C) Running Buffer (PH 7.0, Marx et al)',
        'use': 'Protein',
        'ingredients': ['HEPES', 'NaCl', 'MgCl2', 'Octyl glucopyranoside', 'TCEP HCl'],
        'molarity': [0.025, 0.15, 0.005, 0.01, 0.0005],
        'unit': ['M', 'M', 'M', 'M', 'M'],
    },
    {
        'name': 'Tubulin Reaction Buffer (Ph 7.0, L.Chen et al, 2019)',
        'use': 'Protein',
        'ingredients': ['PIPES', 'EDTA', 'MgCl2', 'Na2GDP'],
        'molarity': [0.08, 0.0005, 0.002, 0.001],
        'unit': ['M', 'M', 'M', 'M'],
    },
]


BufferListed = {"name": [d['name'] for d in Buffer], "ingredients": [d['ingredients'] for d in Buffer],
                      "molarity": [d['molarity'] for d in Buffer], "unit": [d['unit'] for d in Buffer]}
print(Buffer)


with open("Buffer.pickle", "wb") as handle:
    pickle.dump(Buffer, handle, protocol=pickle.HIGHEST_PROTOCOL)

"""with open("Buffer.pickle", "rb") as f:
    Buffer = pickle.load(f)
print(Buffer)"""