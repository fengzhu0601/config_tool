
class Struct(object):
    '''
    classdocs
    '''


    def __init__(self, module, name, desc="", cmd = 0,iszip = False):
        '''
        Constructor
        '''
        self.module = module
        self.name = name
        self.desc = desc
        self.cmd = cmd
        self.zip = iszip
        self.fields = []
        self.fieldDict = {}
        
        
    def addField(self, field):
        self.fields.append(field)
        self.fieldDict[field.name] = field
        