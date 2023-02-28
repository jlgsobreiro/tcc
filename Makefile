build: stop
	docker build --target front -t rand_chat_front .
	docker build --target back -t rand_chat_back .

start:
	docker compose up

stop:
	docker compose down

volume_create_back:
	docker volume create --driver local --opt type=none --opt device=/Users/jlgs/PycharmProjects/random_chat/back/ --opt o=bind:rw back

volume_create_front:
	docker volume create --driver local --opt type=none --opt device=/Users/jlgs/PycharmProjects/random_chat/front/ --opt o=bind:rw front
