from django.shortcuts import render
from django.http import HttpResponse
from .models import PerceptronModel
from .utils import get_plot
# Create your views here.

def index(response):
    qs = PerceptronModel()
    chart = get_plot(qs.x_values, qs.y_values, qs.distances_matrix)
    return render(response, 'main/index.html', {'chart':chart})