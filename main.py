import numpy as np
import pandas as pd


class SyntheticDataGenerator:
    def __init__(self, n_samples, n_features, task):
        self.n_samples = n_samples
        self.n_features = n_features
        self.task = task

    def generate_data(self):
        X = np.random.rand(self.n_samples, self.n_features)
        if self.task == 'regression':
            # Generate regression data
            weights = np.random.rand(self.n_features)
            bias = np.random.rand()
            y = X.dot(weights) + bias
            y += np.random.normal(0, 0.1, size=y.shape)  # Add noise
            return X, y
        elif self.task == 'classification':
            # Generate classification data
            weights = np.random.rand(self.n_features)
            bias = np.random.rand()
            logits = X.dot(weights) + bias
            probs = 1 / (1 + np.exp(-logits))
            y = np.where(probs > 0.5, 1, 0)
            return X, y
        elif self.task == 'clustering':
            # Generate clustering data
            centroids = np.random.rand(self.n_samples, self.n_features)
            cluster_ids = np.random.choice(range(self.n_samples), size=self.n_samples)
            y = centroids[cluster_ids] + np.random.normal(0, 0.1, size=(self.n_samples, self.n_features))
            return y, None
        else:
            raise ValueError(f"Unsupported task: {self.task}")


# Example usage
generator = SyntheticDataGenerator(n_samples=1000, n_features=5, task='regression')
X, y = generator.generate_data()

# Convert to DataFrame and save as CSV
data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
data['target'] = y
data.to_csv('synthetic_data.csv', index=False)
