class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        self.reg_response = get_response

    def __call__(self, request):
        print('This line printed at preprocessing of request')
        response = self.reg_response(request)
        print('This line printed at post processing of request')
        return response


from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return HttpResponse('<h1>Application under maintenance. Please try after some time</h1>')

class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        s1 = '<h1>Currently we are facing technical problem. Please try after some time</h1>'
        s2 = '<h2>Raised exception : {}</h2>'.format(exception.__class__.__name__)
        s3 = '<h2>Raised exception Description: {}</h2>'.format(exception)
        return HttpResponse(s1+s2+s3)

