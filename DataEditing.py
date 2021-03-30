import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table as dt
import pickle
import pandas as pd
from collections import OrderedDict


#print(Chem)
Password = "Gilli"


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

external_stylesheets = [dbc.themes.LUMEN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Buffer Update"
app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    #block1
    className="u-full-width",
    children=[
        dbc.Navbar([
                dbc.NavbarBrand("Test", className="ml-2")
            ],
            color="dark",
            dark=True,
        ),

        dbc.Container([
            html.Div(children=[

                html.Br(),

                html.H2("Add Buffer"),

                html.P("Check if Buffer isn't in the Library"),

                dbc.Row([

                    dbc.Col(width=6, children=[

                        dbc.Input(id="BufferName", placeholder="Name" ,value="", disabled=False, className="mt-3"),
                    ]),

                    dbc.Col(width=6, children=[

                        dbc.Button("Check", id="check", color="primary", block=True, className="mt-3", disabled=False),
                    ]),
                ]),

                html.Br(),

                html.H2(id="check_ok", children = ""),

                html.Br(),

                html.H4(id="NameNewBuffer", children=""),

                html.Br(),

                dbc.FormGroup(
                    [
                        dbc.Label("Chose Subfolder"),
                        dbc.RadioItems(
                            id="subfolder",
                            options= [
                                {"label": "Protein Buffer", "value": "Protein"},
                                {"label": "DNA Buffer", "value": "DNA"},
                                {"label": "HPLC Buffer", "value": "HPLC"},
                                {"label": "Experiment Buffer", "value": "EXP"},
                                {"label": "Other", "value": "Other"},
                            ],
                            value="",
                            inline=True,
                        ),
                    ]
                ),

                html.Br(),

                dt.DataTable(
                    id="table",
                    columns= Col,
                    data= Data_empty,
                    dropdown= {
                        'aggregation': {
                            'options': [
                                {"label": "Solid", "value": "solid"},
                                {"label": "Liquid", "value": "liquid"}
                            ],
                            "clearable": False
                        },
                        "unit": {
                            "options": [
                                {"label": "%", "value": "%"},
                                {"label": "M", "value": "M"},
                                {"label": "mM", "value": "mM"},
                                {"label": "uM", "value": "uM"},
                            ],
                            "clearable": False
                        },
                    },
                    editable=True,
                    row_deletable=True,
                    css=[{"selector": ".Select-menu-outer", "rule": "display: block !important"}],
                ),

                dbc.Button('Add Row', id='editing-rows-button', n_clicks=0, disabled=False),

                html.Br(),

                html.Br(),

                html.H4("Buffer Information"),

                dcc.Textarea(
                    id = "info_in",
                    value = "",
                    placeholder = "Enter information here",
                    style = {"width": "100%", "height": 100},
                    maxLength= "300",
                ),

                html.Br(),

                dbc.Button("Button", id="Button", color="primary", block=True, className="mt-3", disabled=False),

            ]),

            html.Br(),

            html.H3(id = "Output", children=[]),

            html.Br(),

            html.Hr(),

            html.Br(),

            html.H1(id="Recipe_Header", children="Recipe"),

            html.P(id= "Recipe_check",children="Please check if the Recipe is correct!"),

            html.H2(id= "NameCheck_recipe", children=""),

            html.H2(id= "UseCheck_recipe", children=""),

            html.Br(),

            dt.DataTable(
                    id="table_recipe",
                    columns= Col_recipe,
                    data= Data_empty_recipe,
            ),

            html.Br(),

            dcc.Textarea(
                id="info_show",
                value="",
                style={"width": "100%", "height": 100},
                maxLength="300",
                disabled= True,
            ),

            html.Br(),

            html.Br(),

            dbc.Row([

                    dbc.Col(width=6, children=[
                            dbc.FormGroup(
                                    [
                                        dbc.Label("I swear by the honor of my unborn futur pet, Jacky the guinea pig, that the Buffer Recipe is correct!"),
                                        dbc.RadioItems(
                                            id="swear",
                                            options= [
                                                {"label": "Yes", "value": "yes"},
                                                {"label": "No", "value": "no"},
                                            ],
                                            value="no",
                                            inline=True,
                                        ),
                                    ]
                            ),
                        ]),

                    dbc.Col(width=6, children=[
                            dbc.InputGroup(
                                        [
                                            dbc.Input(id="password_1", placeholder="**********", value="", type= "password"),
                                            dbc.InputGroupAddon("Password", addon_type="prepend"),
                                        ],
                                        className= "mb-3"
                                    ),
                    ]),
            ]),

            dbc.Button("Confirm", id="confirm", color="danger", block=True, className="mt-3", disabled=True),

            html.Br(),

            html.H2(id="success", children= ""),

            html.Hr(),

            html.Br(),

            html.H2("Edit Storage"),

            dcc.Dropdown(
                        id="show_buf_chem",
                        options=[{"label": "Buffer List", "value" : "buffer"},
                                 {"label": "Chemical List", "value" : "chem"},
                                 ],
                        value="",
                        placeholder="Select...",
                        className= " mb-3"
                    ),

            dbc.Button("Show", id="show_list", color="primary", block=True, className="mt-3", disabled=False),

            html.Br(),

            dt.DataTable(
                    id="table_edit",
                    columns= Col_Buffer,
                    data= [],
                    editable=True,
                    row_deletable=True,
                    css=[{"selector": ".Select-menu-outer", "rule": "display: block !important"}],
            ),

            html.Br(),

            html.Hr(),

            html.Br(),

            dbc.Row([

                dbc.Col(width=6, children=[
                    dbc.FormGroup(
                        [
                            dbc.Label(
                                "I swear by tomorrows lunch that the recipe is correct!"),
                            dbc.RadioItems(
                                id="swear_2",
                                options=[
                                    {"label": "Yes", "value": "yes"},
                                    {"label": "No", "value": "no"},
                                ],
                                value="no",
                                inline=True,
                            ),
                        ]
                    ),
                ]),

                dbc.Col(width=6, children=[
                    dbc.InputGroup(
                        [
                            dbc.Input(id="password_2", placeholder="**********", value="", type="password"),
                            dbc.InputGroupAddon("Password", addon_type="prepend"),
                        ],
                        className="mb-3"
                    ),
                ]),
            ]),

            dbc.Button("confirm", id="confirm_2", color="danger", block=True, className="mt-3", disabled=True),

            html.Br(),

            html.H2(id="saved_2", children= ""),

            html.Br(),

            html.Hr(),
        ]),
    ]
)

@app.callback(
    [
        Output("check_ok", "children"),
        Output("table", "editable"),
        Output("editing-rows-button", "disabled"),
        Output("Button", "disabled"),
        Output("NameNewBuffer", "children"),
    ],
        Input("check", "n_clicks"),
        State("BufferName", "value")
)
def Buffer_Check(n_clicks, BufferName):
    if not n_clicks:
        return "", False, True, True, ""

    with open("Buffer.pickle", "rb") as f:
        Buffer = pickle.load(f)

    BufferListed = {"name": [d['name'] for d in Buffer], "ingredients": [d['ingredients'] for d in Buffer],
                  "molarity": [d['molarity'] for d in Buffer], "unit": [d['unit'] for d in Buffer]}

    if BufferName in BufferListed["name"]:
        return "Buffer found", False, True, True, ""
    elif BufferName == "":
        return "Your Buffer needs a name!", False, True, True, ""
    else:
        return "Buffer not found", True, False, False, BufferName



@app.callback(
    Output('table', 'data'),
    Input('editing-rows-button', 'n_clicks'),
    State('table', 'data'),
    State('table', 'columns'))
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows

@app.callback(
    [
        Output("table_recipe", "data"),
        Output("table_recipe", "columns"),
        Output("Recipe_Header", "children"),
        Output("Recipe_check", "children"),
        Output("Output", "children"),
        Output("NameCheck_recipe", "children"),
        Output("UseCheck_recipe", "children"),
        Output("info_show", "value"),
    ],
        Input("Button", "n_clicks"),
        State("table", "data"),
        State("NameNewBuffer", "children"),
        State("subfolder", "value"),
        State("info_in","value"),
)
def control(n_clicks, data, NameNewBuffer, subfolder, info_in):

    global Col_recipe

    if not n_clicks:
        return [], Col_recipe, "", "", "", "", "", ""
    if n_clicks > 0:


        EmptyField = "No"
        for i in data:
            if i["name"] == "" or i["amount"] == "" or i['unit'] == "" or i['mass'] == "" or i['aggregation'] == "" or \
                    i['density'] == "" or subfolder == "":
                EmptyField = "Yes"

        if EmptyField == "Yes":
            return [], Col_recipe, "", "", "Please fill in all empty fields", "", "", ""
        if EmptyField == "No":
            return data, Col_recipe, "Recipe", "Please check if the Recipe is correct!", "Successful", f"Name: {NameNewBuffer}", f"Usage: {subfolder} Buffer", info_in


@app.callback(
        Output("success","children"),
        Input("confirm", "n_clicks"),
        State("table_recipe", "data"),
        State("table_recipe", "columns"),
        State("subfolder", "value"),
        State("NameNewBuffer", "children"),
        State("password_1", "value"),
        State("info_show", "value"),
)
def data(n_clicks, data, columns, subfolder, NameNewBuffer, password, info):
    global Password
    with open("Buffer.pickle", "rb") as f:
        Buffer = pickle.load(f)

    with open("Chemicals.pickle", "rb") as f:
        Chem = pickle.load(f)

    BufferListed = {"name": [d['name'] for d in Buffer], "use": [d['use'] for d in Buffer],
                    "ingredients": [d['ingredients'] for d in Buffer],
                    "molarity": [d['molarity'] for d in Buffer], "unit": [d['unit'] for d in Buffer], "info": [d['info'] for d in Buffer]}
    #print(BufferListed)
    #print(info)

    ChemListed = {"name": [d['name'] for d in Chem], "mass": [d['mass'] for d in Chem],
                  "aggregation": [d['aggregation'] for d in Chem], "density": [d['density'] for d in Chem]}

    #print(Chem)
    #print(Buffer)
    if not n_clicks:
        return ""
    if n_clicks > 0:
        if password == Password:
            if NameNewBuffer in BufferListed["name"]:
                return "Buffer already added"



            BufferListed["name"].append(NameNewBuffer)
            BufferListed["use"].append(subfolder)
            BufferListed["info"].append(info)

            ListNewIngredients = []
            ListNewMolarity = []
            ListNewUnit = []

            for i, j in enumerate(data):
                if data[i]["unit"] == "M":
                    Amount = data[i]["amount"]
                    unit_data = "M"
                elif data[i]["unit"] == "mM":
                    Amount = float(data[i]["amount"]) * 1e-3
                    unit_data = "M"
                elif data[i]["unit"] == "uM":
                    Amount = float(data[i]["amount"]) * 1e-6
                    unit_data = "M"
                elif data[i]["unit"] == "%":
                    Amount = data[i]["amount"]
                    unit_data = "%"


                if data[i]["name"] == "":
                    pass
                elif not data[i]["name"] in ChemListed["name"]:
                    ChemListed["name"].append(data[i]["name"])
                    ChemListed["mass"].append(float(data[i]["mass"]))
                    ChemListed["aggregation"].append(data[i]["aggregation"])
                    ChemListed["density"].append(float(data[i]["density"]))

                    ListNewIngredients.append(data[i]["name"])
                    ListNewMolarity.append(float(Amount))
                    ListNewUnit.append(unit_data)


                else:
                    ListNewIngredients.append(data[i]["name"])
                    ListNewMolarity.append(float(Amount))
                    ListNewUnit.append(unit_data)

            BufferListed["ingredients"].append(ListNewIngredients)
            BufferListed["molarity"].append(ListNewMolarity)
            BufferListed["unit"].append(ListNewUnit)

            Chem = [{"name": a, "mass": b, "aggregation": c, "density": d} for (a, b, c, d) in zip(ChemListed["name"], ChemListed["mass"], ChemListed["aggregation"], ChemListed["density"])]
            Buffer = [{"name": a, "use": b, "ingredients": c, "molarity": d, "unit": e, "info": f} for (a, b, c, d, e, f) in zip(BufferListed["name"], BufferListed["use"], BufferListed["ingredients"], BufferListed["molarity"], BufferListed["unit"], BufferListed["info"])]

            with open("Buffer.pickle", "wb") as handle:
                pickle.dump(Buffer, handle, protocol=pickle.HIGHEST_PROTOCOL)
            with open("Chemicals.pickle", "wb") as handle:
                pickle.dump(Chem, handle, protocol=pickle.HIGHEST_PROTOCOL)

            #print(Chem)
            #print(Buffer)
            return "Buffer Added!"
        else:
            return html.H2(style={"color":"red"}, id="success", children = "Wrong Password")


@app.callback(
    Output("confirm", "disabled"),
    Input("swear", "value"),
    State("Button", "n_clicks")
)
def swear_switch(swear, n_clicks):
    if not n_clicks:
        return True
    if swear == "yes":
        return False
    if swear == "no":
        return True

@app.callback(
    [
        Output("table_edit", "data"),
        Output("table_edit", "columns"),
    ],
        Input("show_list", "n_clicks"),
        State("show_buf_chem", "value"),
)
def show_content(n_clicks, chose):
    global Col_Buffer, Col_Chem

    if not n_clicks:
        return [], Col_Buffer

    if chose == "":
        return [], Col_Buffer
    if chose == "buffer":
        with open("Buffer.pickle", "rb") as f:
            Buffer = pickle.load(f)
            #print(Buffer)
        return Buffer, Col_Buffer
    if chose == "chem":
        with open("Chemicals.pickle", "rb") as f:
            Chem = pickle.load(f)
            #print(Chem)
        return Chem, Col_Chem

@app.callback(
        Output("confirm_2", "disabled"),
        Input("swear_2", "value"),
        State("show_list", "n_clicks")
)
def switch_delete(swear, n_clicks):
    if not n_clicks:
        return True
    if swear == "yes":
        return False
    if swear == "no":
        return True

@app.callback(
        Output("saved_2", "children"),
        Input("confirm_2", "n_clicks"),
        State("table_edit", "data"),
        State("table_edit", "columns"),
        State("password_2", "value"),
)
def save_changes(n_clicks, data, columns, password):
    global Col_Buffer, Col_Chem, Password

    if not n_clicks:
        return ""
    if password == Password:
        if columns == Col_Chem:
            with open("Chemicals.pickle", "wb") as handle:
                pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

        if columns == Col_Buffer:
            new_data = []
            for buffer in data:
                _buffer = {}

                for k, v in buffer.items():
                    if k in ["ingredients", "molarity", "unit"]:
                        if isinstance(v, str):
                            _buffer[k] = v.split(", ")
                        else:
                            _buffer[k] = v
                    else:
                        _buffer[k] = v

                new_data.append(_buffer)


            with open("Buffer.pickle", "wb") as handle:
                pickle.dump(new_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return "Update successful"
    else:
        return html.H2(style={"color":"red"}, id="save_2", children = "Wrong Password")

if __name__ == '__main__':
    app.run_server(debug=True)