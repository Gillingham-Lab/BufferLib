import pickle

Buffer =                    [
                            {"name": "Mgmt Reaction Buffer",
                             "use": "Protein",
                              "ingredients": ["Tris", "Glycerol", "DTT", "EDTA"],
                              "molarity": [50e-3, 5, 1e-3, 1e-3],
                              "unit": ["M", "%", "M", "M"],
                            },
                            {"name": "Rad-52 Reaction Buffer",
                             "use": "Protein",
                              "ingredients": ["Bis-Tris propane", "NaCl", "BME"],
                              "molarity": [25e-3, 200e-3, 2e-3],
                              "unit": ["M", "M", "M"],
                            },

                            ]


BufferListed = {"name": [d['name'] for d in Buffer], "ingredients": [d['ingredients'] for d in Buffer],
                      "molarity": [d['molarity'] for d in Buffer], "unit": [d['unit'] for d in Buffer]}
#print(BufferListed)


with open("Buffer.pickle", "wb") as handle:
    pickle.dump(Buffer, handle, protocol=pickle.HIGHEST_PROTOCOL)