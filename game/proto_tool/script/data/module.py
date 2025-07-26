
class Module(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.requests = []
        self.responses = []
        
        
    def addRequest(self, request):    
        self.requests.append(request)
        
    def addResponse(self, response):
        self.responses.append(response)
    
            