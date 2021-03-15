import pickle

Chem =                      [
                            {'name': 'BME', 'mass': 78.13, 'aggregation': 'liquid', 'density': 1.12},
                            {'name': 'Bis-Tris propane', 'mass': 282.34, 'aggregation': 'solid', 'density': 1},
                            {'name': 'DTT', 'mass': 154.25, 'aggregation': 'solid', 'density': 1},
                            {'name': 'EDTA', 'mass': 292.24, 'aggregation': 'solid', 'density': 1},
                            {'name': 'Glycerol', 'mass': 92, 'aggregation': 'liquid', 'density': 1.26},
                            {'name': 'NaCl', 'mass': 58.44, 'aggregation': 'solid', 'density': 1},
                            {'name': 'Tris', 'mass': 121.14, 'aggregation': 'solid', 'density': "1"},
                            ]



with open("Chemicals.pickle", "wb") as handle:
    pickle.dump(Chem, handle, protocol=pickle.HIGHEST_PROTOCOL)


print(leer)