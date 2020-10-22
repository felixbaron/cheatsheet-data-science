# export HADOOP_HOME=/home/hadoop
# export HADOOP_INSTALL=$HADOOP_HOME
# export HADOOP_MAPRED_HOME=$HADOOP_HOME
# export HADOOP_COMMON_HOME=$HADOOP_HOME
# export HADOOP_HDFS_HOME=$HADOOP_HOME
# export HDFS_NAMENODE_USER=root
# export DFS_SECONDARYNAMENODE_USER=root
# export HDFS_SECONDARYNAMENODE_USER=root
# export HDFS_DATANODE_USER=root
# export YARN_NODEMANAGER_USER=root
# export YARN_RESOURCEMANAGER_USER=root
# export YARN_HOME=$HADOOP_HOME
# export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
# export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
# export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
export JAVA_HOME=/usr/local/openjdk-8
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/home/hadoop/etc/hadoop"}
