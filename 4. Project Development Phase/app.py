from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import pickle


app = Flask(__name__)
model = pickle.load(open('predictor.pkl', 'rb'))


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    # Getting the input values from the application
    cash = float(request.form["cash"])
    short_term_securities = float(request.form["short_term_securities"])
    receivables_short_term_liabilities = float(request.form["receivables_short_term_liabilities"])
    operating_expenses_depreciation = float(request.form["operating_expenses_depreciation"])
    retained_earnings = float(request.form["retained_earnings"])
    total_assets = float(request.form["total_assets"])
    net_profit = float(request.form["net_profit"])
    depreciation = float(request.form["depreciation"])
    total_liabilities = float(request.form["total_liabilities"])
    profit_on_operating_activities = float(request.form["profit_on_operating_activities"])
    financial_expenses = float(request.form["financial_expenses"])
    operating_expenses = float(request.form["operating_expenses"])
    profit_on_sales = float(request.form["profit_on_sales"])
    sales = float(request.form["sales"])
    current_assets_inventory = float(request.form["current_assets_inventory"])
    short_term_liabilities = float(request.form["short_term_liabilities"])
    sales_cost_of_products_sold = float(request.form["sales_cost_of_products_sold"])
    total_costs = float(request.form["total_costs"])
    total_sales = float(request.form["total_sales"])

    # Calculating the required values
    attr5 = 365 * ((cash + short_term_securities + receivables_short_term_liabilities) / operating_expenses_depreciation)
    attr6 = retained_earnings / total_assets
    attr26 = (net_profit + depreciation) / total_liabilities
    attr27 = profit_on_operating_activities / financial_expenses
    attr34 = operating_expenses / total_liabilities
    attr35 = profit_on_sales / total_assets
    attr42 = profit_on_operating_activities / sales
    attr46 = current_assets_inventory / short_term_liabilities
    attr56 = sales_cost_of_products_sold / sales
    attr58 = total_costs / total_sales

    # Making an input array for the model
    inputs = [[attr5, attr6, attr26, attr27, attr34, attr35, attr42, attr46, attr56, attr58]]

    # Getting the prediction
    prediction = model.predict(inputs)
    print(prediction)
    if prediction == 1:
        output = "!! THE COMPANY CAN GO BANKRUPT !!"
    else:
        output = "!! THE COMPANY IS SAFE !!"

    # Returning the prediction
    return jsonify({'y': output})


if __name__ == '__main__':
    app.run(debug = True)


# Attr5: [(cash + short-term securities + receivables short-term liabilities) / (operating expenses depreciation)] * 365

# Attr6: retained earnings / total assets

# Attr26: (net profit + depreciation) / total liabilities

# Attr27: profit on operating activities / financial expenses

# Attr34: operating expenses / total liabilities

# Attr35: profit on sales / total assets

# Attr42: profit on operating activities / sales

# Attr46: (current assets inventory) / short-term liabilities

# Attr56: (sales cost of products sold) / sales

# Attr58: total costs /total sales