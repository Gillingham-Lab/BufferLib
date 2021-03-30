import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table as dt
import pickle


external_stylesheets = [dbc.themes.LUMEN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Buffinator"
app.config.suppress_callback_exceptions = True

#-------------------- functions

def mol_unit_function(molarity):
    unit = ""
    if molarity >= 1:
        unit = "M"
    if 1 > molarity >= 1e-3:
        molarity = molarity * 1e3
        unit = "mM"
    if 1e-3 > molarity >= 1e-6:
        molarity = molarity * 1e6
        unit = "uM"
    if 1e-6 > molarity >= 1e-9:
        molarity = molarity * 1e9
        unit = "nM"
    return molarity, unit

def mass_unit_function(mass):
    unit = ""
    if mass >= 1:
        unit = "g"
        mass = round(mass, 2)
    if 1 > mass >= 1e-3:
        unit = "mg"
        mass = int(round(mass * 1e3, 0))
    return mass, unit

def vol_unit_function(volume):
    unit = ""
    if volume >= 1:
        unit = "L"
        volume = round(volume, 2)
    if 1 > volume >= 1e-3:
        unit = "mL"
        volume = round(volume * 1e3, 2)
    if 1e-3 > volume >= 1e-6:
        unit = "uL"
        volume = int(round(volume * 1e6, 0))
    return volume, unit

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

#--------------- layout



app.layout = html.Div(
    #block1
    className="u-full-width",
    children=[
        dbc.Navbar([
                dbc.NavbarBrand("Buffinator", className="ml-2")
            ],
            color="dark",
            dark=True,
        ),

        dbc.Container([
            html.Div(children=[

                html.Br(),

                html.P("One Day this will work!"),


            ]),

            html.Hr(),

            html.H1("Buffinator"),

            html.Br(),

            dbc.Row([

                dbc.Col(width=6, children=[

                    html.H2("Choose Buffer"),

                    html.Br(),

                    dbc.InputGroup(
                        [
                            dbc.Input(id="input-volume", value=50, disabled=False),

                            dbc.InputGroupAddon([
                                dcc.Dropdown(
                                    id="input-volume-unit",
                                    options= options_units_volume,
                                    value= 1e-3,
                                    className=" mb-3",
                                    disabled=False
                                )
                            ]),
                        ]
                    ),

                    dcc.Dropdown(
                        id="Buffer_options",
                        options= options_buffer,
                        placeholder= "Select...",
                        value= "",
                        className= "mb-3"
                    ),

                    dcc.Dropdown(
                        id="Buffer_under_options",
                        options= [],
                        value= "mgmt_1",
                        className= "mb-3"
                    ),


                    dbc.Button("Show Recipe", id="Show", color="primary", block=True, className="mt-3", disabled=False),

                    html.Br(),

                ]),



                dbc.Col(width=6, children=[

                    html.H2("Information"),

                    html.H4("Category Info"),

                    html.P(id="info_cat", children = "Choose category for information"),

                    html.H4("Buffer Info"),

                    html.P(id="info_Buf", children = ""),

                    html.Br(),

                ]),
            ]),



        html.Hr(),


        dbc.Row([

                dbc.Col(width=6, children=[

                    html.H2("Ingredients"),

                    html.Br(),

                    dt.DataTable(
                        id="show_ing",
                        columns=[],
                        data=[],
                    ),

                ]),

                dbc.Col(width=6, children=[

                    html.H2("Recipe"),

                    html.Br(),

                    dt.DataTable(
                        id="Recipe",
                        columns=[],
                        data=[],
                    ),
                ]),
            ]),
        ]),
    ]
)

#-------------------- options menu 1

@app.callback(
        [
    Output("Buffer_under_options", "options"),
    Output("info_cat", "children"),
        ],
    Input("Buffer_options", "value")
)
def menu_1(buffer):
    with open("Buffer.pickle", "rb") as f:
        Buffer = pickle.load(f)

    global info_buffer
    Protbuffer = []
    DNAbuffer = []
    HPLCbuffer = []
    ExpBuffer = []
    Otherbuffer = []

    for i, j in enumerate(Buffer):
        if Buffer[i]["use"] == "Protein":
            Protbuffer.append(Buffer[i]["name"])
        if Buffer[i]["use"] == "DNA":
            DNAbuffer.append(Buffer[i]["name"])
        if Buffer[i]["use"] == "HPLC":
            HPLCbuffer.append(Buffer[i]["name"])
        if Buffer[i]["use"] == "EXP":
            ExpBuffer.append(Buffer[i]["name"])
        if Buffer[i]["use"] == "Other":
            Otherbuffer.append(Buffer[i]["name"])

    Protbuffer = sorted(Protbuffer)
    DNAbuffer = sorted(DNAbuffer)
    HPLCbuffer = sorted(HPLCbuffer)
    Otherbuffer = sorted(Otherbuffer)
    ExpBuffer = sorted(ExpBuffer)

    options_Protbuffer = [
        {"label": i, "value": i}
        for i in Protbuffer]
    options_DNAbuffer = [
        {"label": i, "value": i}
        for i in DNAbuffer]
    options_HPLCbuffer = [
        {"label": i, "value": i}
        for i in HPLCbuffer]
    options_Expbuffer = [
        {"label": i, "value": i}
        for i in ExpBuffer]
    options_Otherbuffer = [
        {"label": i, "value": i}
        for i in Otherbuffer]


    if buffer == "Protein":
        for i, j in enumerate(info_buffer):
            if info_buffer[i]["value"] == "Protein":
                info = info_buffer[i]["info"]
        return options_Protbuffer, info
    elif buffer == "DNA":
        for i, j in enumerate(info_buffer):
            if info_buffer[i]["value"] == "DNA":
                info = info_buffer[i]["info"]
        return options_DNAbuffer, info
    elif buffer == "HPLC":
        for i, j in enumerate(info_buffer):
            if info_buffer[i]["value"] == "HPLC":
                info = info_buffer[i]["info"]
        return options_HPLCbuffer, info
    elif buffer == "EXP":
        for i, j in enumerate(info_buffer):
            if info_buffer[i]["value"] == "EXP":
                info = info_buffer[i]["info"]
        return options_Expbuffer, info
    elif buffer == "Other":
        for i, j in enumerate(info_buffer):
            if info_buffer[i]["value"] == "Other":
                info = info_buffer[i]["info"]
        return options_Otherbuffer, info
    else:
        return [], "Choose category for information"

#-------------------- show ing

@app.callback(
        Output("info_Buf", "children"),
        Input("Buffer_under_options", "value"),
)
def Buffer_info(chosen):
    with open("Buffer.pickle", "rb") as f:
        Buffer = pickle.load(f)
    for i, j in enumerate(Buffer):
        if Buffer[i]["name"] == chosen:
            return Buffer[i]["info"]



@app.callback(
    [
        Output("show_ing", "columns"),
        Output("show_ing", "data"),
    ],
        Input("Buffer_under_options", "value"),
        Input("input-volume-unit", "value"),
        Input("input-volume", "value"),
)
def table_ing(chosen, vol, vol_unit):

    global columns_ing

    with open("Buffer.pickle", "rb") as f:
        Buffer = pickle.load(f)
    print(Buffer)

    try:
        vol = float(vol) * float(vol_unit)
        max = 0
        table_ing = {"number": [], "chem": [], "amount": [], "unit": []}

        for i, l in enumerate(Buffer):
            if chosen == Buffer[i]["name"]:
                for j, k in enumerate(Buffer[i]["ingredients"]):
                    table_ing["number"].append(j + 1)
                    table_ing["chem"].append(Buffer[i]["ingredients"][j])

                    if Buffer[i]["unit"][j] == "M":
                        amount_ing, unit_ing = mol_unit_function(Buffer[i]["molarity"][j])
                    else:
                        unit_ing = Buffer[i]["unit"][j]
                        amount_ing = Buffer[i]["molarity"][j]



                    table_ing["amount"].append(amount_ing)
                    table_ing["unit"].append(unit_ing)
                    max += 1


        water, water_unit = vol_unit_function(vol)

        table_ing["number"].append(max + 1)
        table_ing["chem"].append("Total Volume")
        table_ing["amount"].append(water)
        table_ing["unit"].append(water_unit)

        data_ing = [{"number": a, "chem": b, "amount": f'{c} {d}'} for (a, b, c, d) in
                    zip(table_ing["number"], table_ing["chem"], table_ing["amount"], table_ing["unit"])]

        if data_ing[0]["chem"] == "Total Volume":
            return [], []
        else:
            return columns_recipe, data_ing

    except ValueError:
        return [], []


#-------------------- show recipe

@app.callback(
    [
        Output("Recipe", "columns"),
        Output("Recipe", "data"),
    ],
        Input("Show", "n_clicks"),
        State("Buffer_under_options", "value"),
        State("input-volume-unit", "value"),
        State("input-volume", "value"),
)
def table_recipe(n_clicks, chosen, vol, vol_unit):

    global columns_recipe

    with open("Chemicals.pickle", "rb") as f:
        Chem = pickle.load(f)

    with open("Buffer.pickle", "rb") as f:
        Buffer = pickle.load(f)

    try:
        vol = float(vol) * float(vol_unit)

        ing = {}
        Amount = {}

        if not n_clicks:
            return [], []

        for i, l in enumerate(Buffer):
            if chosen == Buffer[i]["name"]:
                for j, k in enumerate(Buffer[i]["ingredients"]):
                    ing[j] = {"name": Buffer[i]["ingredients"][j], "amount": Buffer[i]["molarity"][j],
                              "unit": Buffer[i]["unit"][j]}

        index = None
        unit = None

        table = {"number": [], "chem": [], "amount": [], "unit": []}

        for i in ing:
            for j, k in enumerate(Chem):
                if Chem[j]["name"] == ing[i]["name"]:
                    index = j

            if ing[i]["unit"] == "M":
                n = vol * ing[i]["amount"]
                mass = n * Chem[index]["mass"]

                if Chem[index]["aggregation"] == "solid":
                    result, unit = mass_unit_function(mass)

                if Chem[index]["aggregation"] == "liquid":
                    result = mass / Chem[index]["density"]
                    result, unit = vol_unit_function(result)

            if ing[i]["unit"] == "%":
                result = vol * ing[i]["amount"] * 0.01
                result, unit = vol_unit_function(result)


            table["number"].append(i + 1)
            table["chem"].append(ing[i]["name"])
            table["amount"].append(result)
            table["unit"].append(unit)

        total_vol = 0

        for j, i in enumerate(table["unit"]):
            if i == "L":
                total_vol = total_vol + table["amount"][j]
            if i == "mL":
                total_vol = total_vol + (table["amount"][j] * 1e-3)
            if i == "uL":
                total_vol = total_vol + (table["amount"][j] * 1e-6)

        #print(total_vol)

        water = vol - total_vol
        water, water_unit = vol_unit_function(water)

        table["number"].append("")
        table["chem"].append("Water")
        table["amount"].append(water)
        table["unit"].append(water_unit)


        data_recipe = [{"number": a, "chem": b, "amount": f'{c} {d}'} for (a, b, c, d) in
                zip(table["number"], table["chem"], table["amount"], table["unit"])]

        #print(data)


        return columns_recipe, data_recipe

    except ValueError:
        return columns_recipe, []


if __name__ == '__main__':
    app.run_server(debug=True)

