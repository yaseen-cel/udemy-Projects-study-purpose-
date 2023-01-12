from django.http import HttpResponse

class MiddleWareLifeCycle:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        print('Before the view is excecuted')
        response = self.get_response(request)
        print('after the view is excecuted')
        return response

class ExceptionHandlingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        return self.get_response(request)
    def process_exception(self,request,exception):
        print(exception)
        return HttpResponse('<b>We are running in to a problem, Please check after sometimes</b>')