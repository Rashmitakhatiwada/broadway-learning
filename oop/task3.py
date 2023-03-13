# create a class cricketor has the properties name, age and no of match played.
# creatae another class batsman that inherits class cricketor with properties name of runs and no of centuries .
# similarly create another class bowler that inherits the class cricketor with property no of wickets.
# create get_info methods in each class that prints the information accordingly.
class Cricketor:
    def __init__(self, name, age, no_of_match_played):
        self.name = name
        self.age = age
        self.no_of_match_played = no_of_match_played

    def get_info(self):
            return f"the cricketor name is {self.name} and his age is {self.age} ."
class Batsman(Cricketor):
    def __init__(self, no_of_runs, no_of_centuries):
        self.no_of_runs = no_of_runs
        self.no_of_centuries = no_of_centuries

    def get_info(self):
            return f"the cricketor has made {self.no_of_runs} runs and has a record of {self.no_of_centuries} centuries."

class Bowler(Cricketor):
    def __init__(self, no_of_wickets):
        self.no_of_wickets = no_of_wickets

    def get_info(self):
            return f"the cricketor has a record of {self.no_of_wickets} wickets. "

raj = Cricketor("raj", 21, 5)
result = raj.get_info()
print(result)
ram = Batsman(210, 2)
result = ram.get_info()
print(result)
ran = Bowler(5)
result = ran.get_info()
print(result)