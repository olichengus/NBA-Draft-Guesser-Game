from nba_api.stats.static import players
import random
from src import GuessScore
from src.Game_API.GameAPI import GameAPI
from src.Player import Player


class GamePlatform:
    def __init__(self):
        self.gameAPI = GameAPI()
        self.availableYears = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
        self.poeltlPlayer = None
        self.round = 0
        self.answerPlayers = []

    # finds new Poeltl player
    def set_new_player(self):
        # maybe use try block here
        draft_year = random.choice(self.availableYears)
        self.poeltlPlayer = self.gameAPI.get_player_from_draft_year(draft_year)

    # returns the team name that made p overall pick in the r round of the y draft
    # used for Testing purposes
    def set_new_player_not_random(self):
        return True

    # receives player name and returns Guess Score based on how close the guess is
    def submit_answer(self, player_name):
        player_search = players.find_players_by_full_name("player_name")
        if player_search == [] or len(player_search) > 1 or player_search[0]["active"] is False:
            raise Exception("No specific player found")
        player_id = player_search[0]["id"]
        player2 = self.gameAPI.make_player(player_id)
        if self.poeltlPlayer is not Player:
            raise Exception("No player to guess")
        # make player by id
        res = self.poeltlPlayer.draft_match(player2)
        return res

    # resets game for another round of guessing
    def reset_game(self):
        self.set_new_player()
        self.answerPlayers = []
        self.round = 0
