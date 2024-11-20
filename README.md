# 간단한 LB 멤버용 이미지
컨테이너로 동작하는 LB 멤버용 이미지입니다. 앞단에 nginx 같은 것을 두고, 이것에 대한 멤버로 만들 때 사용하면 됩니다.
컨테이너 IP와 호스트명을 출력합니다.

## 이미지 빌드
```bash
docker build -t highsky1/lb-member:1.1 .
```

## 네트워크 생성
```bash
docker network create \
--subnet 192.168.24.0/24 \
--ip-range 192.168.24.0/24 \
--gateway 192.168.24.1 \
front-net
```

## LB 컨테이너 생성
```bash
docker run -d --net front-net --ip 192.168.24.2 -p 80:80 --name=front-lb nginx:1.27.2-alpine
```

## 멤버 컨테이너 생성

```bash
docker run -d --net front-net --ip 192.168.24.11 -p 6001:6001 -e PORT=6001 -h alb-node01 --name=alb-node01 highsky1/lb-member:1.1
```
```bash
docker run -d --net front-net --ip 192.168.24.12 -p 6002:6002 -e PORT=6002 -h alb-node02 --name=alb-node02 highsky1/lb-member:1.1
```
```bash
docker run -d --net front-net --ip 192.168.24.13 -p 6003:6003 -e PORT=6003 -h alb-node03 --name=alb-node03 highsky1/lb-member:1.1
```
