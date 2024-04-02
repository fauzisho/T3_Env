from gym.envs.registration import register


register(
    id='tictactoe_gui_gym/tictactoe-gui-v0',
    entry_point='tictactoe_gui_gym.envs:TicTacToeEnv',
)