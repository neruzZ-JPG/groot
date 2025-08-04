
import requests  
url = "http://localhost:8080/feature/flagd.evaluation.v1.Service/ResolveBoolean"  # 替换为官方正确端点  
headers = {"Content-Type": "application/json"}  
data = {  
    "flagKey": "adServiceHighCpu",  
    "value": "on",  
    "context": {}  # 按官方要求补充上下文等字段  
}  
response = requests.post(url, headers=headers, json=data)  
print(response)  