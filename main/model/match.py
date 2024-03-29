class Match:
    def __init__(self, name, players_pair):
        self.name = name
        self.player1 = players_pair[0]
        self.score_player1 = 0
        self.player2 = players_pair[1]
        self.score_player2 = 0
        self.list_score = [0.0, 0.5, 1.0]

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def add_score_match(self, dic_player):

        score_p1 = ""
        score_p2 = ""

        while score_p1 not in self.list_score:
            score_p1 = input("Score du " + self.player1 + ": ")
            score_p1 = float(score_p1)

        self.score_player1 = score_p1
        dic_player[self.player1].score += score_p1

        if score_p1 == 0.0:
            self.list_score = [1.0]

        if score_p1 == 0.5:
            self.list_score = [0.5]

        if score_p1 == 1.0:
            self.list_score = [0.0]

        while score_p2 not in self.list_score:
            score_p2 = input("Score du " + self.player2 + ": ")
            score_p2 = float(score_p2)

        self.score_player2 = score_p2
        dic_player[self.player2].score += score_p2

        print(self.return_dic_match())
        print("\n")

    def return_dic_match(self):
        return {
            "name_match": self.name,
            "match_played": (
                [self.player1, self.score_player1],
                [self.player2, self.score_player2],
            ),
        }
