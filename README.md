#### 使用docker部署web应用

一、确定容器需要和宿主机绑定几个文件目录，方便文件管理
    我这里用到了两处
    1.日志文件目录,方便日志查看，日常维护
          /data/logs/docker:/data/logs/docker
    2.项目代码目录，也是工作目录,方便提交代码
        /data/project:/root/project
    如果项目复杂度增加，可能还需要用到两处
    3.配置文件目录，当然也可以放在工作目录中
        /data/conf:/data/conf
    4.静态文件目录
        /data/static:/data/static
        
二、制作拥有web项目运行所需基础依赖包的镜像
    1.查看本地web运行的沙盒中安装的依赖包
        pip list
    2.根据依赖包，写dockerfile文件，并指定国内源，增加安装速度
        pip install ×× -i https://pypi.tuna.tsinghua.edu.cn/simple/
        注意：a.安装包名称一定要正确，否则创建镜像会失败
             b.需要添加修改系统时区操作。
             c.将创建文件夹，设置时区等操作放在安装依赖前面，减少排错时间。
    3.根据dockerfile文件生成，所有项目通用环境镜像
        docker build -f ./dockerfile -v web-py3:1.0 .
            -f 指定使用的dockerfile文件
            -v 指定生成的镜像名称
   
三、根据新创建的镜像，生成运行web的最终容器
    1.先生成一个数据卷容器，将一中需要绑定的目录都绑定好，方便其他容器挂载数据
        docker run -it --name=web0 -v /data/logs/docker:/data/logs/docker -v /data/project:/root/project web-py3:1.0 /bin/bash
    2.生成最终使用容器
        docker run -id --name=web1 --volumes-from web0 -p 3278:3278 web-py3:1.0 /bin/bash
        注意： 需要指定web服务运行的接口，和宿主机对应端口绑定

四、如果不使用docker-compose,那就直接进入容器启动服务就好，小公司大概率不会使用docker-compose,因为并没有那么多用docker的服务
    1.这里我使用sh脚本，不进入容器启动服务
        docker exec -id web1 bash ~/web1/start.sh
    2.没有sh脚本的情况，只能进入容器，手动执行重启命令