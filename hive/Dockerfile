FROM openjdk:8

USER root

ENV HADOOP_HOME "/root/hadoop"
ENV HIVE_HOME "/root/hive"
ENV PATH "$PATH:$HADOOP_HOME/bin:$HIVE_HOME/bin"

# Install Hive
RUN cd ~ \
  && curl -LO https://downloads.apache.org/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz \
  && tar xfvz apache-hive-3.1.2-bin.tar.gz \
  && mv apache-hive-3.1.2-bin/ ~/hive

# Install Hadoop
RUN cd ~ \
  && curl -LO https://mirror.synyx.de/apache/hadoop/common/stable/hadoop-3.2.1.tar.gz \
  && tar xfvz hadoop-3.2.1.tar.gz \
  && mv hadoop-3.2.1 hadoop

# Fix guava version error: https://bit.ly/31xppri
RUN cp /root/hadoop/share/hadoop/common/lib/guava-27.0-jre.jar /root/hive/lib/ \
    && rm /root/hive/lib/guava-19.0.jar

# Create Hive directories
# RUN hadoop fs -mkdir /tmp \
RUN hadoop fs -mkdir /root/hive/warehouse \
   && hadoop fs -mkdir -p /root/hive/warehouse \
   && hadoop fs -chmod g+w /tmp \
   && hadoop fs -chmod g+w /root/hive/warehouse

# Initiate schema
RUN schematool -dbType derby -initSchema
CMD hiveserver2
