# Install Hadoop on Docker

Build image

```shell
docker build -t hadoop:latest .
docker container run hadoop -p 8088 5070
docker run -it hadoop
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
