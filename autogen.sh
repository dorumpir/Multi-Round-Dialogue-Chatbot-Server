git reset --hard HEAD
git pull origin master:master
docker build -t newnlp-server:latest .
docker rm -f nlp-qiantai; docker run -itd --rm --name nlp-qiantai -p 51111:5000 newnlp-server:latest python main_server.py qiantai 
docker rm -f nlp-lucy; docker run -itd --rm --name nlp-lucy -p 52222:5000 newnlp-server:latest python main_server.py lucy 
docker rm -f nlp-chainmaster; docker run -itd --rm --name nlp-chainmaster -p 53333:5000 newnlp-server:latest python main_server.py chainmaster 
docker rm -f nlp-chainmaster-qun; docker run -itd --rm --name nlp-chainmaster-qun -p 54444:5000 newnlp-server:latest python main_server.py chainmaster_qun 

# 重置项目改动，拉取master分支（免密）
# 根据最新代码build镜像
# 对遂于四个项目，分别删除以前的旧容器，部署新容器
