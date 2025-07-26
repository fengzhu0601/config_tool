
class Field(object):
    '''
    classdocs
    '''


    def __init__(self, name, vtype='', isarray=False, value=0, desc="", imp = ""):
        '''
        Constructor
        '''
        self.name = name
        self.vtype = vtype
        self.isarray = isarray
        self.value = value
        self.desc = desc
        self.imp = imp