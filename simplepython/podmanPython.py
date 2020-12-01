#!/usr/bin/env python3

import requests
import json
import sys

def podmanInfo(podService, apiContext):
    url = service + "/" + context
    print(url)
    response = requests.get(url)
    print(type(response.text))
    jsonresponse = json.loads(response.text)
    #print(jsonresponse["host"])
    print(jsonresponse["host"]["hostname"])
    print(jsonresponse["host"]["arch"])
    print(jsonresponse["store"]["configFile"])

def podmanContainers(podmanService, apiContext):
    url = service + "/" + context
    response = requests.get(url)
    print(type(response.text))
    jsonresponse = json.loads(response.text)
    #print(jsonresponse[0]["Names"])
    #print(jsonresponse[1]["Names"])
    for eachItem in jsonresponse:
        print(eachItem["Names"])

def podmanImages(podmanService, apiContext):
    url = service + "/" + context
    response = requests.get(url)
    print(type(response.text))
    jsonresponse = json.loads(response.text)
    #print(jsonresponse[0]["Names"])
    #print(jsonresponse[1]["Names"])
    for eachItem in jsonresponse:
        print(eachItem["Names"])

def podmanPullImage(podmanService, apiContext):
    url = service + "/" + context
    print(url)
    headers = {'Content-type': 'application/json'}
    payload = {'reference':'docker.io/library/redis'}
    response = requests.post(url, headers=headers, params = payload)
    #response = requests.post(url, headers=headers, json={'reference': 'mongo'})
    #response = requests.request("POST", url, headers=headers, params=payload)
    print(response.text)

service = "http://localhost:8080/v1.40.0/libpod"
print(service)
#context="info"
context=sys.argv[1]
print(context)

if context == "info":
    print("Retrieve Podman System information")
    podmanInfo(service, context)
elif context == "containers/json?all=true":
    print("Retrieve List of all containers")
    podmanContainers(service, context)
elif context == "images/json":
    print("Retrieve List of all images")
    podmanImages(service, context)
elif context == "images/pull":
    print("Retrieve images from registry")
    podmanPullImage(service, context)
else:
    print("Provide the correct API context to fetch data")

