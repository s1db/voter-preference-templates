import numpy as np

def unipolar(agents, candidates):
    tiled = np.tile(np.arange(0, candidates).reshape(candidates, 1), agents)
    return tiled

if __name__ == '__main__':
    print(unipolar(5, 10))