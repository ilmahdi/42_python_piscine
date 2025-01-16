from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def main():
    try:
        df = load("life_expectancy_years.csv")

        plt.plot(df.loc["Morocco"])

        plt.title("Morocco Life expectancy Projection")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")

        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))

        plt.show()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully.")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
