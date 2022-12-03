class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.__score = {self.player1_name: 0, self.player2_name: 0}
        self.score_equal_text = {0: "Love-All", 1: "Fifteen-All",
                            2: "Thirty-All", 3: "Forty-All", "else": "Deuce"}
        self.has_advantage_text = {1: "Advantage player1", "more_than_positive_one": "Win for player1", -
                                1: "Advantage player2", "less_than_negative_one": "Win for player2"}
        self.temp_text = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    @property
    def player1_score(self):
        return self.__score[self.player1_name]

    @property
    def player2_score(self):
        return self.__score[self.player2_name]

    def won_point(self, player_name):
        self.__score[player_name] += 1

    def check_score_is_tie(self):
        if self.player1_score == self.player2_score:
            return True
        return False

    def print_score_equal_text(self):
        try:
            score = self.score_equal_text[self.player1_score]
        except KeyError:
            score = self.score_equal_text["else"]
        return score

    def check_player_advantage(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference >= 0:
            if score_difference >= 2:
                return self.has_advantage_text["more_than_positive_one"]
            return self.has_advantage_text[score_difference]
        else:
            if score_difference <= -2:
                return self.has_advantage_text["less_than_negative_one"]
            return self.has_advantage_text[score_difference]

    def check_score_higher_than_four(self):
        if (self.player1_score) >= 4 or (self.player2_score) >= 4:
            return True
        return False

    def check_temporal_situation(self):
        return self.temp_text[self.player1_score] + "-" + self.temp_text[self.player2_score]

    def get_score(self):
        if self.check_score_is_tie():
            return self.print_score_equal_text()
        elif self.check_score_higher_than_four():
            return self.check_player_advantage()
        else:
            return self.check_temporal_situation()
