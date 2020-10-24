FROM openjdk:8

RUN apt-get update -y \
    && apt-get upgrade -y

# Install SSH
RUN apt-get install -y openssh-server openssh-client

# Passwordless SSH
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Download Hadoop
RUN curl -LO https://downloads.apache.org/hadoop/common/stable/hadoop-3.2.1.tar.gz \
    && tar xvzf hadoop-3.2.1.tar.gz \
    && mv hadoop-3.2.1 /home/hadoop

# TODO: remove ENV, check hadoop-env.sh
ENV HADOOP_HOME "/home/hadoop"
ENV HADOOP_INSTALL "$HADOOP_HOME"
ENV HADOOP_MAPRED_HOME "$HADOOP_HOME"
ENV HADOOP_COMMON_HOME "$HADOOP_HOME"
ENV HADOOP_HDFS_HOME "$HADOOP_HOME"
ENV HDFS_NAMENODE_USER "root"
ENV DFS_SECONDARYNAMENODE_USER "root"
ENV HDFS_SECONDARYNAMENODE_USER "root"
ENV HDFS_DATANODE_USER "root"
ENV YARN_NODEMANAGER_USER "root"
ENV YARN_RESOURCEMANAGER_USER "root"
ENV YARN_HOME "$HADOOP_HOME"
ENV HADOOP_COMMON_LIB_NATIVE_DIR "$HADOOP_HOME/lib/native"
ENV PATH "$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin"
ENV HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
ENV JAVA_HOME "/usr/local/openjdk-8"

COPY mapred-site.xml $HADOOP_HOME/hadoop/mapred-site.xml
COPY hdfs-site.xml $HADOOP_HOME/etc/hdfs-site.xml
COPY core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
COPY yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml
COPY hadoop-env.sh $HADOOP_HOME/etc/hadoop/hadoop-env.sh

# RUN hadoop fs -mkdir -p /home/hadoop/hadooptmpdata
# RUN hadoop fs -mkdir -p /home/hadoop/hdfs/namenode
# RUN hadoop fs -mkdir -p /home/hadoop/hdfs/datanode

ENTRYPOINT service ssh start \
    && hdfs namenode -format \
    && $HADOOP_HOME/sbin/start-dfs.sh \
    && $HADOOP_HOME/sbin/start-yarn.sh \
    && hadoop fs -mkdir -p /home/hadoop/hdfs/datanode \
    && hadoop fs -mkdir -p /home/hadoop/hdfs/namenode \
    && hadoop fs -mkdir -p /home/hadoop/hadooptmpdata \
    && while true; do sleep 1000; done

# See https://stackoverflow.com/a/28214133/11773883
# TODO: check if better https://stackoverflow.com/a/31143261/11773883
EXPOSE 8088 9000 9870 22 9864 9867 8020 9866 9868 8040 50010 9864
