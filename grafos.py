#! /usr/bin/python

graph = {
    'AugustoMontenegro' : {
        'Entroncamento' : {
            'name' : 'Entroncamento',
            'pounds' : [10,20,30] #Morning, afternoon and night
        },
        'PA_Cabral':{
            'name': 'Pedro Álvares Cabral',
            'pounds': [10,20,30]
        }
    },
    'Entroncamento' : {
        'Bosque' : {
            'name': 'Bosque',
            'pounds': [10,20,30]
        }
    },
    'PA_Cabral' : {
        'Dr_Freitas' : {
            'name' : 'Dr. Freitas',
            'pounds' : [10,20,30]
        }
    },
    'Bosque' : {
        'Perimetral' : {
            'name' : "Perimetral",
            'pounds' : [10,20,30]
        },
        'Dr_Freitas' : {
            'name' : "Dr. Freitas",
            'pounds' : [10,20,30]
        },
        'AntonioBaena' : {
            'name' : "Antônio Baena",
            'pounds' : [10,20,30]
        }
    },
    'Dr_Freitas' : {
        'Bosque' : {
            'name' : "Bosque",
            'pounds' : [10,20,30]
        },
        'PA_Cabral' : {
            'name' : "Pedro Álvares Cabral",
            'pounds' : [10,20,30]
        }
    },
    'AntonioBaena' : {
        'Bosque' : {
            'name' : "Bosque",
            'pounds' : [10,20,30]
        },
        'CasteloBranco' : {
            'name' : "Castelo Branco",
            'pounds' : [10,20,30]
        }
    },
    'CasteloBranco' : {
        'AntonioBaena' : {
            'name' : "Antônio Baena",
            'pounds' : [10,20,30]
        },
        'JoseBonifacio' : {
            'name' : "José Bonifácio",
            'pounds' : [10,20,30]
        }
    },
    'JoseBonifacio' : {
        'IgarapeMiri' : {
            'name' : "Barão Igarapé Mirí",
            'pounds' : [10,20,30]
        },
        'CasteloBranco' : {
            'name' : "Castelo Branco",
            'pounds' : [10,20,30]
        }
    },
    'IgarapeMiri' : {
        'UFPA' : {
            'name' : "UFPA",
            'pounds' : [10,20,30]
        },
        'JoseBonifacio' : {
            'name' : "José Bonifácio",
            'pounds' : [10,20,30]
        }
    },
    'Perimetral' : {
        'UFPA' : {
            'name' : "UFPA",
            'pounds' : [10,20,30]
        },
        'Bosque' : {
            'name' : "Bosque",
            'pounds' : [10,20,30]
        }
    },
    'UFPA' : {
        'IgarapeMiri' : {
            'name' : "Barão de Igarapé Mirí",
            'pounds' : [10,20,30]
        },
        'Perimetral' : {
            'name' : "Perimetral",
            'pounds' : [10,20,30]
        }
    }
}

#Buses routes
satelite = ['AugustoMontenegro', 'Entroncamento', 'Bosque', 'AntonioBaena', 'CasteloBranco', 'JoseBonifacio', 'IgarapeMiri', 'UFPA']
cn6 = ['AugustoMontenegro', 'Entroncamento', 'Bosque', 'Perimetral', 'UFPA']
icoaraci = ['AugustoMontenegro', 'PA_Cabral', 'Dr_Freitas', 'Bosque', 'Perimetral', 'UFPA']

#Points
startPoint = 'AugustoMontenegro'
endPoint = 'UFPA'

def validPoints(startPoint, endPoint, route):
    if (startPoint in route) and (endPoint in route):
        return True
    else:
        return False

def getIndexInitStop(startPoint, endPoint, route):
    start = route.index(startPoint)
    end = route.index(endPoint)
    return (start, end)


def calcRoute(startPoint, endPoint, route, shift):
    if(validPoints(startPoint, endPoint, route)):
        (start,end) = getIndexInitStop(startPoint, endPoint, route)
        route = route[start:end+1] #slicing just part that contains bus route
        print(route)
        #defining shift, works as a switch/case 
        poundIndex = {
            'morning': 0,
            'afternoon': 1,
            'night': 2
        }[shift] # default value is 0

        #Sum all route pounds
        pound = 0
        for i in range(0,len(route)-1):
            pound += graph[route[i]][route[i+1]]['pounds'][poundIndex]
        return pound

print(calcRoute('AugustoMontenegro', 'UFPA', icoaraci, 'afternoon'))