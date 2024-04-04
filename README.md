## Installation
```
pip install gym-gui-tictactoe
```

## How to Use
```
gym.make('tictactoe-gui-v0')
```

## How to run demo
```
import gym_gui_tictactoe
import gym
if __name__ == "__main__":
    env = gym.make("gym_gui_tictactoe/tictactoe-gui-v0")
    env.reset()
    terminal = False
    while not terminal:
        action = input("Select action (" + ", ".join(map(str, env.get_actions())) + "): ")
        observation, winner, terminal, truncated, info = env.step(int(action))
        env.render()

    if winner != 0:
        print("Winner is player " + str(winner))
    else:
        print("It's a draw")
```
