default:
	make init
	docker-compose run --rm init-sonar
	docker-compose run --rm sonar-scanner

init:
ifeq (,$(wildcard .env))
	touch .env
	echo "TARGET_PROJECT_LOCAL_PATH=/tmp" >> .env
	echo "SONAR_URL=http://sonarqube:9000 >> .env
endif

reset:
	make init
	docker-compose rm -f -s -v
	make

rmi:
	make init
	docker-compose down --remove-orphans -v --rmi "all"
	rm -f .env