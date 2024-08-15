# CECS 451 Artificial Intelligence Assignments

This repository contains assignments from my AI class. Currently, it includes one project:

## A* Algorithm Implementation

Located in the `a-star` folder, this project implements the A* search algorithm for finding the optimal path between cities in California.

### Files in the a-star folder:

1. `a-star.py`: The main Python script implementing the A* algorithm.
2. `coordinates.txt`: Contains the latitude and longitude coordinates of California cities.
3. `map.txt`: Defines the connections between cities and their distances.

### How it works:

The A* algorithm uses a combination of the actual distance traveled (g-score) and an estimated distance to the goal (h-score) to find the optimal path between two cities. The script:

1. Reads city coordinates from `coordinates.txt`.
2. Reads the map connections from `map.txt`.
3. Uses the Haversine formula to calculate straight-line distances between cities.
4. Implements the A* algorithm to find the best route between two given cities.

### Usage:

Run the script from the command line, providing the start and end cities as arguments:
python a-star.py [start_city] [end_city]
python a-star.py SanFrancisco LosAngeles

The script will output the best route and total distance between the specified cities.

### Requirements:

- Python 3.x
- No additional libraries required (uses only built-in modules)

Feel free to explore the code and experiment with different city combinations!


## 2. Hidden Markov Model (HMM) Implementation

Located in the `hmm` folder, this project implements a Hidden Markov Model for probabilistic inference.

### Files in the hmm folder:

1. `hmm.py`: The main Python script implementing the HMM algorithm.
2. `cpt.txt`: Input file containing the Conditional Probability Table (CPT) data.
3. `cptANS.txt`: Output file with the filtered probabilities for each input line.

### How it works:

The HMM implementation performs filtering on the input data. It reads the CPT from the input file, applies the filtering algorithm, and calculates the probabilities for each state.

### Usage:

Run the script from the command line, providing the input file as an argument:
python hmm.py cpt.txt

The script will output the filtered probabilities for each input line.

### Requirements:

- Python 3.x
- No additional libraries required (uses only built-in modules)

Feel free to explore the code and experiment with different inputs for both projects!


## 3. N-Queens Problem Solvers

Located in the `n-queens` folder, this project implements two different approaches to solve the N-Queens problem: Genetic Algorithm and Hill Climbing.

### Files in the n-queens folder:

1. `board.py`: Defines the Board class for representing the N-Queens board.
2. `genetic.py`: Implements the Genetic Algorithm approach to solve the N-Queens problem.
3. `hill.py`: Implements the Hill Climbing approach to solve the N-Queens problem.

### How it works:

#### Board Class
- Represents the N-Queens board and provides methods for board manipulation and fitness calculation.

#### Genetic Algorithm
- Uses evolutionary principles to solve the N-Queens problem.
- Implements crossover, mutation, and selection operations on a population of board configurations.
- Continues evolving the population until a solution with no attacking pairs is found.

#### Hill Climbing
- Uses local search to find a solution to the N-Queens problem.
- Starts with a random board configuration and iteratively moves to better neighboring configurations.
- Continues until a board with no attacking pairs is found.

### Usage:

To run the Genetic Algorithm solver:
python genetic.py

To run the Hill Climbing solver:
python hill.py

Both scripts will output the running time and the final board configuration.

### Requirements:

- Python 3.x
- NumPy library (for the Board class)

Feel free to explore the code and experiment with different board sizes or algorithm parameters!


## 4. Neural Network Regression

Located in the `neural_network_regression.ipynb` notebook, this project implements a simple neural network to solve a regression problem using a toy dataset.

### How it works:

1. Dataset Generation: Creates a toy dataset using a custom function with random parameters.
2. Data Splitting: Splits data into training, validation, and test sets.
3. Neural Network Implementation: 
   - One hidden layer with 3 neurons
   - One output neuron
   - Sigmoid activation function
4. Training:
   - Uses gradient descent and backpropagation
   - Implements forward and backward propagation
   - Updates weights and biases
5. Evaluation:
   - Plots training and validation loss over epochs
   - Retrains on combined training and validation set
   - Makes predictions on test set and visualizes results

### Usage:

Run the Jupyter Notebook `neural_network_regression.ipynb` cell by cell to see the implementation and results.

### Requirements:

- Python 3.x
- NumPy
- Matplotlib
- scikit-learn

This project demonstrates the implementation of a basic neural network from scratch and its application to a regression problem.


## 5. Decision Tree Algorithms Comparison

Located in the `decision_tree_comparison.ipynb` notebook, this project implements and compares various decision tree-based algorithms using the Breast Cancer dataset from scikit-learn.

### Dataset:
- Breast Cancer dataset from sklearn.datasets

### Algorithms Implemented:
1. Simple Decision Tree
2. Bagging Classifier
3. AdaBoost Classifier
4. Random Forest Classifier

### How it works:

1. Data Loading and Preprocessing:
   - Loads the Breast Cancer dataset
   - Splits data into training and test sets (50% each)

2. Simple Decision Tree:
   - Implements a decision tree with entropy criterion and max depth of 2
   - Calculates accuracy and confusion matrix
   - Visualizes the decision tree

3. Bagging Classifier:
   - Implements bagging with decision trees
   - Varies the number of estimators from 1 to 49
   - Plots accuracy against the number of estimators

4. AdaBoost Classifier:
   - Implements AdaBoost with decision trees
   - Varies the number of estimators from 1 to 49
   - Plots accuracy against the number of estimators

5. Random Forest Classifier:
   - Implements Random Forest with 100 estimators
   - Varies the number of features from 1 to 49
   - Plots accuracy against the number of features

### Usage:

Run the Jupyter Notebook `decision_tree_comparison.ipynb` cell by cell to see the implementation and results for each algorithm.

### Requirements:

- Python 3.x
- NumPy
- Matplotlib
- scikit-learn

This project demonstrates the implementation and comparison of different decision tree-based ensemble methods on a real-world dataset, showcasing how different parameters affect model performance.


## 6. Airport Location Optimization

Located in the `n_airports.ipynb` notebook, this project implements a clustering algorithm to optimize airport locations based on city distributions.

### Problem Description:
Given a set of cities, the goal is to find optimal locations for a specified number of airports that minimize the total distance between cities and their nearest airports.

### Key Components:

1. Data Generation:
   - Generates 100 cities clustered around 5 centers
   - Initializes 3 random airport locations

2. Visualization:
   - Plots cities and initial airport locations

3. Clustering Algorithm:
   - Implements a custom clustering algorithm to optimize airport locations
   - Uses gradient descent to minimize the total distance between cities and their nearest airports

4. Optimization Process:
   - Iteratively updates airport locations
   - Calculates and plots the objective function value (total distance) at each iteration

### Key Functions:

- `closest()`: Assigns each city to its nearest airport
- `objectiveFunction()`: Calculates the total distance between cities and their assigned airports
- `gradient()`: Computes the gradient and updates airport locations

### Usage:

Run the Jupyter Notebook `n_airports.ipynb` cell by cell to see the implementation, visualization, and optimization results.

### Requirements:

- Python 3.x
- NumPy
- Matplotlib

This project demonstrates the application of optimization techniques to a real-world problem, showcasing how iterative algorithms can be used to find optimal solutions in complex scenarios.


## 7. Markov Chain Monte Carlo (MCMC) Sampling for Bayesian Networks

Located in the `mcmc.py` file, this project implements MCMC sampling for a Bayesian Network representing relationships between cloud cover (C), sprinkler use (S), rain (R), and wet grass (W).

### Key Components:

1. Bayesian Network Setup:
   - Uses the `sorobn` library to create and query a Bayesian Network
   - Defines conditional probability tables for each variable

2. Probability Calculations:
   - Computes various conditional probabilities using the Bayesian Network

3. Transition Matrix:
   - Constructs a transition matrix for the MCMC sampling process

4. MCMC Sampling:
   - Implements an MCMC sampling function to estimate probabilities

5. Results Comparison:
   - Compares exact probabilities from the Bayesian Network with estimates from MCMC sampling

### Key Functions:

- `estimate(n, transition_matrix)`: Performs MCMC sampling for n iterations and estimates the probability of C=True given S=False and W=True

### Usage:

Run the script using Python:
python mcmc.py

The script will output:
- Sampling probabilities
- Transition probability matrix
- Exact and estimated probabilities for P(C|-s,w) with different sample sizes

### Requirements:

- Python 3.x
- pandas
- sorobn (custom Bayesian Network library)

This project demonstrates the application of MCMC sampling to estimate probabilities in a Bayesian Network, showcasing how sampling methods can be used to approximate probabilities in complex probabilistic models.
