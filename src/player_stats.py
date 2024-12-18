class PlayerStats:
    def __init__(self, player_id, player_name, stat_type, stats_per_season):
        """
        Initialize a PlayerStats instance.

        :param id: Unique identifier for the player
        :param name: Name of the player
        :param stat_type: Type of stats (e.g., goals, points, assists)
        :param stats_per_season: Dictionary with seasons as keys and stats as values
        """
        self.player_id = player_id
        self.player_name = player_name
        self.stat_type = stat_type
        self.stats_per_season = stats_per_season

    def __repr__(self):
        """
        Returns a string representation of the Player instance.
        """
        return (f"Player(id={self.player_id}, name='{self.player_name}', stat_type='{self.stat_type}', "
                f"stats_per_season={self.stats_per_season})")

    def get_total_stats(self):
        """
        Calculate and return the total stats across all seasons.
        :return: Total stats as an integer
        """
        return sum(self.stats_per_season.values())

    def get_season_stat(self, season):
        """
        Get the stats for a specific season.
        :param season: Season year as a key
        :return: Stats for the specified season
        """
        return self.stats_per_season.get(season, 0)