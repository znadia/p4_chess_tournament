import json
class Player:

    def __init__(self, name, first_name, d_o_b, sex, ranking, score=0):
        self.name = name
        self.first_name = first_name
        self.d_o_b = d_o_b
        self.sex = sex
        self.ranking = ranking
        self.score = score

    def __str__(self):
        return f"nameess:{self.name} {self.first_name} {self.d_o_b} {self.sex} {self.score} {self.ranking}"

    def __repr__(self):
        return f"//repr// {self.name} {self.first_name} {self.d_o_b} {self.sex} {self.score} {self.ranking}"
        #return self.name

    
    def return_players(self):
        return {
                    "name": self.name,
                    "first_name": self.first_name,
                    "d_o_b": self.d_o_b,
                    "sex": self.sex,
                    "ranking": self.ranking,
                    "score": self.score
                }