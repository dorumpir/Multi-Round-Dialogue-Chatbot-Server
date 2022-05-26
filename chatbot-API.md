
## API

### Intention
 - POST：/api/v1/nlp/intent
 - Body：
  ```json
  {"query": "sentences"}
  ```
 - Return：
  ```json
  success：
  {"success": 0, "data": "intention as string, for example, photo, dance, chat and etc"}
  error：
  {"success": "other non-zero int", "message": "error info"}
  ```
 - Client Example：
  ```python
  import requests
  root_url = 'http://www.aaa.com:80'
  route = '/api/v1/nlp/intent'

  url = root_url + route
  data = {"query": "sentence"}
  res = requests.get(url, json=data)
  result = res.json()
  ```



### Chat
 - POST：/api/v1/nlp/chat
 - Body：
  ```json
  {"query": "question, i.e. What do you think of ..."}
  ```
 - Return：
  ```json
  success：
  {"success": 0, "data": "answer to the querying question"}
  error：
  {"success": "other non-zero int", "message": "error info"}
  ```
 - Client Example：
  ```python
  import requests
  root_url = 'http://www.aaa.com:80'
  route = '/api/v1/nlp/chat'

  url = root_url + route
  data = {"query": "question"}
  res = requests.get(url, json=data)
  result = res.json()
  ```



### Knowledge Graph
 - Url：
  - Search in all domains: /api/v1/nlp/konwledge
  - Search anime-related knowledge：/api/v1/nlp/konwledge/commic
  - Search cuisine-related knowledge：/api/v1/nlp/konwledge/food
  - Search blockchain-related knowledge：/api/v1/nlp/konwledge/blockchain
 - Body：
  ```json
  {"query": "question, i.e. What is a wallet in blockchain?"}
  ```
 - Return：
  ```json
  Success：
  {"success": 0, "data": "knowkedge description reagrding the question"}
  Error：
  {"success": "other non-zero int", "message": "error info"}
  ```
 - Client Example：
  ```python
  import requests
  root_url = 'http://www.aaa.com:80'
  route = '/api/v1/nlp/knowledge'

  url = root_url + route
  data = {"query": "question"}
  res = requests.get(url, json=data)
  result = res.json()
  ```