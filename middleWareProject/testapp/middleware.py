class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        #print('This line is printed at preproceesing of request')
        response = self.get_response(request)
        #print('This line is printed at post processing of request')
        return response