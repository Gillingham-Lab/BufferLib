import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt
from Tools import unit_function, Buf, Chemical, columns_recipe, options_units_volume, options_buffer, info_buffer



layout = html.Div(
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

                html.P("The day has come: it works!"),


            ]),

            html.Hr(),

            html.H1("Buffer Library"),

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
                        value= "",
                        className= "mb-3"
                    ),


                    dbc.Button("Show Recipe", id="Show", color="primary", block=True, className="mt-3", disabled=False),

                    html.Br(),

                ]),



                dbc.Col(width=6, children=[

                    html.H2("Information"),

                    html.Br(),

                    html.H4("Category Information"),

                    dcc.Textarea(
                        id="info_cat",
                        value="",
                        style={"width": "100%", "height": 50},
                        disabled=True,
                        placeholder=""
                    ),

                    html.Br(),

                    html.Br(),

                    html.H4("Buffer Information"),

                    dcc.Textarea(
                        id="info_Buf",
                        value="",
                        style={"width": "100%", "height": 50},
                        disabled=True,
                        placeholder= ""
                    ),

                    html.Br(),

                ]),
            ]),



        html.Hr(),


        dbc.Row([

                dbc.Col(width=6, children=[

                    html.H2(id="header_ingredients", children = ""),

                    html.Br(),

                    html.P(id="ingredients_Buffername", children=""),

                    html.Br(),

                    dt.DataTable(
                        id="show_ing",
                        columns=[],
                        data=[],
                        style_cell={'textAlign': 'center'},

                    ),

                ]),

                dbc.Col(width=6, children=[

                    html.H2(id= "header_Recipe", children=""),

                    html.Br(),

                    html.P(id="Recipe_Buffername", children = ""),

                    html.Br(),

                    dt.DataTable(
                        id="Recipe",
                        columns=[],
                        data=[],
                        style_cell={'textAlign': 'center'},
                    ),
                ]),
            ]),

            html.Hr(),

        ]),
    ]
)
