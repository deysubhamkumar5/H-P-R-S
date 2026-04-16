# module4_analytics.py
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    try:
        df = pd.read_csv("patients.csv", names=["ID", "Name"])
        return df
    except:
        print("File not found")
        return None


def analyze(df):
    print("\nTotal Patients:", len(df))


def plot_data(df):
    df["ID"].value_counts().plot(kind="bar")
    plt.title("Patient Records")
    plt.savefig("output.png")
    plt.close()
    print("Chart saved as output.png")


def main():
    df = load_data()
    if df is not None:
        analyze(df)
        plot_data(df)


if __name__ == "__main__":
    main()