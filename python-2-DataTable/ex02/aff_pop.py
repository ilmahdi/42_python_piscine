from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FuncFormatter


def convert_population(v):
    """Convert population values to numeric"""
    return float(v.replace("B", "e9").replace("M", "e6").replace("k", "e3"))


def main():
    try:
        df = load("population_total.csv")
        df = df.map(convert_population)

        plt.plot(
            df.loc["Morocco", "1800":"2050"],
            label="Morocco", color="blue"
        )
        plt.plot(
            df.loc["France", "1800":"2050"],
            label="France", color="green"
        )

        plt.title("Population Projection")
        plt.xlabel("Year")
        plt.ylabel("Population")

        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))
        plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=4))
        plt.gca().yaxis.set_major_formatter(
            FuncFormatter(lambda value, _: f"{int(value / 1e6)}M")
        )
        plt.legend()
        plt.show()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully.")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
