import itertools
import random

team_names = ["Tigers", "Dragons", "Eagles", "Sharks", "Wolves", "Bears"]

def tournament_scheduler():
    random.shuffle(team_names)
    shuffled_pair = list(itertools.combinations(team_names, 2))
    
    print("--- Tournament Schedule ---")
    for i in range(len(shuffled_pair)):
        print(f"Match {i+1}: {shuffled_pair[i][0]} vs {shuffled_pair[i][1]}")
    print("---------------------------")
    print(f"Total Matches to play: {len(shuffled_pair)}")
        


tournament_scheduler()