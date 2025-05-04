from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def hello(request):
    return HttpResponse("하이용")

def hi(request):
    return HttpResponse("안녕하세요")

def whoyouare(request):
    return HttpResponse("나는 배진석이에요")

def jsonhello(request):
    return JsonResponse({'message' : '안녕하세요'}, 
                        json_dumps_params={'ensure_ascii': False},
                        content_type='application/json; charset=utf-8',
     )
@csrf_exempt
def post_hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return JsonResponse(
            {'message' : f'{name}님 안녕하세요!'}, 
            json_dumps_params={'ensure_ascii': False}, 
            content_type='application/json; charset=utf-8',
        )
    else:
        return JsonResponse(
            {'error' : 'post 요청이 아닙니다.'}, 
            json_dumps_params={'ensure_ascii': False}, 
            content_type='application/json; charset=utf-8',
        )