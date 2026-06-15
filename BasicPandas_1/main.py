import pandas as pd
import json

df = pd.read_csv("orders.csv")
df = df.drop_duplicates()
df["Date"] = pd.to_datetime(df["Date"])

df["Revenue"] = df["Quantity"]*df["UnitPrice"]
    
total_revenue = df["Revenue"].sum()
customers_totals = (
    df.groupby("Customer")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
product_totals_by_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
product_totals_by_quantity = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)
category_report_by_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
category_report_by_quantity = (
    df.groupby("Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

report = {
    "total_revenue": int(total_revenue),
    "top_customer": {
        customers_totals.idxmax(): {
            "Quantity": int(df[df["Customer"] == customers_totals.idxmax()]["Quantity"].sum()),
            "Revenue": customers_totals.max()
            }},
    "top_product_by_revenue": {
        product_totals_by_revenue.idxmax(): {
            "Quantity": int(df[df["Product"] == product_totals_by_revenue.idxmax()]["Quantity"].sum()),
            "Revenue": product_totals_by_revenue.max()
        }},
    "top_product_by_quantity": {
        product_totals_by_quantity.idxmax(): {
            "Quantity": product_totals_by_quantity.max(),
            "Revenue": int(df[df["Product"] == product_totals_by_quantity.idxmax()]["Revenue"].sum())
        }},
    "top_category_by_revenue": {
        category_report_by_revenue.idxmax(): {
            "Quantity": int(df[df["Category"] == category_report_by_revenue.idxmax()]["Quantity"].sum()),
            "Revenue": category_report_by_revenue.max()
        }},
    "top_category_by_quantity": {
        category_report_by_quantity.idxmax(): {
            "Quantity": category_report_by_quantity.max(),
            "Revenue": int(df[df["Category"] == category_report_by_quantity.idxmax()]["Revenue"].sum()),
        }}
}

with open("report.json", 'w') as jsonfile:
    json.dump(report, jsonfile, indent=4)

print(df[df["Customer"] == "Beatriz"]["Quantity"].sum())