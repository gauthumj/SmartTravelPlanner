import requests
'''
python file containing function to find distance between two places(calc_dist())
and function to find route with the shortest paths(NextNode())
***uncomment the lines to run sample***
'''
def calc_dist(place1,place2):
    url = 'https://www.distance24.org/route.json?stops='+place1+'|'+place2
    req = requests.get(url)
    a = req.json()
    dist = int()
    for key,value in a.items():
        if key=='distance':
            dist = value
    return dist


STACK = []
final = dict()

def NextNode(placenode:str,Places):
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
            NextNode(temp1,Places)
        else:
            final[placenode] = Places[0]
            STACK.append(Places[0])
    return final,STACK

# Places = ['chennai','mumbai','goa','delhi','kolkata']  # temporary values
# route1,route2 = NextNode(Places[0],Places)
# print(route1)
# print(route2)