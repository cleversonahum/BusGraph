#! /usr/bin/python

graph = {
    'AugustoMontenegro' : [
        {
            'connection' : 'Entroncamento',
            'name' : 'Entroncamento',
            'pounds' : [10,20,30] #Morning, afternoon and night
        },
        {
            'connection' : 'PA_Cabral',
            'name': 'Pedro Álvares Cabral',
            'pounds': [10,20,30]
        }
    ],
    'Entroncamento' : [
        {
            'connection' : 'Bosque',
            'name': 'Bosque',
            'pounds': [10,20,30]
        }
    ],
    'PA_Cabral' : [
        {
            'connection' : 'Dr_Freitas',
            'name' : 'Dr. Freitas',
            'pounds' : [10,20,30]
        }
    ],
    'Bosque' : [
        {
            'connection' : 'Perimetral',
            'name' : "Perimetral",
            'pounds' : [10,20,30]
        },
        {
            'connection' : 'Dr_Freitas',
            'name' : "Dr. Freitas",
            'pounds' : [10,20,30]
        },
        {
            'connection' : 'AntonioBaena',
            'name' : "Antônio Baena",
            'pounds' : [10,20,30]
        }
    ],
    'Dr_Freitas' : [
        {
            'connection' : 'Bosque',
            'name' : "Bosque",
            'pounds' : [10,20,30]
        },
        {
            'connection' : 'PA_Cabral',
            'name' : "Pedro Álvares Cabral",
            'pounds' : [10,20,30]
        }
    ],
    'AntonioBaena' : [
        {
            'connection' : 'Bosque',
            'name' : "Bosque",
            'pounds' : [10,20,30]
        },
        {
            'connection' : 'CasteloBranco',
            'name' : "Castelo Branco",
            'pounds' : [10,20,30]
        }
    ],
    'CasteloBranco' : [
        {
            'connection' : 'AntonioBaena',
            'name' : "Antônio Baena",
            'pounds' : [10,20,30]
        },
        {
            'connection' : 'JoseBonifacio',
            'name' : "José Bonifácio",
            'pounds' : [10,20,30]
        }
    ],
    'JoseBonifacio' : [
        {
            'connection' : 'IgarapeMiri',
            'name' : "Barão Igarapé Mirí",
            'pounds' : [10,20,30]
        },
        {
            'connection' : 'CasteloBranco',
            'name' : "Castelo Branco",
            'pounds' : [10,20,30]
        }
    ],
    'IgarapeMiri' : [
        {
            'connection' : 'UFPA',
            'name' : "UFPA",
            'pounds' : [10,20,30]
        },
        {
            'connection' : 'JoseBonifacio',
            'name' : "José Bonifácio",
            'pounds' : [10,20,30]
        }
    ],
    'Perimetral' : [
        {
            'connection' : 'UFPA',
            'name' : "UFPA",
            'pounds' : [10,20,30]
        },
        {
            'connection' : 'Bosque',
            'name' : "Bosque",
            'pounds' : [10,20,30]
        }
    ],
    'UFPA' : [
        {
            'connection' : 'IgarapeMiri',
            'name' : "Barão de Igarapé Mirí",
            'pounds' : [10,20,30]
        },
        {
            'connection' : 'Perimetral',
            'name' : "Perimetral",
            'pounds' : [10,20,30]
        }
    ]
}

#Buses routes
satelite = ['AugustoMontenegro', 'Entroncamento', 'Bosque', 'AntonioBaena', 'CasteloBranco', 'CasteloBranco', 'JoseBonifacio', 'UFPA']
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


def calculateRote(startPoint, endPoint, route):
    if(validPoints(startPoint, endPoint, route)):
        (start,end) = getIndexInitStop(startPoint, endPoint, route)
        route = route[start:end+1] #slicing just part that contains bus route
        print(route)
        for i in range(0,len(route)-1):
            print(graph[route[i]][route.index(route[i+1])])
            #print(route.index(route[i+1])-1)
            #print(graph[route[i]][0]['pounds'][0])
            #print (graph[route[i]])

calculateRote('AugustoMontenegro', 'UFPA', cn6)