# website

This is a sample website based on django
========================================
##### 1、服务器上面安装数据库MariaDB，就是MySQL
##### 2、服务器上部署nginx+uwsgi+gunicorn能让python的web程序跑起来
##### 3、设计数据库的表
##### 4、写python代码收集服务器的信息并且存到数据库里面
##### 5、前端的html展示，这个牵扯的内容比较多，最好是用现成的框架实现bootstrap+echart

github协作开发步骤：
===================
##### 1、先在github上面fork此项目到自己的github账号里面
##### 2、在本地电脑上面clone一份fork到自己github账号的项目
##### 3、在本地电脑上，基于第二步中clone的项目建立一个dev的branch分支，命令：git branch dev
##### 4、所有的代码编写和修改都在dev分支中进行
##### 5、代码编写或修改完成后，使用git push origin dev，此命令有两个作用:
①在远程的github上对应的项目中创建dev分支<br>
②把本地的dev分支的修改提交到github的dev分支中<br>

##### 6、当github上的dev分支更新之后，需要在github上的dev分支中申请pull request请求更新，这样github中的master分支才能与dev分支保持同步

##### 7、本地master的代码更新有两种办法
一、与远程origin同步，推荐此方法<br>
①切换到本地master分支，命令为git checkout master<br>
②获取远程github中master的最新修改<br>
　git fetch origin master<br>
　git merge origin/master<br>
③当本地的master和远程的origin master同步完成之后才能在本地master分支进行下一次的push操作<br>
二、也可以合并本地dev分支的修改，命令：git merge dev

##### 8、最后在你自己github的master上可以申请pull request请求更新，在收到你的pull request后，我会合并到此项目的最终版本里面（前提是你在第一步中一定是fork了我的项目）
