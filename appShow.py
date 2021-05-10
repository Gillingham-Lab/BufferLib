import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from Tools import unit_function, Buf, Chemical, columns_recipe, options_units_volume, options_buffer, info_buffer
from LayoutShow import layout


external_stylesheets = [dbc.themes.LUMEN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Buffinator"
app.config.suppress_callback_exceptions = True
app.layout = layout

#-------------------- options menu 1

@app.callback(
        [
    Output("Buffer_under_options", "options"),
    Output("info_cat", "value"),
        ],
    Input("Buffer_options", "value")
)
def menu_1(buffer):
    Buffer = Buf.load()
    global info_buffer
    options_buffer = []

    for x in ["Protein", "DNA", "HPLC", "EXP", "Other"]:
        if buffer == x:
            for i, j in enumerate(info_buffer):
                if info_buffer[i]["value"] == x:
                    info = info_buffer[i]["info"]
            for k, l in enumerate(Buffer):
                if Buffer[k].use == x:
                    options_buffer.append(Buffer[k].name)
            options_buffer = [
                {"label": i, "value": i}
                for i in sorted(options_buffer)]
            return options_buffer, info
    else:
        return [], ""

#-------------------- show ing

@app.callback(
        Output("info_Buf", "value"),
        Input("Buffer_under_options", "value"),
        Input("Buffer_options", "value"),
)
def Buffer_info(chosen, uper_chosen):
    Buffer = Buf.load()

    for i, j in enumerate(Buffer):
        if Buffer[i].name == chosen:
            if Buffer[i].use == uper_chosen:
                return Buffer[i].info
            else:
                return ""

@app.callback(
    [
        Output("show_ing", "columns"),
        Output("show_ing", "data"),
        Output("header_ingredients", "children"),
        Output("ingredients_Buffername", "children"),
        Output("Show", "n_clicks")
    ],
        Input("Buffer_under_options", "value"),
        Input("input-volume-unit", "value"),
        Input("input-volume", "value"),
)
def table_ing(chosen, vol, vol_unit):

    global columns_ing
    Buffer = Buf.load()

    try:
        vol = float(vol) * float(vol_unit)
        water, water_unit = unit_function.vol(vol)
        table_ing = {"number": [], "chem": [], "amount": [], "unit": []}

        for i, l in enumerate(Buffer):
            if chosen == Buffer[i].name:
                for j, k in enumerate(Buffer[i].ingredients):
                    if Buffer[i].unit[j] == "M":
                        amount_ing, unit_ing = unit_function.mol(Buffer[i].molarity[j])
                    else:
                        unit_ing = Buffer[i].unit[j]
                        amount_ing = Buffer[i].molarity[j]

                    table_ing["amount"].append(amount_ing)
                    table_ing["unit"].append(unit_ing)
                    table_ing["number"].append(j + 1)
                    table_ing["chem"].append(Buffer[i].ingredients[j])

        table_ing["number"].append("")
        table_ing["chem"].append("Total Volume")
        table_ing["amount"].append(water)
        table_ing["unit"].append(water_unit)

        data_ing = [{"number": a, "chem": b, "amount": f'{c} {d}'} for (a, b, c, d) in
                    zip(table_ing["number"], table_ing["chem"], table_ing["amount"], table_ing["unit"])]

        if data_ing[0]["chem"] == "Total Volume":
            return [], [], "", "", None
        else:
            return columns_recipe, data_ing, "Ingredients", chosen, None

    except ValueError:
        return [], [], "", "", None


#-------------------- show recipe

@app.callback(
    [
        Output("Recipe", "columns"),
        Output("Recipe", "data"),
        Output("header_Recipe", "children"),
        Output("Recipe_Buffername", "children"),
    ],
        Input("Show", "n_clicks"),
        Input("Buffer_under_options", "value"),
        State("input-volume-unit", "value"),
        State("input-volume", "value"),
)
def table_recipe(n_clicks, chosen, vol, vol_unit):
    Chem = Chemical.load()
    Buffer = Buf.load()

    try:
        vol = float(vol) * float(vol_unit)
        water, water_unit = unit_function.vol(vol)
        ing = {}
        index = None
        unit = None


        if not n_clicks:
            return [], [], "", ""

        for i, l in enumerate(Buffer):
            if chosen == Buffer[i].name:
                for j, k in enumerate(Buffer[i].ingredients):
                    ing[j] = {"name": Buffer[i].ingredients[j], "amount": Buffer[i].molarity[j],
                              "unit": Buffer[i].unit[j]}

        table = {"number": [], "chem": [], "amount": [], "unit": []}

        for i in ing:
            for j, k in enumerate(Chem):
                if Chem[j].name == ing[i]["name"]:
                    index = j

            if ing[i]["unit"] == "M":
                n = vol * ing[i]["amount"]
                mass = n * float(Chem[index].mass)
                if Chem[index].aggregation == "solid":
                    result, unit = unit_function.mass(mass)
                if Chem[index].aggregation == "liquid":
                    result = mass / Chem[index].density
                    result, unit = unit_function.vol(result)

            if ing[i]["unit"] == "%":
                result = vol * ing[i]["amount"] * 0.01
                result, unit = unit_function.vol(result)

            table["number"].append(i + 1)
            table["chem"].append(ing[i]["name"])
            table["amount"].append(result)
            table["unit"].append(unit)
        table["number"].append("")
        table["chem"].append("Fill up with water to ")
        table["amount"].append(water)
        table["unit"].append(water_unit)

        data_recipe = [{"number": a, "chem": b, "amount": f'{c} {d}'} for (a, b, c, d) in
                zip(table["number"], table["chem"], table["amount"], table["unit"])]

        return columns_recipe, data_recipe, "Recipe", chosen

    except ValueError:
        return [], [], "", ""

if __name__ == '__main__':
    app.run_server(debug=True)