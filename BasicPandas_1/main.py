import pandas as pd
import json

df = pd.read_csv("sales.csv")
df = df.drop_duplicates()
df["Date"] = pd.to_datetime(df["Date"])

df["Revenue"] = df["Quantity"]*df["UnitPrice"]
    
def build_report_entry(name, quantity_series, revenue_series):
    return {
        name: {
            "Quantity": int(quantity_series[name]),
            "Revenue": int(revenue_series[name])
        }
    }

def get_totals(df, group):
    quantity = (
        df.groupby(group)["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    revenue = (
        df.groupby(group)["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return quantity, revenue

# TOTAL REVENUE
total_revenue = df["Revenue"].sum()

# CUSTOMERS
customers_totals_by_quantity, customers_totals_by_revenue = get_totals(df, "Customer")

top_customer_qty = customers_totals_by_quantity.idxmax()
top_customer_rev = customers_totals_by_revenue.idxmax()

# PRODUCTS
product_totals_by_quantity, product_totals_by_revenue = get_totals(df, "Product")

top_product_qty = product_totals_by_quantity.idxmax()
top_product_rev = product_totals_by_revenue.idxmax()

# CATEGORIES
category_report_by_quantity, category_report_by_revenue = get_totals(df, "Category")

top_category_qty = category_report_by_quantity.idxmax()
top_category_rev = category_report_by_revenue.idxmax()

# REPORT
report = {
    "total_revenue": int(total_revenue),
    "top_customer_by_revenue": (
        build_report_entry(
            top_customer_rev, 
            customers_totals_by_quantity, 
            customers_totals_by_revenue
            ) 
        ),
    "top_customer_by_quantity": (
        build_report_entry(
            top_customer_qty, 
            customers_totals_by_quantity, 
            customers_totals_by_revenue
            )
        ),
    "top_product_by_revenue": (
        build_report_entry(
            top_product_rev, 
            product_totals_by_quantity, 
            product_totals_by_revenue
            )
    ),
    "top_product_by_quantity": (
        build_report_entry(
            top_product_qty, 
            product_totals_by_quantity, 
            product_totals_by_revenue
            )
    ),
    "top_category_by_revenue": (
        build_report_entry(
            top_category_rev, 
            category_report_by_quantity, 
            category_report_by_revenue
            )
    ),
    "top_category_by_quantity": (
        build_report_entry(
            top_category_qty, 
            category_report_by_quantity, 
            category_report_by_revenue
            )
    )
}

with open("report.json", 'w') as jsonfile:
    json.dump(report, jsonfile, indent=4)
