# Pandas Sales Analysis
## What is the project
This is a python Pandas project that transforms raw .csv sales date into meaningful business insights and exports them as JSON reports.
## Why was it made
It was built for practicing python, Pandas, csv transformation, json writing, and real analytics
## How to run it
```bash
pip install pandas
python main.py
```
('python3' is preferred for Linux and Mac)
## What does it produce
The code will take the input: csv data(initially named as 'sales.csv'), transforms it, and write the new data into the output: JSON file(initially named as 'report.json').
The JSON output is organised in this way:
```json
{
    "total_revenue": 46606,
    "top_customer_by_revenue": {
        "Beatriz": {
            "Quantity": 3,
            "Revenue": 5900
        }
    },
    "top_customer_by_quantity": {
        "Larissa": {
            "Quantity": 32,
            "Revenue": 4790
        }
    },
    "top_product_by_revenue": {
        "Laptop": {
            "Quantity": 7,
            "Revenue": 24500
        }
    },
    "top_product_by_quantity": {
        "Pen": {
            "Quantity": 130,
            "Revenue": 390
        }
    },
    "top_category_by_revenue": {
        "Electronics": {
            "Quantity": 25,
            "Revenue": 34630
        }
    },
    "top_category_by_quantity": {
        "Office": {
            "Quantity": 186,
            "Revenue": 1062
        }
    }
}
```
(Fictional data used as example)
## What was learned during the development
During this project, it was practiced:
-Pandas(groupby, data aggregation, sorting, duplicate removal, derived columns)
-Python dictionaries
-CSV transformation
-JSON writing
-optimisation by functions
## LICENSE
[MIT](https://choosealicense.com/licenses/mit/)