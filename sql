
1、创建并导入数据库
#Perform the initial MySQL setup

a)[root@localhost ~]# mysql_install_db
b)[root@localhost ~]# chkconfig --level 2345 mysqld on
c)[root@localhost ~]# service mysqld start
d)[root@localhost ~]# mysql_secure_installation
o Press Enter for current password
o Type a password for the 'root' user [password]
o Re-enter your new 'root' password
o Y to remove anonymous user
o Y to disallow remote logon
o Y to remove the test database
o Y to reload the privilege tables
 

2、修改MySQL root用户密码(默认密码为空) 
#mysqladmin -u root -p password admin123 
测试能否正常登陆数据库 #mysql -uroot -padmin123

3、建website库和添加Mysql用户
mysql> create database website character set utf8 collate utf8_bin;
mysql> grant all on website.* to 'website'@'%' identified by 'admin123';
mysql> flush privileges;

4、修改Model后可以在不影响现有数据的前提下重建表结构
# python manage.py makemigrations
# python manage.py migrate