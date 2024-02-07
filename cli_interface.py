# cli_interface.py
import argparse
from data_storage_utils import generate_and_save_data


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Generate synthetic data for machine learning.")

    # Add command-line arguments
    parser.add_argument('--samples', type=int, default=100, help='Number of samples to generate')
    parser.add_argument('--features', type=int, default=10, help='Number of features')
    parser.add_argument('--task', choices=['regression', 'classification', 'clustering'], required=True,
                        help='Type of task (regression, classification, clustering)')
    parser.add_argument('--noise', type=float, default=0.1, help='Noise level for data')

    return parser.parse_args()


def main():
    """Main function."""
    args = parse_arguments()

    try:
        message = generate_and_save_data(args.samples, args.features, args.task, args.noise)
        print(message)
    except ValueError as ve:
        print(f"Error: {ve}")
    except FileNotFoundError as fe:
        print(f"Error: {fe}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

