default:
	make init
	docker-compose run --rm init-sonar

init:
ifeq (,$(wildcard .env))
	touch .env
endif

scan:
	docker-compose build sonar-scanner
	docker-compose run --rm sonar-scanner