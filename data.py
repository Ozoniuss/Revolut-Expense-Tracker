from datetime import datetime
import json
from dataclasses import dataclass
from typing import List

EXPENSES_JSON = "expenses.json"

@dataclass
class Expense:
    """Expense contains all the relevant information about an expense"""
    type: str
    state: str
    started_date: int
    updated_date: int
    completed_date: int
    currency: str
    amount: int
    fee: int
    description: str

    def __init__(self, json_expense) -> None:
        self.type = json_expense.get("type")
        self.state = json_expense.get("state")
        self.started_date = json_expense.get("startedDate")
        self.updated_date = json_expense.get("updatedDate")
        self.completed_date = json_expense.get("completedDate")
        self.currency = json_expense.get("currency")
        self.amount = json_expense.get("amount")
        self.fee = json_expense.get("fee")
        self.description = json_expense.get("description")


            
# loads all expenses from a json file with expenses
def load_expenses(filename: str = EXPENSES_JSON) -> List[Expense]:
    all_expenses = []
    with open(filename) as f:
        expenses_json = json.load(f)
        for exp_json in expenses_json:
            expense = Expense(exp_json)
            all_expenses.append(expense)

    return all_expenses


