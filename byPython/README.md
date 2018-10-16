

## <h3> 描述

## <h3> hadoop 管理节点在存储到 zookeeper 时是使用 protobuf 进行了序列化，所以在使用Python编写程序前，需要安装相应的模块 ,目前只支持获取 active namenode  和  resourcemanager node ，后期我会继续更新 。

## <h3>  流程
* 1. 安装protobuf环境
* 2. proto文件转换
* 3. python取值

## <h3>    部署
 
* 1. 下载protobuf源代码（实例版本：2.5.0）  

```ruby
wget https://protobuf.googlecode.com/files/protobuf-2.5.0.tar.gz 
```

* 2. 解压，编译，安装 

```ruby
yum -y install gcc gcc-c++ libstdc++-devel make build
tar zxvf protobuf-2.5.0.tar.gz 
cd protobuf-2.5.0 
./configure 
make 
make install
```
*  接下来编译python接口的（不需要python接口的请跳过）
```ruby
cd ./python 
python setup.py build 
python setup.py test 
python setup.py install
```
*  验证使用命令 
```ruby
protoc -version
```
*  可是在python 下使用 
```ruby
>>import google.protobuf
```
没有报错，那就是能用了。

*  3.安装完成，验证Linux命令 
```ruby
protoc --version
libprotoc 2.5.0
```
*  4.下载hadoop源码（实例版本：3.1.0）
```ruby
wget http://archive.apache.org/dist/hadoop/core/hadoop-3.1.0-src.tar.gz
```
*  5.生成python 可用py文件

* *    （1）通过 HAZKInfo.proto 获取 hadoop namenode 节点信息
```ruby
        find hadoop-3.1.0 -name "HAZKInfo.proto"
        protoc -I=hadoop-3.1.0-src/hadoop-hdfs-project/hadoop-hdfs/src/main/proto/HAZKInfo.proto --python_out=/root/modules
```  	
* *    （2）通过yarn_server_resourcemanager_service_protos.proto文件获取 yarn resourcemanager 节点信息 依赖文件（yarn_protos.proto，Security.proto）
```ruby
find hadoop-3.1.0 -name "yarn_protos.proto"
find hadoop-3.1.0 -name "Security.proto"
find hadoop-3.1.0 -name "yarn_server_resourcemanager_service_protos.proto"
        protoc -I=hadoop-3.1.0-src/hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api/src/main/proto/yarn_protos.proto --python_out=/root/modules
        protoc -I=hadoop-3.1.0-src/hadoop-common-project/hadoop-common/src/main/proto/Security.proto --python_out=/root/modules
        protoc -I=hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api/src/main/proto/server/yarn_server_resourcemanager_service_protos.proto --python_out=/root/modules
```
## <h3> 其中-I是source的路径，--python_out表示对应python库的生成路径，然后是对应的proto文件。当然，pb还支持c++和java，修改--python_out即可。


* 6. 执行脚本
```ruby
python zk.py 
ActiveNamenode : namenode-1001.localhost
ActiveRMID : rm1
```

