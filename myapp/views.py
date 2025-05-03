from django.http import HttpResponse
def hello(request):
    return HttpResponse("하이용")

def hi(request):
    return HttpResponse("안녕하세요")

def whoyouare(request):
    return HttpResponse("나는 배진석이에요")