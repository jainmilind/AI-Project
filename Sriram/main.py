import numpy as np
from sklearn.datasets import make_classification
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split


def pso_lda(X, y, n_particles=50, n_iterations=200, w=0.7, c1=1.4, c2=1.4):
    n_features = X.shape[1]
    lb = np.ones(n_features) * -10
    ub = np.ones(n_features) * 10
    # Initialize particles
    particles = np.random.uniform(low=lb, high=ub, size=(n_particles, n_features))
    velocities = np.zeros((n_particles, n_features))
    best_particle_positions = particles.copy()
    best_particle_scores = np.zeros(n_particles)
    global_best_particle_position = np.zeros(n_features)
    global_best_particle_score = -np.inf

    for i in range(n_iterations):
        for j in range(n_particles):
            # Evaluate score for current particle
            mask = particles[j] > 0
            selected_features = np.where(mask)[0]
            if len(selected_features) == 0:
                score = -np.inf
            else:
                X_selected = X[:, selected_features]
                clf = LinearDiscriminantAnalysis()
                clf.fit(X_selected, y)
                score = clf.score(X_selected, y)

            # Update best particle positions and scores
            if score > best_particle_scores[j]:
                best_particle_scores[j] = score
                best_particle_positions[j] = particles[j]

            if score > global_best_particle_score:
                global_best_particle_score = score
                global_best_particle_position = particles[j]

            # Update velocities and particle positions
            r1, r2 = np.random.rand(), np.random.rand()
            velocities[j] = (w * velocities[j] +
                             c1 * r1 * (best_particle_positions[j] - particles[j]) +
                             c2 * r2 * (global_best_particle_position - particles[j]))
            particles[j] = particles[j] + velocities[j]
            particles[j] = np.clip(particles[j], lb, ub)

    # Select best features
    mask = global_best_particle_position > 0
    selected_features = np.where(mask)[0]

    if len(selected_features) == 0:
        raise ValueError("PSO-LDA failed to select any features")

    X_selected = X[:, selected_features]

    # Train LDA on selected features
    clf = LinearDiscriminantAnalysis()
    clf.fit(X_selected, y)

    return clf, selected_features


# Generate a random classification dataset
X, y = make_classification(n_samples=800, n_features=10, n_informative=5, n_redundant=0, n_clusters_per_class=1,
                           random_state=42)

# Split dataset into training and testing sets
split_idx = int(0.8 * len(X))
X_train, y_train = X[:split_idx], y[:split_idx]
X_test, y_test = X[split_idx:], y[split_idx:]

# Run PSO-LDA feature selection on training set
clf, selected_features = pso_lda(X_train, y_train)

# Test classifier on test set
X_test_selected = X_test[:, selected_features]
test_score = clf.score(X_test_selected, y_test)

# Generate make_classification dataset
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize LDA model and fit to data
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# Make predictions on test data
y_pred = lda.predict(X_test)

# Evaluate accuracy of predictions
accuracy = lda.score(X_test, y_test)
print("Test score without PSOLDA:", accuracy)

print("Selected features:", selected_features)
print("Test score:", test_score)