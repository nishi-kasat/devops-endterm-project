from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

DATASET = "dataset/u.user"


def load_data():
    columns = ["user_id", "age", "gender", "occupation", "zip_code"]

    df = pd.read_csv(
        DATASET,
        sep="|",
        names=columns,
        header=None
    )

    # Convert numeric columns
    df["user_id"] = pd.to_numeric(df["user_id"], errors="coerce")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    # Remove invalid rows if any
    df = df.dropna()

    return df


@app.route("/")
def home():

    df = load_data()

    total_users = len(df)
    average_age = round(df["age"].mean(), 2)

    os.makedirs("static", exist_ok=True)

    # Age Distribution
    plt.figure(figsize=(8,4))
    df["age"].hist(bins=15)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Users")
    plt.tight_layout()
    plt.savefig("static/age_distribution.png")
    plt.close()

    # Occupation Distribution
    plt.figure(figsize=(10,5))
    df["occupation"].value_counts().plot(kind="bar")
    plt.title("Occupation Distribution")
    plt.tight_layout()
    plt.savefig("static/occupation_distribution.png")
    plt.close()

    occupation_summary = (
        df.groupby("occupation")
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
    )

    return render_template(
        "index.html",
        total_users=total_users,
        average_age=average_age,
        occupations=occupation_summary.to_html(
            index=False,
            classes="table table-striped"
        ),
        users=df.head(20).to_html(
            index=False,
            classes="table table-bordered"
        )
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)