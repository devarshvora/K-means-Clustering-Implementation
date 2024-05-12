#Name: Devarsh Vora

import random
import sys
import matplotlib.pyplot as plt

def load_data(data_file):
    """#Loads the data from the file and returns the feature columns (all columns except the last one)."""
    data = []
    with open(data_file, 'r') as file:
        for line in file:
            # Strip newline and split on whitespace
            line = line.strip().split()
            # Convert all but the last column (label) to floats and append to data
            data.append([float(val) for val in line[:-1]])
    return data

def initialize_centroids(features, k):
    """Randomly initialize 'k' centroids from the data points."""
    # Set the random seed for reproducibility
    random.seed(0)
    # Select 'k' random indices from the features
    indices = random.sample(range(len(features)), k)
    # Initialize centroids using the selected data points
    centroids = [features[idx] for idx in indices]
    return centroids

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    distance = sum((a - b) ** 2 for a, b in zip(point1, point2))
    return distance ** 0.5

def assign_clusters(features, centroids):
    """Assign each data point to the nearest centroid and return clusters."""
    clusters = [[] for _ in range(len(centroids))]
    
    for i, point in enumerate(features):
        # Find the centroid with the minimum distance to the point
        distances = [calculate_distance(point, centroid) for centroid in centroids]
        nearest_centroid_idx = distances.index(min(distances))
        clusters[nearest_centroid_idx].append(i)
    
    return clusters

def update_centroids(features, clusters, k):
    """Update centroids based on the current clusters."""
    centroids = []
    
    for i in range(k):
        if clusters[i]:
            # Calculate the mean of the points in the cluster
            cluster_points = [features[idx] for idx in clusters[i]]
            centroid = [sum(dim) / len(dim) for dim in zip(*cluster_points)]
            centroids.append(centroid)
        else:
            # If a cluster is empty, re-initialize the centroid randomly
            # Set the random seed for reproducibility
            random.seed(0)
            centroids.append(features[random.randint(0, len(features) - 1)])
    
    return centroids

def calculate_error(features, centroids, clusters):
    """Calculate the sum of squared errors."""
    error = 0
    for i, cluster in enumerate(clusters):
        if cluster:
            for idx in cluster:
                # Calculate squared distance between the point and its centroid
                distance = calculate_distance(features[idx], centroids[i])
                error += distance ** 2
    return error

def kmeans(features, k, max_iterations=20):
    """Implement k-means clustering with 'k' clusters."""
    # Initialize centroids
    centroids = initialize_centroids(features, k)
    
    for iteration in range(max_iterations):
        # Assign points to the nearest centroid
        clusters = assign_clusters(features, centroids)
        
        # Update centroids based on the current clusters
        new_centroids = update_centroids(features, clusters, k)
        
        # Check if centroids have changed
        if centroids == new_centroids:
            break
        
        # Update centroids for the next iteration
        centroids = new_centroids
    
    # Calculate the sum of squared errors
    error = calculate_error(features, centroids, clusters)
    
    return error

def main(data_file):
    """Main function to run k-means clustering on the given dataset."""
    # Load the data
    features = load_data(data_file)
    
    # Initialize a list to store errors
    errors = []
    
    # Loop through the range of K values (2 to 10)
    for k in range(2, 11):
        # Run k-means clustering and calculate the sum of squared errors
        error = kmeans(features, k)
        errors.append(error)
        
        # Print the error
        print(f"For k = {k} After 20 iterations: Error = {error:.4f}")
        
    # Plot error vs. K values
    plt.figure()
    plt.plot(range(2, 11), errors, marker='o')
    plt.xlabel('K')
    plt.ylabel('Error')
    plt.title('Error vs. K Plot')
    plt.show()

if __name__ == "__main__":
    # Check if the script is being run with a command-line argument
    # Here "data_file.txt" needs to be changes as per the name of the test file
    # Here "P3_Devarsh" is the my python file name (change if name is being modfiied)
    if len(sys.argv) != 2:
        print("How to Run: python P3_Devarsh.py data_file.txt")
        sys.exit(1)
    
    # The data file path is provided as the first command-line argument
    data_file = sys.argv[1]
    
    # Run the main function with the specified data file
    main(data_file)
