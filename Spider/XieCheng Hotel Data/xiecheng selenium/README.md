xiecheng
=================================

��Դʱ����Ϣ�ۺ�ƽ̨
--------------------------

##������Ϣ��

����scrapy+selenium����ȥ���ԣ����Ͼ���Ϊ������ȡ�Ͼ��оƵ�Ļ�����Ϣ������Ƶ��������<br />

##ʹ��Python �⣺
1.scrapy�����ϰ�װ������࣬�����������������<br />

2.selenium<br />
����ֱ��ʹ��pip���а�װ<br />

SeleniumҲ��һ������WebӦ�ó�����ԵĹ��ߡ�Selenium����ֱ��������������У������������û��ڲ���һ����<br />


##ʹ������:
1.Chrome����<br />
���ص�ַ��http://npm.taobao.org/mirrors/chromedriver<br />

selenium������Ҫ��������ϵͳ��Ӧ�汾��������õ�ϵͳ��ֱ�ӷ��ʵ��ļ��У������{PYTHON_HOME}/Scripts�ļ�����<br />


##���ݿ⣺

###���ݿ���:xiecheng
1.hotellianjie���洢�Ƶ�url��<br />
```sql
DROP TABLE IF EXISTS `hotellianjie`;
CREATE TABLE `hotellianjie` (
  `guid` varchar(255) DEFAULT NULL,
  `lianjie` varchar(255) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `comm_num` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
2.hotelinfo���Ƶ������Ϣ���ݣ�<br />
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
3.hotelcommentinfo���洢�Ƶ��������ݣ�<br />
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