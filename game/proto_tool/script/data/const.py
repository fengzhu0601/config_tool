
class Const(object):
    '''
    classdocs
    '''


    def __init__(self, module, name, desc, vtype, public):
        '''
        Constructor
        '''
        self.module = module
        self.name = name
        self.desc = desc
        self.fields = []
        self.fieldDict = {}
        self.type = vtype
        self.public = public
        
        
    def addField(self, field):
        self.fields.append(field)
        self.fieldDict[field.name] = field