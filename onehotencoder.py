import numpy as np

class onehotencoder:

    def __init__(self, y):
        self.y = y

    def hotencode(self):
        #y is a 1D numpy array
        assert self.y.ndim == 1
        unique_classes = np.unique(self.y)
        num_classes = len(unique_classes)

        hot_encoded = np.zeros((self.y.shape[0], num_classes))

        for i in range(self.y.shape[0]):
            for j in range(num_classes):
                if self.y[i] == j:
                    hot_encoded[i][j] = 1
        return hot_encoded
