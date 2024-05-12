# K-means-Clustering-Implementation

Sure, here's a README template for your project:

---

# K-means Clustering Implementation

## Overview

In this project, we implement the k-means clustering algorithm without using any library functions. The program takes a dataset file as input, initializes the k-means clustering, and runs it for a range of K values (2-10). It calculates the error after 20 iterations for each K value and displays the results. Additionally, it draws a graph showing the error values corresponding to different K values.

## Dataset Description

The dataset file follows the same format as the training files in the UCI datasets directory. Each column, except for the last one, contains different features. The last column contains the class labels. The program does not use data from the last column as features.

## K-means Algorithm

1. Initialize the number of clusters, K.
2. Randomly assign K centroid points.
3. Assign each data point to its nearest centroid to create K clusters.
4. Re-calculate the centroids using the newly created clusters.
5. Repeat steps 3 and 4 until the centroids converge.

## Initialization

Different initialization approaches are attempted to deal with the initial centroid problem. The program implements the initialization method without using any library functions. For random state, it uses 0.

## Usage

```bash
python kmeans.py <data_file>
```

## Output

For each value of K (2-10), the program displays the error after 20 iterations in the format:

```
For k = 2 After 20 iterations: Error = 
For k = 3 After 20 iterations: Error = 
...
For k = 10 After 20 iterations: Error = 
```

Additionally, it generates a graph showing the error vs. K values.

```

## Dependencies

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
