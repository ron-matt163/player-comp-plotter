import matplotlib.pyplot as plt
import matplotlib as mpl
from constants import PERMITTED_STAT_TYPES
from typing import List
from player_stats import PlayerStats

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


def plot_stats_per_season(stat_type: str, players: List[PlayerStats]):
    """
    Plots the given data representing stats per season for multiple players.

    Args:
        stat_type (str): The type of stats to plot.
        players (list): A list of PlayerStats instances.
    """
    if stat_type not in PERMITTED_STAT_TYPES:
        print("ERROR: Required stat type not found in the understat API library response")
        return None

    # Extract all seasons from all players
    all_seasons = set()
    for player in players:
        all_seasons.update(player.stats_per_season.keys())
    seasons = sorted(all_seasons)

    # Set up the font and style
    mpl.rcParams['text.color'] = 'white'
    mpl.rcParams['axes.labelcolor'] = 'white'
    mpl.rcParams['xtick.color'] = 'white'
    mpl.rcParams['ytick.color'] = 'white'

    labels = get_labels_for_stat_type(stat_type)

    # Create the plot
    fig, ax = plt.subplots(figsize=(16, 10), facecolor='#1c1c1c')  # Darker shade of gray
    ax.set_facecolor('#1c1c1c')

    # Plot stats for each player
    for player in players:
        stats = [float(player.stats_per_season.get(season, 0)) for season in seasons]
        ax.plot(seasons, stats, marker='o', linewidth=2, label=player.player_name)

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

