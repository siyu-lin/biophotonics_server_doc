# Introduction to Docker
Credit: This page is adapted from [Docker](docs.docker.com/get-started/overview)

Useful resources: [Docker introductions](https://towardsdatascience.com/how-docker-can-help-you-become-a-more-effective-data-scientist-7fc048ef91d5)

## What is Docker?
Docker is a platform that provides the ability to package and run an application in an **isolated** environment called a _container_. The intuitive way of thinking of a docker is that it can be considered to be an extremely lightweight virtual machine.

## Why Docker?
- Lightweight: The _containers_ contain everything needed to run the application.
- Fast: We can use more of the server capacity
- Portability: Making programs relatively cross-platform, and Sharing and management of projects and environment
- Reproducibility: Easy reinstallation
- Safety: It won't mess up with the sudo access

# Core Docker Architecture
## Docker daemon 
The Docker daemon ```dockerd``` listens to our requests and operates/manages the Docker objects.

## Docker client
The Docker client ```docker``` is basically **us**, which sends commands like ```docker run``` to ```dockerd```.

## Docker image
An image is a read-only template with instructions for creating a Docker container. Usually, an image is based on another image, with possible customization. For instance, we can base our image on the ```pytorch/pytorch``` image that is available to us on DockerHub, then add an additional package to it and run our own Python code. We can download public images from DockerHub, but almost all of the time, we need to make modifications and synthesize our own image with a ```Dockerfile```.

Building an image from a ```Dockerfile```
```
docker image build -t IMAGENAME
```

## Dockerfile
We ```build``` an image from a Dockerfile.

### Example Dockerfile 1 

Assume we have a file structure as follow:
```
/mnt/disk1/Steven_Lin/
|--- helloworld.py
|--- Dockerfile
```
We want to build an _image_ that eventually lets us run the container which executes the ```helloworld.py``` file. 
A simple example of a ```Dockerfile``` that allows us to do that is as followed.
```Dockerfile
FROM python:3.8-slim-buster
WORKDIR /mnt/disk1/Steven_Lin/
COPY  . .
CMD [ "python3", "helloworld.py" ]
```

- ```FROM``` allows us to choose an image that we are building upon
- ```WORKDIR``` allows us to set our current working directory
- ```COPY . .``` here is tricky, the two dots have completely different meaning. The first argument after ```COPY``` represents the path to what we want to copy relative to the ```WORKDIR```. The argument being a dot ```.``` means that we want to copy everything in ```WORKDIR```. The second argument tells us where to paste the copied files. When we build an image, we are not building the image here in our working directory, instead, we are building it 'elsewhere'. The second dot ```.``` means that we are copying everything to that 'elsewhere' directly.
- ```CMD [ "python3", "helloworld.py" ]``` tells the image that we want to execute the ```helloworld.py``` file in the **image directory, i.e., "elsewhere"**. We can execute it because we just copied our file over there.

### Example Dockerfile 2

To consolidate the notion of the two directory. Consider the following Dockerfile that will give us the same result.
```Dockerfile
FROM python:3.8-slim-buster
WORKDIR /mnt/disk1/Steven_Lin/
COPY  helloworld.py /code/
CMD [ "python3", "/code/helloworld.py" ]
```
We explicity copy the ```helloworld.py``` in ```WORKDIR``` into the ```/code/``` folder in our image directory. 
If we now run 
```Dockerfile
CMD [ "python3", "helloworld.py" ]
```
Our ```dockerd``` will not be able to find the ```helloworld.py``` file there anymore. Instead, we need to specify the directory.

## Docker container
A _Docker container_ is a runnable instance of an image. In essence, when we are running a code using Docker, we are actually running the _Docker container_ that contains the code ( and all other required dependencies, commands, etc.).

Ex.

Assume that we have an image called ```my-image```,
```
docker run my-image
```
runs a _container_ that corresponds to this image. 

Some flags that are commonly used with ```docker run```:
- Detach ```-d``` allows us to run the code in the backend, so we can still use our shell/bash for commands. We are also free to sign off and log back in later to check the progress or results.


# General Workflow
## Method I
Pull docker from a standard docker image on [DockerHub](https://login.docker.com/u/login/identifier?state=hKFo2SB0QTJvaGdxZUdvd19HNVlOTnRYQUZFTXVhaFRQbllqRaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIF9hOU9pSEM4Tkh3YUJPVFl2WFl3anRVVXhyaHlKc3p1o2NpZNkgbHZlOUdHbDhKdFNVcm5lUTFFVnVDMGxiakhkaTluYjk) (Sign up an account if needed).

Ex.
```
docker pull pytorch/pytorch:2.1.0-cuda11.8-cudnn8-devel
```

```
docker pull [OPTIONS] NAME[:TAG|@DIGEST]
```

Then, you need to create a container from image:
```
docker run -it [IMAGE-ID]
```

You can find [IMAGE-ID] by:
```
docker images
```

Then, install the packages that you need

Ex.
```
apt update && apt install -y wget unzip curl bzip2 git vim
```

After you make changes to the docker container, you can detach the docker container and commit the changes.

To detach the docker container (when you are in docker) use ```control+p+q``` hotkey.

```
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
```

Example:
```
$ docker images    
REPOSITORY                        TAG                 ID                  CREATED             VIRTUAL SIZE
SvenDowideit/testimage            version3            f5283438590d 

$ docker container ls

$ docker commit containerID  SvenDowideit/testimage:version3
```

After committing the changes, you can push the docker image to your DockerHub account

```
docker push [OPTIONS] NAME[:TAG]
```

Then, you can run your docker.

Some advanced tips for running a docker:

**In the user folder**, create a .bashrc file.

```
touch .bashrc
```

```
vim .bashrc
```

If you need to use multi-gpu processing, you do need to add a large shared memory size ```--shm-size=16g```

```
alias CreateXXXXContainer='docker run -it \
        --gpus all \
        --name Container_Name \
        --hostname USER_NAME \
        --shm-size=16g \ 
        -p 5081:5081 \
        -v /path/to/hostmachine/:/path/inside/docker-container/ \
        [REPOSITORY[:TAG]] \
        /bin/bash'
```

after editing the .bashrc file, update the file

```
source .bashrc
```

Then running the container can use:

```
CreateXXXXContainer
```





## Dealing with Large Dataset
Use the volume ```-v``` flag.


