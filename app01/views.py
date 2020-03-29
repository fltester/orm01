from django.shortcuts import render,HttpResponse
from django.views import View
from app01 import models
# Create your views here.


class QueryView(View):
    def get(self,request):
        # new_obj = models.UserInfo(
        #     #id = 2,
        #     name = "fc",
        #     bday = "2020-03-23",
        #     checked = 1,
        #     sex = 2,
        # )
        # new_obj.save()

        # models.UserInfo.objects.create(
        #         name = "lyj1",
        #         bday = "2020-03-23",
        #         checked = 0,
        #         sex = 2,
        #         #time = datetime.datetime.now(),
        # )
        # ret = models.UserInfo.objects.filter(name__startswith="f").update(
        #     sex = 1,
        # )
        # print(ret)
        #ret.delete()


        #批量插入
        # obj_list = []
        # for i in range(20):
        #     obj = models.Book(
        #         title = f"JPM{i}",
        #         price = 20+i,
        #         publish = "24"
        #     )
        #     obj_list.append(obj)
        # models.Book.objects.bulk_create(obj_list)

        #查询
        # ret1 = models.Book.objects.all()
        # ret2 = models.Book.objects.filter(id=1)
        # print(ret1)
        # print(ret2)



        #多表添加
        #一对一增加
        # 一对多和一对一写法一样
        #au_obj = models.AuthorDetail.objects.get(id=4)
        # models.Author.objects.create(
        #     name = "fc",
        #     age = 55,
        #     #两种方式
        #     au_id = 4,
        #     #au = au_obj
        # )
        #一对多和一对一写法一样

        #多对多
        # new_obj = models.Book1.objects.create(
        #     title = "uuuuuu",
        #     price = 7,
        #     publishDate = "2019-08-05",
        #     publishs_id = 3,
        #
        # )
        # new_obj.authors.add(1,4)
        # new_obj.authors.add(*[1, 4])#既可以用id也可以用对象


        #删除
        #一对一
        #models.AuthorDetail.objects.filter(id=3).delete()
        #models.Author.objects.filter(id=2).delete()

        #一对多
        #models.Book1.objects.filter(id=1).delete()

        #多对多
        book_obj = models.Book1.objects.get(id=9)
        #book_obj.authors.remove(1)#删除指定的一条
        #book_obj.authors.clear()#清除所有的相关数据
        #book_obj.authors.set([1,4])#先清除再添加


        #修改
        # models.Author.objects.filter(id=1).update(
        #     name = "LYJJ"
        # )


        #基于对象的跨表查询
        #查询
        #一对一
        #正向查询 关系属性写在表1，通过表一查询表2的数据，叫做正向查询，反之叫反向查询
        # obj = models.Author.objects.filter(name="fc")[0]
        # ph = obj.au.telephone #对象.属性
        # print(ph)

        #反向查询
        # obj = models.AuthorDetail.objects.get(telephone="666")
        # na = obj.author.name  #对象.表名
        # print(na)

        #一对多 正向查询
        # obj = models.Book1.objects.get(title="hlm")
        # pna = obj.publishs.name
        # print(pna)

        #一对多反向查询
        # obj = models.Publish.objects.filter(name="大幅度")[0]
        # te = obj.book1_set.all()
        # for i in  te:
        #     print(i.title)
        # print(te)



        #多对多 正向查询
        # obj = models.Book1.objects.filter(title="xyj").first()
        # ret = obj.authors.all()
        # for i in ret:
        #     print(i.name)
        # print(ret)

        #多对多反向查询
        obj = models.Author.objects.filter(name="fc").first()
        ret = obj.book1_set.all()
        for i in ret:
            print(i.title)
        return HttpResponse("ok")