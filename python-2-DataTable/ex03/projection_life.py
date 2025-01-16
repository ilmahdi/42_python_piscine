from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        df_life = load("life_expectancy_years.csv")
        df_income = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )

        plt.title("1900")
        plt.xlabel("Gross domistic product")
        plt.ylabel("Life Expectancy")

        plt.scatter(df_income["1900"], df_life["1900"], color="blue")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=["300", "1k", "10k"])

        plt.tight_layout()
        plt.show()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully.")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
