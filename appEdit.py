import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from Tools import unit_function, Buf, Chemical, extract_unit, Col_Buffer, Col_Chem, Data_empty_recipe, Data_empty, Col_recipe, Col
from LayoutEdit import layout


#print(Chem)
Password = "Gilli"

external_stylesheets = [dbc.themes.LUMEN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Buffer Update"
app.config.suppress_callback_exceptions = True

app.layout = layout
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

    Buffer = Buf.load()
    if BufferName in [d.name for d in Buffer]:
        return "Buffer already in the library!", False, True, True, ""
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
            if i["name"] == "" or i["amount"] == "" or i['unit'] == "" or i['mass'] == "" or i['aggregation'] == "" or i['density'] == "" or subfolder == "":
                EmptyField = "Yes"
        if EmptyField == "Yes":
            return [], Col_recipe, "", "", "Please fill in all empty fields", "", "", ""
        if EmptyField == "No":
            return data, Col_recipe, "Recipe", "Please check if the Recipe is correct!", "Successful", f"Name: {NameNewBuffer}", f"Usage: {subfolder} Buffer", info_in


@app.callback(
        Output("success","children"),
        Input("confirm", "n_clicks"),
        State("table_recipe", "data"),
        State("subfolder", "value"),
        State("NameNewBuffer", "children"),
        State("password_1", "value"),
        State("info_show", "value"),
)
def data(n_clicks, data, subfolder, NameNewBuffer, password, info):
    global Password
    ListNewIngredients = []
    ListNewMolarity = []
    ListNewUnit = []
    Buffer = Buf.load()
    Chem = Chemical.load()

    if not n_clicks:
        return ""
    if n_clicks > 0:
        if password == Password:
            if NameNewBuffer in [d.name for d in Buffer]:
                return "Buffer already added"

            for i, j in enumerate(data):
                Amount, unit_data = extract_unit(data[i]["unit"], data[i]["amount"])
                ListNewIngredients.append(data[i]["name"])
                ListNewMolarity.append(float(Amount))
                ListNewUnit.append(unit_data)

                if not data[i]["name"] in [d.name for d in Chem]:
                    data[i]["name"] = Chemical(data[i]["name"],data[i]["mass"], data[i]["aggregation"], data[i]["density"])
                    Chem.append(data[i]["name"])

            NameNewBuffer = Buf(NameNewBuffer, subfolder, ListNewIngredients, ListNewMolarity, ListNewUnit, info)
            Buffer.append(NameNewBuffer)
            Buf.save(Buffer)
            Chemical.save(Chem)
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
        Buffer = Buf.load()
        Buffer = Buf.list_to_dic(Buffer)
        return Buffer, Col_Buffer
    if chose == "chem":
        Chem = Chemical.load()
        Chem = Chemical.list_to_dic(Chem)
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
            data = Chemical.dic_to_list(data)
            Chemical.save(data)

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

            new_data = Buf.dic_to_list(new_data)
            Buf.save(new_data)

        return "Update successful"
    else:
        return html.H2(style={"color":"red"}, id="save_2", children = "Wrong Password")

if __name__ == '__main__':
    app.run_server(debug=True)