# CS F407 AI Project 
|Team Members ID | Names | Email-ID|
|----|---|---|
|2020A7PS0282H <i>(Leader)</i>|Anish Kumar Kallepalli|f20200282@hyderabad.bits-pilani.ac.in|
|2020A7PS1080H|Ashwin Naveen Pugalia|f20201080@hyderabad.bits-pilani.ac.in|
|2020A7PS0273H|Sriram Srivatsan|f20200273@hyderabad.bits-pilani.ac.in|
|2020A7PS0153H|Milind Jain|f20200153@hyderabad.bits-pilani.ac.in|

## Improving Rules of Classifiers using Artificial Intelligence Techniques  
- We have stored all the papers which we have used to implement our codes in [Papers](./Papers/).   

### Algorithms Used:
We have used the following <b>search algorithms</b> in our project:
- <u><b>Genetic Algorithm (GA)</b></u>: We have used GA to improve accuracy of K-Nearest Neighbours(KNN) by selecting a subset of features which gives us the maximum fitness score for classification.
- <u><b>Particle Swarm Optimization (PSO)</b></u>: We have used PSO algorithm to improve accuracy of  Linear Discriminant Analysis(LDA) for multiclass classification problem.
- <u><b>Ant colony optimization (ACO)</u></b>: We have used ACO to improve accuracy of K-Nearest neighbors(KNN) by selecting a subset of features which gives us the maximum fitness score for classification.

In addition to that we have also used:
- <u><b> Bagging classifier</b></u>: We used bagging classifier which is an ensemble technique that uses multiple classifiers and takes multiple subsets of data with replacement and uses voting to decide the outcome. 
- <u><b> Fuzzy K-Nearest neighbor</b></u>: We used fuzzy KNN algorithm as it performs better than generic KNN as The issue with the base KNN classifier is that each sample is given an equal weight. This creates issues in certain situations when sample sets overlap. Whereas, The fuzzy KNN algorithm assigns class membership to a sample vector rather than assigning the vector to a particular class.

### Datasets used:
We have used the dataset <b>breast_cancer</b> which is present in sklearn.datasets as it is a popular choice for training and testing classification models.   

Although we had to use <b>sonar.csv</b> in PSOLDA.


### Analysis and comparative study
In the project we have seen how AI techniques like <b>Genetic Algorithm </b>, <b>Particle Swarm Optimization</b> and <b>Ant colony optimization</b> improve rules for classifiers and even outperform the most popular machine learning techniques like LDA and KNN. We also looked over novel Techniques like bagging classifier and fuzzy KNN which outperforms the baseline classifiers in various aspects. In conclusion, the integration of AI techniques can significantly enhance the accuracy and efficiency of classification rules, leading to better decision-making and improved outcomes in various fields. 
