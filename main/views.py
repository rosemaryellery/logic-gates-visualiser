from django.shortcuts import render
# from .models import PerceptronModel
from .utils import get_plot
# Create your views here.

def index(request):
    gate_type = 'AND'
    desc = ''
    if request.method == 'POST':
        gate_type = request.POST.get('gate')
    labels = [0, 0, 0, 1]
    if gate_type == 'AND':
        labels = [0, 0, 0, 1]
        desc = 'As shown above, the perceptron model can plot a clear decision boundary for the AND gate as it is linearly-seperable.'
    elif gate_type == 'OR':
        labels = [0, 1, 1, 1]
        desc = 'When trained on an OR gate, the perceptron displays a linear decision boundary.'
    elif gate_type == 'XOR':
        labels = [0, 1, 1, 0]
        desc = 'The possible outputs of an XOR gate are not linearly-seperable, therefore the plot shows no decision boundary. This demonstrates the limitations of using a perceptron model.'
    x_values, y_values, distances_matrix = PerceptronModel(labels)
    chart = get_plot(x_values, y_values, distances_matrix)
    return render(request, 'main/index.html', {'chart':chart, 'gate_type': gate_type, 'desc':desc})
    

def PerceptronModel(labels):
    # import codecademylib3_seaborn
    from sklearn.linear_model import Perceptron
    import matplotlib.pyplot as plt
    import numpy as np
    from itertools import product

    data = [[0, 0], [0, 1], [1, 0], [1, 1]]

    # plt.scatter([point[0] for point in data], [point[1] for point in data], c=labels)
    # plt.show()

    classifier = Perceptron(max_iter = 40)
    classifier.fit(data, labels)
    # print(classifier.score(data, labels))

    # print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]]))

    x_values = np.linspace(0, 1, 100)
    y_values = np.linspace(0, 1, 100)


    point_grid = list(product(x_values, y_values))

    distances = classifier.decision_function(point_grid)

    abs_distances = [abs(point) for point in distances]

    distances_matrix = np.reshape(abs_distances, (100, 100))
    
    return x_values, y_values, distances_matrix