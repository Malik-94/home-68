import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_add(request, *args, **kwargs):
    result = None
    if request.body:
        request_data = json.loads(request.body)
        a = request_data.get('A')
        b = request_data.get('B')
        try:
            a = int(a)
            b = int(b)
            result = a + b
            # data = {
            #     'answer': result
            # }
            return JsonResponse({
                'result' : result
            })
        except ValueError:
            response = JsonResponse({'error': 'Bad request'})
            response.status_code = 400
            return response



@csrf_exempt
def api_subtract(request, *args, **kwargs):
    result = None
    if request.body:
        request_data = json.loads(request.body)
        a = request_data["A"]
        b = request_data["B"]
        result = a - b
    data = {
        'answer': result
    }
    return JsonResponse(data)


@csrf_exempt
def api_multiply(request, *args, **kwargs):
    result = None
    if request.body:
        request_data = json.loads(request.body)
        a = request_data["A"]
        b = request_data["B"]
        result = a * b
    data = {
        'answer': result
    }
    return JsonResponse(data)


@csrf_exempt
def api_divide(request, *args, **kwargs):
    result = None
    if request.body:
        request_data = json.loads(request.body)
        a = request_data["A"]
        b = request_data["B"]
        result = a / b
    data = {
        'answer': result
    }
    return JsonResponse(data)