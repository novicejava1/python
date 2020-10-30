import requests

def calculator(firstname, secondname):

    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"fname": firstname,"sname": secondname}

    headers = {
        'x-rapidapi-host': "love-calculator.p.rapidapi.com",
        'x-rapidapi-key': "2a4940fac9msha85bed4cc1c0f92p13c187jsn351142a50d3c"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsondata = response.json()
    return jsondata
