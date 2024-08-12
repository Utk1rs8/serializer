from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.

def student_list(req):
    stu=Student.objects.all()
    serializer =StudentSerializer(stu,many=True)
    return JsonResponse (serializer.data,safe=False)

def student_detail(req,pk):
    user = Student.objects.get(id=pk)
    serializer = StudentSerializer(user)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def list(request):
    if request.method =="GET":
        user = Student.objects.all()
        serializer_data = StudentSerializer(user,many=True)
        # print(serializer_data.data)
        json_data = JSONRenderer().render(serializer_data.data)
        return HttpResponse(json_data,content_type = 'application/json')
    
    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data) 
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')