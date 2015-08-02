# website

This is a sample website based on django
========================================
1、服务器上面安装数据库MariaDB，就是MySQL<br>
2、服务器上部署nginx+uwsgi+gunicorn能让python的web程序跑起来<br>
3、设计数据库的表<br>
4、写python代码收集服务器的信息并且存到数据库里面<br>
5、前端的html展示，这个牵扯的内容比较多，最好是用现成的框架实现bootstrap+echart<br>

github协作开发步骤：
===================
1、先在github上面fork此项目到自己的github账号里面<br>
2、在本地电脑上面clone一份fork到自己github账号的项目<br>
3、在本地电脑上，基于第二步中clone的项目建立一个dev的branch分支，命令：git branch dev<br>
4、所有的代码编写和修改都在dev分支中进行<br>
5、代码编写或修改完成后，使用git push origin dev，此命令有两个作用：<br>
&nbsp&nbsp①在远程的github上对应的项目中创建dev分支<br>
&nbsp&nbsp②把本地的dev分支的修改提交到github的dev分支中<br>
6、本地master的代码合并，此步骤之前要先做完以下的①和②的步骤<br>
  ①切换到本地master分支，命令为git checkout master<br>
  ②获取远程github中master的最新修改<br>
  git fetch origin master<br>
  git merge origin/master<br>
  ③当本地的master和远程的origin master同步完成之后才可以合并本地dev分支的修改，命令：git merge dev<br>
7、然后本地的master中使用git push origin master，把本地的master修改提交到远程的origin master中，或者是在github上把origin master和origin dev做合并也能达到此效果，在github上如果远程的dev分支有修改会自动提醒要求合并<br>
8、最后在github的master上可以申请pull request请求更新，在收到你的pull request后，我会合并到此项目的最终版本里面（前提是你在第一步中一定是fork了我的项目）<br>
