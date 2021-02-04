PYTHON = python3

build-docker:
	docker build -t bestbuyscrapper .

run-docker:
	docker run -it --name bestbuy-scrapper bestbuyscrapper

clean-docker:
	docker rm bestbuy-scrapper