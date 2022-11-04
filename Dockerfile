FROM ubuntu
RUN apt-get update
RUN apt-get install nginx -y
CMD ["sleep", "1500"]
