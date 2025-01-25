import os

from django.shortcuts import render, HttpResponse
from .models import TodoItem
# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoItemSerializer
import numpy as np
import json
from .dataNormalization.main import get_normalized_data
from tensorflow.keras.models import load_model
from .auxiliaryFunctions.selectTopResult import get_top_ten_result

# Create your views here.
def home(request):
    return render(request, "home.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})


@api_view(['POST'])  # Zmieniono na POST
def get_model_predict(request):
    try:
        # Pobranie danych z ciała zapytania
        data = json.loads(request.body)  # Konwersja JSON na obiekt Python

        # Wyciąganie danych z payloadu
        main_products = data.get('mainProductsInformations', [])
        id_visitor = data.get('idVisitor', [])
        selected_dates = data.get('selectedDateStates', [])
        item_properties = data.get('ItemPropertiesState', [])

        # Przykładowe przetwarzanie danych
        # Tutaj możesz użyć np. `main_products`, `id_visitor`, itp. do obliczeń
        processed_data = {
            "mainProductsLength": len(main_products),
            "visitorCount": len(id_visitor),
            "selectedDatesCount": len([d for d in selected_dates if d is not None]),
            "itemPropertiesShape": [len(item_properties), len(item_properties[0]) if item_properties else 0],
        }

        data_set = get_normalized_data(id_visitor, main_products, item_properties, selected_dates)

        base_dir = os.path.dirname(__file__)

        model_path = os.path.join(base_dir, 'model_storage', 'model.h5')

        model = load_model(model_path)

        prediction = model.predict(data_set)
        print(prediction)

        top_ten_predictions = get_top_ten_result(prediction)

        # predictions = np.random.rand(10, 2).tolist()

        return Response({
            "processedData": processed_data,
            "predictions": top_ten_predictions
        }, content_type="application/json")
        # return Response(predictions, content_type="application/json")


    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON"}, status=400)

    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        items = TodoItem.objects.all()
        serializer = TodoItemSerializer(items, many=True)
        return Response(serializer.data, content_type='application/json')
    
    elif request.method == 'POST':
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        item = TodoItem.objects.get(pk=pk)
    except TodoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoItemSerializer(item)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)