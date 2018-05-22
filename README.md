# mafengwo
Python爬虫，目标站点www.mafengwo.cn，仅用来练习学习Python和爬虫知识

### 技术：

Python@3.0+

Scrapy@1.5

MongoDB@3.4+

IDE: PyCharm

环境: Conda


### 爬取内容：
#### 功能页1 －目的地
url: `http://www.mafengwo.cn/mdd`

当前页面下的全球目的地
容器选择器: `div.row-state`
目的地链接选择器: `a::attr(href)`

目标值(例如，柬埔寨): `/travel-scenic-spot/mafengwo/10070.html`，所以需要马蜂窝站点的域名

获取到目标值后爬取对应页面，解析页面
提取如下内容：
- 目的页面地址，`url`
- 目的地ID，`stateId`
- 目的地名称（包括中文及英文）, `chineseName`, `englistName`
- 目的地图片地址，`photoUrl`


#### 功能页2－目的地热门城市列表

url: `http://www.mafengwo.cn/mdd/citylist/{{stateId}}.html`
容器选择器：`div.row-placeList`

提取内容：
- 所在国家id, `stateId`
- 热门城市列表id列表, 另外需要存储相关城市汇总信息：
 - state_id
 - 城市页面地址, `url`
 - 城市名称, `chineseName`, `englishName`
 - 城市主图地址, `city_main_photo`
 - 热度(多少人去过), hotIndex
 - 概况, summary
 - top3景点, id 和名称

第一页可以直接爬取，其他分页数据ajax

#### 功能页3 － 城市数据
url: `http://www.mafengwo.cn/travel-scenic-spot/mafengwo/{city_id}.html`
提取内容：
- 城市ID，`city_id`
- 城市图片地址，`photo_url`
- 周边城市信息（ajax)
 - id
 - 主图
 - name
 - url
 - hot_index



先实现上面功能，景点数据后续再爬
#### 功能页4 －目的地景点
url: `http://www.mafengwo.cn/jd/{{stateId}}/gonglve.html`，其中`stateId`为目的地Id

容器选择：`div.row-allScenic`

ajax动态数据


### 项目进度(按功能点实现)
- 国家数据爬取及解析, done
- 热门城市数据爬取及解析, done
- 各个城市数据爬取第一页数据, done
- 城市周边城市，接口数据爬取
- 城市分页数据，接口爬取
- 数据入库
- 景点数据
- 项目重构
