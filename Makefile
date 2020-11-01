NAME=flaskapp

run:
	docker-compose build
	docker-compose up -d

stop:
	docker-compose stop

start:
	docker-compose up -d

rm:
	docker-compose rm
