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
        new_obj = models.Book1.objects.create(
            title = "uuuuuu",
            price = 7,
            publishDate = "2019-08-05",
            publishs_id = 3,

        )
        new_obj.authors.add(1,4)#既可以用id也可以用对象
        return HttpResponse("ok")