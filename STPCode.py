import requests

def calc_dist(place1,place2):
    url = 'https://www.distance24.org/route.json?stops='+place1+'|'+place2
    req=requests.get(url)
    a = req.json()
    dist = int()
    for key,value in a.items():
        if key=='distance':
            dist = value
    return dist


# class CustomDictionary():
#     def __init__(self):
#         self.type = dict()  # datatype
#
#     def add(self, key, value):  # method to append
#         self[key] = value


Places = ['chennai','mumbai','goa','delhi','kolkata']  # temporary values
STACK = []
final = dict()

def NextNode(placenode):
    temp = dict()
    if placenode not in STACK and len(STACK) != (len(Places)):
        STACK.append(placenode)
        if len(STACK) != (len(Places)):
            for j in range(len(Places)):
                if Places[j] not in STACK:
                    temp[Places[j]]= calc_dist(placenode,Places[j])
            temp1 = min(temp, key=lambda k: temp[k])
            final[placenode]= temp1
            # print(final)
            # print(STACK)
            NextNode(temp1)
        else:
            final[placenode] = Places[0]
    return final,STACK


route1,route2 = NextNode(Places[0])
print(route1)
print(route2)