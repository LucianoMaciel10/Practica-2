def calculate_team_goal_average(players_statistics,games_played):
    """Itera por cada jugador, suma todos los goles de los jugadores, divide el resultado por 
       la cantidad de partidos jugados y lo devuelve"""
    team_goal_average = 0
    for key in players_statistics:
        team_goal_average += players_statistics[key]["goals"]
    return team_goal_average/games_played

def average_goals_per_game(player,games_played):
   """Calcula y devulve el promedio de goles por partido de un jugador"""
   return player["goals"]/games_played