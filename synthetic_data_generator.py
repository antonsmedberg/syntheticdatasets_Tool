import matplotlib.pyplot as plt
import numpy as np


class SyntheticDataGenerator:
    """
    A class to generate synthetic data for different machine learning tasks.

    Attributes:
        n_samples (int): Number of samples to generate.
        n_features (int): Number of features in the dataset.
        task (str): The machine learning task for which data is generated.
                    Supported tasks are 'regression', 'classification', and 'clustering'.
        noise_level (float, optional): Noise level for regression data.
        n_classes (int, optional): Number of classes for classification.
        n_clusters (int, optional): Number of clusters for clustering.
    """

    def __init__(self, n_samples: int, n_features: int, task: str,
                 noise_level: float = 0.1, n_classes: int = 2, n_clusters: int = 3):
        self.validate_parameters(n_samples, n_features, task, n_classes, n_clusters)
        self.n_samples = n_samples
        self.n_features = n_features
        self.task = task
        self.noise_level = noise_level
        self.n_classes = n_classes
        self.n_clusters = n_clusters

    @staticmethod
    def validate_parameters(n_samples, n_features, task, n_classes, n_clusters):
        if n_samples <= 0 or n_features <= 0:
            raise ValueError("Number of samples and features must be positive.")
        if task not in ['regression', 'classification', 'clustering']:
            raise ValueError("Task must be 'regression', 'classification', or 'clustering'.")
        if n_classes < 2:
            raise ValueError("Number of classes must be at least 2 for classification.")
        if n_clusters < 1:
            raise ValueError("Number of clusters must be positive for clustering.")

    def _generate_regression_data(self, X: np.ndarray):
        weights = np.random.rand(self.n_features)
        bias = np.random.rand()
        y = X.dot(weights) + bias
        y += np.random.normal(0, self.noise_level, size=y.shape)
        return X, y

    def _generate_classification_data(self, X: np.ndarray):
        weights = np.random.rand(self.n_features, self.n_classes)
        biases = np.random.rand(self.n_classes)
        logits = X.dot(weights) + biases
        y = np.argmax(logits, axis=1)
        return X, y

    def _generate_clustering_data(self, X: np.ndarray):
        centroids = np.random.rand(self.n_clusters, self.n_features)
        cluster_ids = np.random.choice(range(self.n_clusters), size=self.n_samples)
        y = centroids[cluster_ids] + np.random.normal(0, self.noise_level, size=(self.n_samples, self.n_features))
        return y, None

    def generate_data(self):
        X = np.random.rand(self.n_samples, self.n_features)

        if self.task == 'regression':
            return self._generate_regression_data(X)
        elif self.task == 'classification':
            return self._generate_classification_data(X)
        elif self.task == 'clustering':
            return self._generate_clustering_data(X)

    def plot_data(self, X, y=None):
        if self.task == 'regression':
            plt.scatter(X[:, 0], y)
            plt.xlabel('Feature 1')
            plt.ylabel('Target Value')
        elif self.task == 'clustering':
            plt.scatter(X[:, 0], X[:, 1], c=y)
            plt.xlabel('Feature 1')
            plt.ylabel('Feature 2')
        elif self.task == 'classification':
            plt.scatter(X[:, 0], X[:, 1], c=y, cmap='jet')  # using 'jet' colormap
        plt.title(f'Synthetic Data for {self.task.capitalize()}')
        plt.show()

# Example Usage
# generator = SyntheticDataGenerator(n_samples=1000, n_features=2, task='classification', n_classes=3)
# X, y = generator.generate_data()
# generator.plot_data(X, y)

# Converting to DataFrame and Saving to CSV
# data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
# data['target'] = y
# data.to_csv('synthetic_data.csv', index=False)
