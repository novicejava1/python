import requests

def calculator(firstname, secondname):

    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"fname": firstname,"sname": secondname}

    headers = {
        'x-rapidapi-host': "love-calculator.p.rapidapi.com",
        'x-rapidapi-key': "eafa077e65mshca508cd4fa60020p14fd85jsnc555e158ac3a"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(type(response))
    jsondata = response.json()
    #print(jsondata['percentage'])
    #print(jsondata['result'])
    return jsondata
