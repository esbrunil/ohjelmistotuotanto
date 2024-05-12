class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):

        if self.m_score1 == self.m_score2:
            if self.m_score1 > 2:
                return "Deuce"
            score_names = ["Love-All", "Fifteen-All", "Thirty-All"]
            return score_names[self.m_score1]

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                return "Advantage player1"

            if minus_result == -1:
                return "Advantage player2"

            if minus_result >= 2:
                return "Win for player1"

            return "Win for player2"

        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return score_names[self.m_score1] + "-" + score_names[self.m_score2]
