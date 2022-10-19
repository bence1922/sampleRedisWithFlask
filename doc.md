# Documentation of my work 
An addition to README, focused on describing my work.

# Environment
I used Ubuntu 20.04.1 with WSL2, and I used VS Code for coding.

# Screenshots
After the command, you can see that the two containers are running.
![Screenshot 1.](dockerContainers.PNG)
```
workstation@DESKTOP-LS3KC80:~/sampleRedisWithFlask$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                                       NAMES
13054f4cdb96   redislabs/redismod   "redis-server --load…"   2 minutes ago   Up 2 minutes   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   samplerediswithflask-redis-1
5f73081a992d   app_image            "/bin/sh -c 'python …"   2 minutes ago   Up 2 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   samplerediswithflask-web-1
```

## Testing endpoints
I used curl for testing. The screenshot show the correctness of the operation.
![Screenshot 2.](test.PNG)

## Implementation
I would document the more interesting parts of the implementation.
### Get git commit hash
The value of commithash is copied to an environment variable when the image is created. Then, I read it from there when needed with the python script.
### Exception handling
If you try to retrieve the value of the counter earlier than it is set, you will get an error, so I made a simple error handling.

