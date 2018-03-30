# Find working socks5 proxy

## ENV

- LIMIT [100]: integer - how many proxy to find
- THREADS [50]: integer - treads to check is_alive(proxy)

## RUN

	docker build . --tag find_proxy
	docker run -it --rm -e LIMIT=50 -e THREADS=50 find_proxy
