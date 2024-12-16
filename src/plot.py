import matplotlib.pyplot as plt
import matplotlib as mpl
from constants import PERMITTED_STAT_TYPES

def get_labels_for_stat_type(stat_type):
    labels = {}

    if stat_type == "goals":
        labels["title"] = "Goals Scored Per Season"
        labels["ylabel"] = "Goals Scored"
    elif stat_type == "assists":
        labels["title"] = "Assists Provided Per Season"
        labels["ylabel"] = "Assists Provided"
    elif stat_type == "xG":
        labels["title"] = "xGoals Per Season"
        labels["ylabel"] = "xG"
    elif stat_type == "xA":
        labels["title"] = "xAssists Per Season"
        labels["ylabel"] = "xA"

    return labels


def plot_stats_per_season(stat_type: str, data1: dict, data2: dict, player1: str, player2: str):
    """
    Plots the given data representing goals scored per season for two players.

    Args:
        data1 (dict): A dictionary where keys are seasons (str) and values are goals (str) for player 1.
        data2 (dict): A dictionary where keys are seasons (str) and values are goals (str) for player 2.
        player1 (str): Name of player 1.
        player2 (str): Name of player 2.
    """
    if stat_type not in PERMITTED_STAT_TYPES:
        print("ERROR: Required stat type not found in the understat API library response")
        return None

    # Extract seasons and goals for both players
    seasons = sorted(set(data1.keys()).union(data2.keys()))
    stat1 = [float(data1.get(season, 0)) for season in seasons]
    stat2 = [float(data2.get(season, 0)) for season in seasons]

    # Set up the font and style
    mpl.rcParams['text.color'] = 'white'
    mpl.rcParams['axes.labelcolor'] = 'white'
    mpl.rcParams['xtick.color'] = 'white'
    mpl.rcParams['ytick.color'] = 'white'

    labels = get_labels_for_stat_type(stat_type)

    # Create the plot
    fig, ax = plt.subplots(figsize=(16, 10), facecolor='#1c1c1c')  # Darker shade of gray
    ax.set_facecolor('#1c1c1c')

    ax.plot(seasons, stat1, marker='o', color='skyblue', linewidth=2, label=player1)
    ax.plot(seasons, stat2, marker='o', color='orange', linewidth=2, label=player2)

    # Customize the plot
    ax.set_title(labels["title"], fontsize=20)
    ax.set_xlabel('Season', fontsize=14)
    ax.set_ylabel(labels["ylabel"], fontsize=14)
    legend = ax.legend(loc='upper left', fontsize=14)
    legend.get_frame().set_facecolor('black')
    ax.grid(visible=False)

    # Display the plot
    plt.tight_layout()
    plt.show()

