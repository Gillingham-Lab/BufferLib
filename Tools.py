import pickle

class unit_function:
    """dissolves floating and unit of inputs"""
    def mol(self):
        """dissolves molarity unit"""
        unit = ""
        if self >= 1:
            unit = "M"
            molarity = self
        if 1 > self >= 1e-3:
            molarity = self * 1e3
            unit = "mM"
        if 1e-3 > self >= 1e-6:
            molarity = self * 1e6
            unit = "uM"
        if 1e-6 > self >= 1e-9:
            molarity = self * 1e9
            unit = "nM"
        else:
            pass
        return molarity, unit

    def mass(self):
        unit = ""
        if self >= 1:
            unit = "g"
            mass = round(self, 2)
        if 1 > self >= 1e-3:
            unit = "mg"
            mass = int(round(self * 1e3, 0))
        return mass, unit

    def vol(self):
        unit = ""
        if self >= 1:
            unit = "L"
            volume = round(self, 2)
        if 1 > self >= 1e-3:
            unit = "mL"
            volume = round(self * 1e3, 2)
        if 1e-3 > self >= 1e-6:
            unit = "uL"
            volume = int(round(self * 1e6, 0))
        return volume, unit

class Buf:

    """Gives the buffer the storage, load and save with pickle"""

    def __init__(self, name, use, ingredients, molarity, unit, info):
         self.name = name
         self.use = use
         self.ingredients = ingredients
         self.molarity = molarity
         self.unit = unit
         self.info = info

    @staticmethod
    def load():
        """Loads the storage. one output as list of buffer class objects"""
        with open("Buffer.pickle", "rb") as f:
            buffer = pickle.load(f)
        return buffer

    def save(self):
        """Saves the bufferlist to a pickle file. self = name input"""
        with open("Buffer.pickle", "wb") as handle:
            pickle.dump(self, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def dic_to_list(self):
        BufferList = []
        for i, j in enumerate(self):
            self[i]["name"] = Buf(self[i]["name"], self[i]["use"], self[i]["ingredients"], self[i]["molarity"], self[i]["unit"], self[i]["info"])
            BufferList.append(self[i]["name"])
        return BufferList

    def list_to_dic(self):
        """converts list of chem typ objects to a list of dict"""
        BufferDic = []
        for i, j in enumerate(self):
            BufferDic.append(self[i].__dict__)
        return BufferDic

class Chemical:
    """Gives the chemicals the storage, load and save with pickle"""
    def __init__(self, name, mass, aggregation, density):
        self.name = name
        self.mass = mass
        self.aggregation = aggregation
        self.density = density

    def dic_to_list(self):
        """converts a dic in chem class format to list of class type objects"""
        ChemList = []
        for i, j in enumerate(self):
            self[i]["name"] = Chemical(self[i]["name"], self[i]["mass"], self[i]["aggregation"], self[i]["density"])
            ChemList.append(self[i]["name"])
        return ChemList

    def list_to_dic(self):
        """converts list of chem typ objects to a list of dict"""
        ChemDic = []
        for i, j in enumerate(self):
            ChemDic.append(self[i].__dict__)
        return ChemDic

    @staticmethod
    def load():
        """Loads the storage. one output as list of buffer class objects"""
        with open("Chemicals.pickle", "rb") as f:
            Chem = pickle.load(f)
        return Chem

    def save(self):
        """Saves the bufferlist to a pickle file. self = name input"""
        with open(f"Chemicals.pickle", "wb") as handle:
            pickle.dump(self, handle, protocol=pickle.HIGHEST_PROTOCOL)


def extract_unit(unit, amount):
    """extracts float and unit out data set. input Unit, amount. (Mol and %)"""
    if unit == "M":
        Amount = amount
        unit_data = "M"
    elif unit == "mM":
        Amount = float(amount) * 1e-3
        unit_data = "M"
    elif unit == "uM":
        Amount = float(amount) * 1e-6
        unit_data = "M"
    elif unit == "%":
        Amount = amount
        unit_data = "%"
    return Amount, unit_data












#-------------------- datatables

columns_recipe =            [
                            {"id": "number", "name": "Number"},
                            {"id": "chem", "name": "Chemical"},
                            {"id": "amount", "name": "Amount"},
                            ]

#--------------------  units
options_units_volume =      [
                            {"label": "L", "value" : 1},
                            {"label": "mL", "value" : 1e-3},
                            {"label": "uL", "value" : 1e-6},
                            ]

#-------------------- options menus

options_buffer =            [
                            {"label": "Protein Buffer", "value": "Protein"},
                            {"label": "DNA Buffer", "value": "DNA"},
                            {"label": "HPLC Buffer", "value": "HPLC"},
                            {"label": "Experiment Buffer", "value": "EXP"},
                            {"label": "Other Buffer", "value": "Other"},
                            ]

#--------------- infos

info_buffer =   [
                {"value": "Protein", "info": "Buffer that are used to run in vitro experiments with proteins"},
                {"value": "DNA", "info": "Buffer to work with DNA"},
                {"value": "HPLC", "info": "HPLC eluents etc."},
                {"value": "EXP", "info": "Buffers for experiments eg. Lysis etc"},
                {"value": "Other", "info": "Buffer that do not contain to anything else"},
]

#--------------- Editing

Col_Buffer = [
    {"id": "name", 'name': 'Chemical'},
    {"id": "use", 'name': 'Use'},
    {"id": "ingredients", 'name': 'Ingredients'},
    {"id": "molarity", 'name': 'Molarity'},
    {"id": "unit", 'name': 'unit'},
    {"id": "info", 'name': 'Information'},
    ]

Col_Chem = [
    {"id": "name", 'name': 'Chemical'},
    {"id": "mass", 'name': 'Molecular Mass'},
    {"id": "aggregation", 'name': 'Aggregation', "presentation": "dropdown"},
    {"id": "density", 'name': 'Density'},
    ]

Data_empty_recipe = [
    {"name": "", "amount": "", "unit": ""}
]

Data_empty = [
    {"name": "", "amount": "", "unit": "", "Molecular Mass": "", "aggregation": "", "density": ""}
]

Col_recipe = [
    {"id": "name", 'name': 'Chemical'},
    {"id": "amount", 'name': 'Concentration'},
    {"id": "unit", 'name': 'Unit', "presentation": "dropdown"},
    ]


Col = [
    {"id": "name", 'name': 'Chemical'},
    {"id": "amount", 'name': 'Concentration'},
    {"id": "unit", 'name': 'Unit', "presentation": "dropdown"},
    {"id": "mass", 'name': 'Molecular Mass'},
    {"id": "aggregation", 'name': 'Aggregation', "presentation": "dropdown"},
    {"id": "density", 'name': 'Density'},
    ]
