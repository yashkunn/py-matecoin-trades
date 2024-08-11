import json
from decimal import Decimal


def calculate_profit(
        trades_file: str, output_file: str = "profit.json"
) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        matecoin_account += bought
        matecoin_account -= sold

        earned_money -= bought * matecoin_price
        earned_money += sold * matecoin_price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(output_file, "w") as file:
        json.dump(profit_data, file, indent=4)
