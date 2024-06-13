### Information about source data and some statistics (maybe plots, tables, images)

### Information about your model, choosen framework, hyperparams) 

### How to install instructions and run your app with virtual environment

### Information about Dockerfile and describe it’s content

Dockerfile stores all the necessary information for docker image.

Comments:

```
FROM ubuntu:22.04 (Base image for docker)
MAINTAINER Nikita Pronin (This is me, the author)
RUN apt-get update -y (Updates the package list to ensure the latest versions of packages are available and accepts all the choices)
COPY . /opt/gsom_project (Current directory is copied to this location)
WORKDIR /opt/gsom_project (This location is set as working directory)
RUN apt install -y python3-pip (Python and pip are installed)
RUN pip3 install -r requirements.txt (All the required libraries are installed for the )
CMD python3 app.py (Docker will run the only process with price predicitons for rent)
```

### How to open the port in your remote VM

Port 5444 is used by default. 

If it is closed and web-service is not availiable, then port can be opened in remote VM with the command.

```
ufw allow 5444
```

Port can be changed in app.py in the last lines of code.

```
if __name__ == '__main__':
    app.run(debug=True, **port=5444**, host='0.0.0.0')
```

### How to run app using docker and which port it uses

Docker imaged can be pulled with this command:

```
docker push altwayme/gsom_project:tagname
```

where tagname should be the latest verions (v.0.4).

---

After that application can be started with this command:

```
sudo docker run --network host -d altwayme/gsom_project:v.0.4
```
