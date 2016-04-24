http://www.jianshu.com/p/a8aad3bf4dc4
## 基本环境搭建

### 创建虚拟环境
	需要安装virtualenv virtualenvwrapper

	```shell
	$ mkvirtualenv tech_blog_all
	# cd tech_blog_all
	```


### 下载依赖
   安装好依赖

   ```shell
   $ pip install -r requirements.txt
   ```


## 创建项目

	```shell
	$ scrapy startproject tech_blog_all
	```

## 定义要抓取的数据

	```python
	import scrapy

	class DmozItem(scrapy.Item):
		title = scrapy.Field()
		link = scrapy.Field()
		desc = scrapy.Field()
	```


	```shell
	scrapy genspider -t basic meituan taobao.org
	```

