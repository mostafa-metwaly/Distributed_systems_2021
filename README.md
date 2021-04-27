# Dockerizing simple chatting system 

This is the first assignment  WARM UP:
I have build a simple chatting system using python3 and some dependencies of it using the socket and threading the chatting system is done.
this chatting system consists of a server that handles the connection between the host machine and the clients using the IP address of the host and ports

## What Happens:
the clients are all connected on the same server and when any of them send a message all other clients recieve the same message.
also the server logging have a history of each client connection and dissconnection to it and there IP addresses and Port numbers.

## Implementation:
I have used a static IP address and port number to be used inside the clients and server and then made two files for client and server 
then Implemented them into a docker file with base image of python3 and without any extra addittions, and the image just run the server.py file or client.py
After that I used docker-compose to bulid the two images and connect the server with the clients on the same network and I can from here run multiple client using the same image.

# Running the Files:
to run the chatting system you will need to build the images of server and client images and naming them client:latest and server:latest using 
## building Dockerfile images
```bash
$  docker build --pull --rm -f "Assignment1/client/Dockerfile" -t client:latest "Assignment1/client" 
$  docker build --pull --rm -f "Assignment1/server/Dockerfile" -t server:latest "Assignment1/server" 
```

## building Docker-comopse image

then you have the images you can then run the dockercompose file to connect both of the images 
```bash
$ docker-compose -f "Assignment1/docker-compose.yml" up -d --build
```
## running the chatting system or adding new client
```bash
$ docker-compose run client
```
## Chatting
After adding new client start writing any message and press enter this message will be prodcasted to all running clients.
```bash
write any message you want and Press Enter
```




### Docker-Compose

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about all the features of Compose, see the [list of features](https://docs.docker.com/compose/overview/#features).

By using the following command you can start up your application:

```
docker-compose -f <docker-compose-file> up
```



# Refrences and Useful Material:

[Bind Mounts](https://docs.docker.com/storage/bind-mounts/)
[Writing a proper Dockerfile:](https://docs.docker.com/engine/reference/builder/)

[Docker commands with VScode:](https://github.com/Microsoft/vscode-docker)

[Docker cheat sheet](https://github.com/wsargent/docker-cheat-sheet)

[How to write excellent Dockerfiles](https://rock-it.pl/how-to-write-excellent-dockerfiles/)

