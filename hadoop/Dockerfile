FROM openjdk:8

RUN apt-get update -y \
    && apt-get upgrade -y

RUN apt-get install -y openssh-server openssh-client

RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
RUN service ssh start

RUN service ssh start
RUN curl -LO https://downloads.apache.org/hadoop/common/stable/hadoop-3.2.1.tar.gz \
    && tar xvzf hadoop-3.2.1.tar.gz \
    && mv hadoop-3.2.1 /home/hadoop

# TODO: remove ENV, check hadoop-env.sh
ENV HADOOP_HOME=/home/hadoop
ENV HADOOP_INSTALL=$HADOOP_HOME
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_HOME=$HADOOP_HOME
ENV HADOOP_HDFS_HOME=$HADOOP_HOME
ENV HDFS_NAMENODE_USER=root
ENV DFS_SECONDARYNAMENODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV YARN_NODEMANAGER_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
ENV PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
ENV HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
ENV JAVA_HOME=/usr/local/openjdk-8
ENV HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/home/hadoop/etc/hadoop"}


COPY mapred-site.xml $HADOOP_HOME/hadoop/mapred-site.xml
COPY hdfs-site.xml $HADOOP_HOME/etc/hdfs-site.xml
COPY core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
COPY yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml
COPY hadoop-env.sh $HADOOP_HOME/etc/hadoop/hadoop-env.sh
# RUN cat $HADOOP_HOME/etc/hadoop/hadoop-env.sh >> ~/.bashrc \
#     && /bin/bash -c "source ~/.bashrc"

RUN mkdir -p /home/hadoop/hadooptmpdata
RUN mkdir -p /home/hadoop/hdfs/namenode
RUN mkdir -p /home/hadoop/hdfs/datanode

ENTRYPOINT service ssh start \
    && hdfs namenode -format \
    && $HADOOP_HOME/sbin/start-dfs.sh \
    && $HADOOP_HOME/sbin/start-yarn.sh \
    && while true; do sleep 1000; done

# See https://stackoverflow.com/a/28214133/11773883
# TODO: check if better https://stackoverflow.com/a/31143261/11773883
EXPOSE 8088 50070
