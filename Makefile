default:
	make init
	docker-compose run --rm init-sonar
	docker-compose run --rm sonar-scanner

init:
ifeq (,$(wildcard .env))
	touch .env
	echo "TARGET_PROJECT_LOCAL_PATH=/dev/null" >> .env
endif
