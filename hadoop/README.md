# Install Hadoop on Docker

Build image

# TODO: repair https://haridas.in/bigdata-session-1-hadoop-with-docker.html

```shell
docker build -t hadoop:latest .
docker network create hadoop-nw
docker run --name namenode --network hadoop-nw -p 8088:8088 -p 9000:9000 -p 50010:50010 -p 9870:9870 -p 9864:9864 -p 8020:8020 -p 9867:9867 -p 9866:9866 -p 9868:9686 -p 8040:8040 -p 22:22 hadoop
docker exec -it namenode bash
```

## SSH into Hadoop

You can ssh into the machine as follows:

```shell
docker exec -it hadoop /bin/bash
```

## Resources

[1](https://www.howtoforge.com/how-to-install-and-configure-apache-hadoop-on-ubuntu-2004/)
[2](https://linuxconfig.org/how-to-install-hadoop-on-ubuntu-18-04-bionic-beaver-linux)]
[3](https://phoenixnap.com/kb/install-hadoop-ubuntu)
[4](https://larrylo.gitbooks.io/distribute-cloud-environment-on-ubuntu-14-04-with/content/set_hadoop_environment_in_a_docker_container.html)
[5](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/DockerContainers.html)
[6](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/ClusterSetup.html)
[7](https://github.com/sequenceiq/hadoop-docker)
