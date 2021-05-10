import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt
from Tools import Col_Buffer, Col_Chem, Data_empty_recipe, Data_empty, Col_recipe, Col

layout = html.Div(
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
                    style_cell={'textAlign': 'left'},
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
                    style_cell={'textAlign': 'left'},
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
                    style_cell={'textAlign': 'left'},
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
