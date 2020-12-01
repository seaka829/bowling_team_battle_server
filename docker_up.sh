#docker-compose down
docker-compose down --rmi all --volumes
docker rmi bowling_app_api
docker-compose up -d db
docker-compose up -d api
docker-compose up -d phpmyadmin
docker-compose up -d ubuntu
