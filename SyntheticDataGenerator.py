
# Importing necessary libraries
import numpy as np
import pandas as pd

class SyntheticDataGenerator:
    """
    A class to generate synthetic data for different machine learning tasks.

    Attributes:
        n_samples (int): Number of samples to generate.
        n_features (int): Number of features in the dataset.
        task (str): The machine learning task for which data is generated. 
                    Supported tasks are 'regression', 'classification', and 'clustering'.
    """

    def __init__(self, n_samples: int, n_features: int, task: str):
        """
        Initialize the SyntheticDataGenerator with the specified parameters.

        Args:
            n_samples (int): Number of samples to generate.
            n_features (int): Number of features in the dataset.
            task (str): The machine learning task ('regression', 'classification', 'clustering').
        """
        self.n_samples = n_samples
        self.n_features = n_features
        self.task = task

    def _generate_regression_data(self, X: np.ndarray):
        """
        Generates synthetic data for regression tasks.

        Args:
            X (numpy.ndarray): The input feature matrix.

        Returns:
            X (numpy.ndarray): Features of the synthetic dataset.
            y (numpy.ndarray): Target values for regression.
        """
        weights = np.random.rand(self.n_features)
        bias = np.random.rand()
        y = X.dot(weights) + bias
        y += np.random.normal(0, 0.1, size=y.shape)  # Add noise
        return X, y

    def _generate_classification_data(self, X: np.ndarray):
        """
        Generates synthetic data for classification tasks.

        Args:
            X (numpy.ndarray): The input feature matrix.

        Returns:
            X (numpy.ndarray): Features of the synthetic dataset.
            y (numpy.ndarray): Binary target values for classification.
        """
        weights = np.random.rand(self.n_features)
        bias = np.random.rand()
        logits = X.dot(weights) + bias
        probs = 1 / (1 + np.exp(-logits))
        y = np.where(probs > 0.5, 1, 0)
        return X, y

    def _generate_clustering_data(self, X: np.ndarray):
        """
        Generates synthetic data for clustering tasks.

        Args:
            X (numpy.ndarray): The input feature matrix.

        Returns:
            y (numpy.ndarray): Data points for clustering.
            None: As clustering is unsupervised, no targets are returned.
        """
        centroids = np.random.rand(self.n_samples, self.n_features)
        cluster_ids = np.random.choice(range(self.n_samples), size=self.n_samples)
        y = centroids[cluster_ids] + np.random.normal(0, 0.1, size=(self.n_samples, self.n_features))
        return y, None

    def generate_data(self):
        """
        Generates synthetic data based on the specified task.

        Returns:
            X (numpy.ndarray): Features of the synthetic dataset (if applicable).
            y (numpy.ndarray): Target values or data points for the specified task.

        Raises:
            ValueError: If the specified task is not supported.
        """
        X = np.random.rand(self.n_samples, self.n_features)

        if self.task == 'regression':
            return self._generate_regression_data(X)
        elif self.task == 'classification':
            return self._generate_classification_data(X)
        elif self.task == 'clustering':
            return self._generate_clustering_data(X)
        else:
            supported_tasks = ['regression', 'classification', 'clustering']
            raise ValueError(f"Unsupported task: {self.task}. Supported tasks are: {supported_tasks}")

# Usage Instructions (in Swedish)
# För att använda denna klass, skapa först en instans av den genom att ange antalet prover, antalet funktioner och uppgiftstypen.
# Exempel: generator = SyntheticDataGenerator(n_samples=1000, n_features=5, task='regression')
# Anropa sedan metoden generate_data för att generera data. 
# Exempel: X, y = generator.generate_data()

# För att konvertera de genererade datan till en DataFrame och spara som CSV, använd följande kod:
# data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
# data['target'] = y
# data.to_csv('synthetic_data.csv', index=False)

# Uncomment the following lines to test the class functionality.
# generator = SyntheticDataGenerator(n_samples=1000, n_features=5, task='regression')
# X, y = generator.generate_data()
# data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
# data['target'] = y
# data.to_csv('synthetic_data.csv', index=False)
