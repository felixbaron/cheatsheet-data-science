FROM openjdk:8

USER root

ENV HADOOP_HOME "/root/hadoop"
ENV HIVE_HOME "/root/hive"
ENV PATH "$PATH:$HADOOP_HOME/bin:$HIVE_HOME/bin"

# Install Hive
RUN cd ~ \
  && curl -LO https://downloads.apache.org/hive/stable-2/apache-hive-2.3.7-bin.tar.gz \
  && tar xfvz apache-hive-2.3.7-bin.tar.gz \
  && mv apache-hive-2.3.7-bin/ ~/hive \
  && cd ~/hive \
  && echo "export HIVE_HOME=`pwd`" >> ~/.bashrc

# Install Hadoop
RUN cd ~ \
  && curl -LO https://mirror.synyx.de/apache/hadoop/common/stable/hadoop-3.2.1.tar.gz \
  && tar xfvz hadoop-3.2.1.tar.gz \
  && mv hadoop-3.2.1 hadoop \
  && cd hadoop \
  && echo "export HADOOP_HOME=`pwd`" >> ~/.bashrc

RUN echo "export PATH=/root/hive/bin:/root/hadoop/bin:$PATH" >> ~/.bashrc

# Fix guava version error: https://bit.ly/31xppri
RUN cp /root/hadoop/share/hadoop/common/lib/guava-27.0-jre.jar /root/hive/lib/ \
    && rm /root/hive/lib/guava-14.0.1.jar

# Create Hive directories
# RUN hadoop fs -mkdir /tmp \
RUN hadoop fs -mkdir /root/hive/warehouse \
   && hadoop fs -mkdir -p /root/hive/warehouse \
   && hadoop fs -chmod g+w /tmp \
   && hadoop fs -chmod g+w /root/hive/warehouse 

# Initiate schema
RUN schematool -dbType derby -initSchema
