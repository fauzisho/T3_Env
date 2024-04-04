# AI Trafic Project Group (Tic-Tac-Toe)

![ss.png](assets%2Fss.png)

## Installation
```
pip install gym-gui-tictactoe
```

## How to Use
```
gym.make("gym_gui_tictactoe/tictactoe-gui-v0")
```

## How to run demo
```
import gym_gui_tictactoe
import gym
if __name__ == "__main__":
    env = gym.make("gym_gui_tictactoe/tictactoe-gui-v0")
    env.reset()
    gameOver = False
    while not gameOver:
        action = input("Select action (" + ", ".join(map(str, env.get_actions())) + "): ")
        observation, winner, gameOver, truncated, info = env.step(int(action))
        env.render()

    if winner != 0:
        print("Winner is player " + str(winner))
    else:
        print("It's a draw")
```

## How to run agent with randomly actions
```
import gym_gui_tictactoe
import gym
import random

if __name__ == "__main__":
    env = gym.make("gym_gui_tictactoe/tictactoe-gui-v0")

    total_games = 20  # Total games to play
    player_1_wins = 0
    player_2_wins = 0

    for game in range(total_games):
        print("Game", game + 1)

        env.reset()
        gameOver = False

        static_actions = [0, 1, 2, 3, 4, 5, 6, 7, 8] 

        random.shuffle(static_actions)

        for action in static_actions:
            observation, winner, gameOver, truncated, info = env.step(action)
            env.render()

            if gameOver:
                break

        if winner == 1:
            player_1_wins += 1
        elif winner == -1:
            player_2_wins += 1

        if winner != 0:
            print("Winner is player " + str(winner))
        else:
            print("It's a draw")

    print("Player 1 wins:", player_1_wins)
    print("Player 2 wins:", player_2_wins)

    if player_1_wins > player_2_wins:
        print("Player 1 is the best!")
    elif player_2_wins > player_1_wins:
        print("Player 2 is the best!")
    else:
        print("Both players have the same number of wins.")
```
