from django.shortcuts import render

from rest_framework.decorators import api_view
#restFramework是django中一个提供API接口的框架
from . import models
from .models import Desk,Rent
from django.http import JsonResponse

# Create your views here.

#没有实现的功能
# #如果没有指定座位，则查询某层楼所有的座位，
# # 如果指定了座位，则返回指定座位的信息
#
# #同理，如果不传入时间，则显示所有时间段的座位
# #如果传入了时间，则显示指定时间段的座位
#
# @api_view(["GET"])
# def get_use_all_seat(request):
#     data=request.GET
#     floor_id = data.get("floor_id")
#     desk_id = data.get("desk_id") #可能为null,未传入指定座位号
#     start_time = data.get("start_time",None)
#     end_time = data.get("end_time")
#     date=data.get("date")
#
#     user_id = request.session.get('name')
#     if start_time == None:
#         query_data={
#             'floor_id':floor_id,
#             'date':date,
#             'start_time__lt':1,
#             'end_time__gt':13,
#             }
#     else:
#         query_data={
#             'floor_id':floor_id,
#             'date':date,
#             'start_time__lt':start_time,
#             'end_time__gt':end_time,
#          }
#
#     data_list =[]
#     if desk_id ==None:           #没有指定桌子编号
#         for i in range(1,3):    #假设每层楼有50张桌子，数量可以修改
#             query_data["seat_id"] =i
#             occupy = Rent.objects.filter(**query_data).filter(status=1)
#             if occupy:
#                 user_id = occupy[0].user_id
#                 start_time = str(occupy[0].start_time)
#                 end_time = str(occupy[0].end_time)
#                 data_list.append({"status":1,"floor_id":floor_id,"seat_id":i,
#                                   "start_time":start_time,
#                                   "end_time": end_time,
#                                   "msg":"该座位已被预约，预约时间段：{}-{}".format(user_id,start_time,end_time)
#                 })
#             else:
#                 data_list.append({"status":0,"floor_id":floor_id,"seat_id":i,
#                                   "start_time":"",
#                                   "end_time": "",
#                                   "msg":"该座位未被预约"
#                 })
#     else:       #查询某一张桌子的状态
#         query_data["seat_id"] = desk_id
#         occupy=Rent.objects.filter(**query_data).filter(status=1)
#         if occupy:
#             user_id = occupy[0].user_id
#             start_time = str(occupy[0].start_time)
#             end_time = str(occupy[0].end_time)
#             data_list.append({"status": 1, "floor_id": floor_id, "seat_id": desk_id,
#                                 "start_time": start_time,
#                                 "end_time": end_time,
#                                 "msg": "该座位已被预约，预约时间段：{}-{}".format(user_id, start_time, end_time)
#                                 })
#         else:
#             data_list.append({"status":0,"floor_id":floor_id,"seat_id":desk_id,
#                                 "start_time":"",
#                                 "end_time": "",
#                                 "msg":"该座位未被预约"
#                                     })
#
#     return render(request, 'seat/base.html', locals())


def search(request):
    user = request.GET.get('No')
    objreturn ={}
    seatsearch = list(models.Desk.objects.values().filter(rent_state=0))
    usersearch = list(models.Rent.objects.values().filter(user_number_id=user))
    print(seatsearch)
    print(usersearch)
    if usersearch == []:
        objreturn['status'] = 1
        objreturn['message'] = seatsearch
        objreturn['rent'] = ''
    else:
        objreturn['status'] = 0
        objreturn['message'] = seatsearch
        objreturn['rent'] = usersearch
    return JsonResponse(objreturn)

#尝试写接口 by chenxinran
#取消预约
def cancel(request):
    user = request.POST.get('No')
    objreturn={}
    usersearch = models.Rent.objects.values().filter(user_number_id=user)
    print(usersearch)
    if usersearch:
        objreturn['status'] = 0
        usersearch.end_time = usersearch.start_time #end_time数据类型只能是整数，故设置为起始时间。 #取消是否代表将整条记录删掉？怎么做？
    else:
        objreturn['status'] = 1
    return JsonResponse(objreturn)

def rent(request):
    #status 0：预约成功 ；1：输入数据有误 ；2：已有其他预约记录 ；3：已被他人预约；4：输入未完整
    userno = request.POST.get('No')
    desk_number = request.POST.get('desk_number')
    start_time0 = request.POST.get('start_time')
    end_time0 = request.POST.get('end_time')
    date0 = request.POST.get('date')
    objreturn ={}
    if userno and desk_number and start_time0 and end_time0 and date:
        if start_time0 < end_time0:
            objreturn['status'] = 1
            return JsonResponse(objreturn)
        usersearch = list(models.Rent.objects.values().filter(user_number_id=userno,status=0))#检查是否有未来的预约
        if usersearch == []:
            objreturn['status'] = 2
            return JsonResponse(objreturn)
        desksearch = list(models.Rent.objects.values().filter(desk_number_id=desk_number,status=0))
        flag1 = 0
        i = 0
        while (i < len(desksearch)):#检查当日的同一位子有预约
            da = desksearch[i]['date']
            if da == date0:
                flag1 = 1
                break
            i = i + 1
        if flag1 == 1:#检查当日的同一位子的预约是否时间冲突
            i = 0
            flag =0
            while (i < len(desksearch)):
                 if desksearch[i]['date'] != date0:
                     continue
                 st = desksearch[i]['start_time'] 
                 ed = desksearch[i]['end_time']
                 if (st > start_time0 & ed < end_time0)|(st < end_time0 < ed)|(st < start_time0 < ed):
                    flag =1
                    break
                 i = i + 1
            if flag == 1:
                objreturn['status'] = 3
                return JsonResponse(objreturn)
            models.Rent.objects.create(user_number_id = userno,desk_number_id =desk_number,start_time =start_time0,end_time =end_time0,date = date0,status = 0)#插入数据
            models.Desk.objects.filter(desk_id=desk_number).update(rent_state = 1)
            desk_choice=list(models.Desk.objects.values('desk_id','floor','plug_state').filter(desk_id=desk_number))
            objreturn['desk_information'] = desk_choice
            objreturn['status'] = 0
            return JsonResponse(objreturn)
    objreturn['status'] = 4
    return JsonResponse(objreturn)

