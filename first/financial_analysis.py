import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import ylabel

df = pd.read_csv("expenses.csv")

df["date"] = pd.to_datetime(df["date"])

def create_daily_chart(df):
    plt.plot(df["date"],df["amount"])
    plt.title("daily spending")
    plt.xlabel("date")
    plt.ylabel("amount")
    plt.xticks(rotation = 45)
    plt.savefig("daily_spending.png")
    plt.show()



def create_category_chart(category_total):

    category_total.plot(kind = "bar")

    plt.title("spending by category")
    plt.xlabel("category")
    plt.ylabel("Amount")

    for i,value in enumerate(category_total):
        plt.text(i , value , str(value),ha = "center",va = "bottom")
    plt.savefig("category_spending.png")
    plt.show()


category_total =df.groupby("category")["amount"].sum()

category_percentage = category_total / df["amount"].sum()*100

def create_pie_chart(category_percentage):
    plt.pie(
        category_percentage,
        labels = category_percentage.index,
        autopct = "f1.1%%"
    )

    plt.title("spending distribution")
    plt.savefig("spending_distribution.png")
    plt.show()

create_pie_chart(category_percentage)

create_category_chart(category_total)

create_daily_chart(df)

average_spending = df["amount"].mean()
high_spending = df[df["amount"] > average_spending]

std_spending = df["amount"].std()
upper_limit = average_spending + 2 * std_spending
outer = df[df["amount"] > upper_limit]

print(outer)








print("highest spending category:",category_total.idxmax())
print("which amount bigger than 50:\n",df[df["amount"] > 50])

print(df[(df["amount"] > 30) & (df["category"] == "food")])