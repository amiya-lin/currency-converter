from cProfile import label
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("financial_transactions.csv")
df["date"] = pd.to_datetime(df["date"])
total_income = df[df["type"]=="income"]["amount"].sum()
total_expense = df[df["type"]=="expense"]["amount"].sum()

net_cash_flow = total_income - total_expense

daily_income = df[df["type"] == "income"].groupby("date")["amount"].sum()
daily_expense = df[df["type"] == "expense"].groupby("date")["amount"].sum()

daily_cash_flow = pd.concat(
    [daily_income.rename("income"),
    daily_expense.rename("expense")
    ],
    axis = 1
)

daily_cash_flow = daily_cash_flow.fillna(0)
daily_cash_flow["net_cash_flow"] = (
    daily_cash_flow["income"] - daily_cash_flow["expense"]
)

plt.plot(
    daily_cash_flow.index,
    daily_cash_flow["net_cash_flow"]
)

plt.title("daily_net_cash_flow")
plt.xlabel("date")
plt.ylabel("net cash flow")
plt.xticks(rotation = 45)

plt.show()


ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(
    daily_cash_flow.index,
    daily_cash_flow["income"],
    label = "income"
)

ax2.plot(
    daily_cash_flow.index,
    daily_cash_flow["expense"],
    label = "expense"
)

ax2.plot(
    daily_cash_flow.index,
    daily_cash_flow["net_cash_flow"],
    label = "net_cash_flow"
)
ax1.set_ylim(0,5500)
ax2.set_ylim(-150,150)
ax1.set_title("daily income,expense and net cash flow")
ax1.set_xlabel("date")
ax1.set_ylabel("amount")
ax1.tick_params(axis = "x",labelrotation = 45)

plt.show()

daily_cash_flow["cumulative_cash_flow"] = (
    daily_cash_flow["net_cash_flow"].cumsum()
)

peak_date = daily_cash_flow["net_cash_flow"].idxmax()
peak_value = daily_cash_flow.loc[peak_date,"cumulative_cash_flow"]
daily_cash_flow["net_flow_status"] = np.where(daily_cash_flow["net_cash_flow"] > 0,"positive","negative")
expense_df = df[df["type"] == "expense"]
max_expense_index = expense_df["amount"].idxmax()
max_expense = expense_df.loc[max_expense_index]
category_expense = expense_df.groupby("category")["amount"].sum()
highest_expense_category = category_expense.idxmax()

saving_rate = net_cash_flow / total_income *100
max_expense_amount = max_expense["amount"]



print(daily_cash_flow)
print("\n========financial analysis report=========="
      "\ntotal income:",total_income,
      "\ntotal expense:",total_expense,
      f"f\nnet cash flow:{net_cash_flow}",
      "\nmax expense amount:",max_expense_amount,
      f"\nsaving rate:{saving_rate:.2f}%"
      "\n",)

