#!/bin/sh

docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=microblog -e MYSQL_USER=microblog -e MYSQL_PASSWORD=Willis_27149 mysql/mysql-server:5.7

docker run --name microblog -d -p 80:5000 --rm --link mysql:dbserver -e DATABASE_URL=mysql+pymysql://microblog:Willis_27149@dbserver/microblog microblog:latest