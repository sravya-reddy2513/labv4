import requests

url = 'https://localhost:6000/predict_api'
r = requests.post(url,json={'Length1':17.5, 'Length2':19,'Length3':21.3  ,'Height':8.3922,'Width':2.9181},verify=False)

print(r.json())