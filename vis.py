import numpy as np
import matplotlib.pyplot as plt

def draw_game(g: np.ndarray, ax: plt.Axes):
    ax.matshow(g, vmin=-1, vmax=1)


if __name__ == '__main__':
    def create_game():
        g = np.zeros((7, 7))
        g[:2, :2] = -1
        g[:2, -2:] = -1
        g[-2:, :2] = -1
        g[-2:, -2:] = -1
        return g
    
    g = create_game()
    g[3, 3] = 1
    fig, ax = plt.subplots()
    draw_game(g, ax)
    plt.show()

