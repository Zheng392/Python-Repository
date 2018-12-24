xiecheng
=================================

众源时空信息聚合平台
--------------------------

##基本信息：

基于scrapy+selenium的爬去策略，以南京市为例，抽取南京市酒店的基本信息数据与酒店点评数据<br />

##使用Python 库：
1.scrapy，网上安装方法许多，可自行下载相关依赖<br />

2.selenium<br />
可以直接使用pip进行安装<br />

Selenium也是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。<br />


##使用驱动:
1.Chrome驱动<br />
下载地址：http://npm.taobao.org/mirrors/chromedriver<br />

selenium调用需要，需下载系统对应版本，将其放置到系统能直接访问的文件夹，如放在{PYTHON_HOME}/Scripts文件夹中<br />


##数据库：

###数据库名:xiecheng
1.hotellianjie（存储酒店url）<br />
```sql
DROP TABLE IF EXISTS `hotellianjie`;
CREATE TABLE `hotellianjie` (
  `guid` varchar(255) DEFAULT NULL,
  `lianjie` varchar(255) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `comm_num` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
2.hotelinfo（酒店基本信息数据）<br />
```sql
DROP TABLE IF EXISTS `hotelinfo`;
CREATE TABLE `hotelinfo` (
  `guid` varchar(255) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `title` varchar(60) DEFAULT NULL,
  `price` decimal(10,1) DEFAULT NULL,
  `score` int(20) DEFAULT NULL,
  `recommend` varchar(120) DEFAULT NULL,
  `area` varchar(120) DEFAULT NULL,
  `havawifi` varchar(20) DEFAULT NULL,
  `discussNum` int(11) DEFAULT NULL,
  `common_facilities` varchar(500) DEFAULT NULL,
  `activity_facilities` varchar(255) DEFAULT NULL,
  `service_facilities` varchar(255) DEFAULT NULL,
  `room_facilities` varchar(255) DEFAULT NULL,
  `around_facilities` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
3.hotelcommentinfo（存储酒店评论数据）<br />
```sql
DROP TABLE IF EXISTS `hotelcommentinfo`;
CREATE TABLE `hotelcommentinfo` (
  `hotelname` varchar(50) DEFAULT NULL,
  `username` varchar(40) DEFAULT NULL,
  `commentscore` varchar(40) DEFAULT NULL,
  `intime` varchar(40) DEFAULT NULL,
  `tourstyle` varchar(40) DEFAULT NULL,
  `praisenum` int(11) DEFAULT NULL,
  `commenttime` varchar(60) DEFAULT NULL,
  `comment` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```