## 简介
- 模仿豆瓣写的读书网站  
- 使用python的django框架  
- 大二小学期的作品  

## 环境配置  
Window10  
Python3.x  
Django2.0  

## 下载运行  
1. ```git clone git@github.com:YJGit/reading_website.git```  
2. 进入reading_website目录，打开命令行，运行```python manage.py runserver 0.0.0.0:8000```  
3. 打开浏览器，输入```http://localhost:8000/```，即可看到网站  

## 问题解决  
1. 问题:   
File "E:\projects\Reading-website\books\models.py", line 53, in UserProfile    
    user = models.OneToOneField(User)  
TypeError: __init__() missing 1 required positional argument: 'on_delete'  
解决:  
将user = models.OneToOneField(User)改为user = models.OneToOneField(User, on_delete=models.DO_NOTHING)  
  
2. 问题：数据同步  
解决：  
python manage.py makemigrations --merge   
python manage.py migrate --fake books  

## 效果图  
首页:  
一  
![](http://ouebtut1h.bkt.clouddn.com/reading_web_index_top.PNG)  
二  
![](http://ouebtut1h.bkt.clouddn.com/reading_web_index_bottom.PNG)  

查找：  
![](http://ouebtut1h.bkt.clouddn.com/reading_web_search.PNG)  

书的详情：  
![](http://ouebtut1h.bkt.clouddn.com/reading_web_book_detail.PNG)  

## 合作者  
马子俊 清华大学软件学院   
于科屹 清华大学软件学院  