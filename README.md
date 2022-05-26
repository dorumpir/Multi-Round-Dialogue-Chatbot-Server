# Multi-round Dialogue Chatbot Server

## Description

It is a framework of a multi-round dialogue chatbot backend server, supporting intent recognitions, question answering and knowledge graphs and personalized chatbot characters. Notice only the web server provided; models, rules and corpus of textual tasks are emitted. 

## Deploy

### 0. prerequisite
- git
- docker
- mandatory ports not occupied（check autogen.sh 51111 52222 53333 54444）
- Databases: ElasticSearch, Neo4J, MongoDB

### 1. how to use
- pull this project to the server to be deployed
- in the current folder, execute：

``` shell
        bash autogen.sh
```

- The program will exit when finished
- **Notice：when there are updates on git repo，run the above command can pull and deploy automatically**
  - git config required on the target machine，which makes it pull projects without password
  - pull master branch by default，for personalization one can change autogen.sh

### 2. debug
 - by default this project start for container instances (nlp-*)
 - For checking output, execute the following command on deployed machine：

``` shell
        docker logs -f nlp-chainmaster
```
