import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_data_to_csv(X: np.ndarray, y: np.ndarray, filename: str = 'synthetic_data.csv') -> None:
    """Save synthetic data to CSV file."""
    data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
    data['target'] = y
    data.to_csv(filename, index=False)


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
        """
        Initialize the SyntheticDataGenerator object.

        Args:
            n_samples (int): Number of samples to generate.
            n_features (int): Number of features in the dataset.
            task (str): The machine learning task for which data is generated.
            noise_level (float, optional): Noise level for regression data.
            n_classes (int, optional): Number of classes for classification.
            n_clusters (int, optional): Number of clusters for clustering.
        """
        self.validate_parameters(n_samples, n_features, task, n_classes, n_clusters)
        self.n_samples = n_samples
        self.n_features = n_features
        self.task = task
        self.noise_level = noise_level
        self.n_classes = n_classes
        self.n_clusters = n_clusters

    @staticmethod
    def validate_parameters(n_samples, n_features, task, n_classes, n_clusters):
        """Validate parameters."""
        if n_samples <= 0 or n_features <= 0:
            raise ValueError("Number of samples and features must be positive.")
        if task not in ['regression', 'classification', 'clustering']:
            raise ValueError("Task must be 'regression', 'classification', or 'clustering'.")
        if n_classes < 2:
            raise ValueError("Number of classes must be at least 2 for classification.")
        if n_clusters < 1:
            raise ValueError("Number of clusters must be positive for clustering.")

    def _add_noise(self, data: np.ndarray) -> np.ndarray:
        """Add Gaussian noise to the data."""
        return data + np.random.normal(0, self.noise_level, size=data.shape)

    def generate_regression_data(self) -> tuple:
        """Generate synthetic regression data."""
        X = np.random.rand(self.n_samples, self.n_features)
        weights = np.random.rand(self.n_features)
        bias = np.random.rand()
        y = X.dot(weights) + bias
        y = self._add_noise(y)
        return X, y

    def generate_classification_data(self) -> tuple:
        """Generate synthetic classification data."""
        X = np.random.rand(self.n_samples, self.n_features)
        weights = np.random.rand(self.n_features, self.n_classes)
        biases = np.random.rand(self.n_classes)
        logits = X.dot(weights) + biases
        y = np.argmax(logits, axis=1)
        return X, y

    def generate_clustering_data(self) -> tuple:
        """Generate synthetic clustering data."""
        centroids = np.random.rand(self.n_clusters, self.n_features)
        cluster_ids = np.random.choice(range(self.n_clusters), size=self.n_samples)
        X = centroids[cluster_ids] + np.random.normal(0, self.noise_level, size=(self.n_samples, self.n_features))
        return X, cluster_ids

    def generate_data(self) -> tuple:
        """Generate synthetic data."""
        if self.task == 'regression':
            return self.generate_regression_data()
        elif self.task == 'classification':
            return self.generate_classification_data()
        elif self.task == 'clustering':
            return self.generate_clustering_data()

    def plot_data(self, X: np.ndarray, y: np.ndarray = None, xlabel: str = 'Feature 1',
                  ylabel: str = 'Feature 2', title: str = 'Synthetic Data') -> None:
        """Plot synthetic data."""
        plt.figure(figsize=(8, 6))
        if y is None:
            plt.scatter(X[:, 0], X[:, 1])
        else:
            plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
            plt.colorbar(label='Cluster')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(True)
        plt.show()


# Example Usage
generator = SyntheticDataGenerator(n_samples=1000, n_features=2, task='classification', n_classes=3)
X_data, y_data = generator.generate_data()
generator.plot_data(X_data, y_data)
save_data_to_csv(X_data, y_data, filename='synthetic_data.csv')


