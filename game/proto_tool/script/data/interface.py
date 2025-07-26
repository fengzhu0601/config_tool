
class Interface(object):
    '''
    classdocs
    '''


    def __init__(self, module, name, desc,iszip = False):
        '''
        Constructor
        '''
        self.module = module
        self.name = name
        self.desc = desc
        self.zip = iszip
        self.fields = []
        self.fieldDict = {}
        self.cmd = 0
        
        
    def addField(self, field):
        self.fields.append(field)
        self.fieldDict[field.name] = field