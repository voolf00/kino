from django.shortcuts import render_to_response, redirect
from film.models import Film
from django.contrib import auth
from django.core.paginator import Paginator
import datetime

# Create your views here.
