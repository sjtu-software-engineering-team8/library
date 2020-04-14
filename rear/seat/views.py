from django.shortcuts import render

from rest_framework.decorators import api_view
#restFramework是django中一个提供API接口的框架

from .models import Desk,Rent

# Create your views here.

#如果没有指定座位，则查询某层楼所有的座位，
# 如果指定了座位，则返回指定座位的信息

#同理，如果不传入时间，则显示所有时间段的座位
#如果传入了时间，则显示指定时间段的座位

@api_view(["GET"])
def get_use_all_seat(request):
    data=request.GET
    floor_id = data.get("floor_id")
    desk_id = data.get("desk_id") #可能为null,未传入指定座位号
    start_time = data.get("start_time",None)
    end_time = data.get("end_time")
    date=data.get("date")

    user_id = request.session.get('name')
    if start_time == None:
        query_data={
            'floor_id':floor_id,
            'date':date,
            'start_time__lt':1,
            'end_time__gt':13,
            }
    else:
        query_data={
            'floor_id':floor_id,
            'date':date,
            'start_time__lt':start_time,
            'end_time__gt':end_time,
         }

    data_list =[]
    if desk_id ==None:           #没有指定桌子编号
        for i in range(1,3):    #假设每层楼有50张桌子，数量可以修改
            query_data["seat_id"] =i
            occupy = Rent.objects.filter(**query_data).filter(status=1)
            if occupy:
                user_id = occupy[0].user_id
                start_time = str(occupy[0].start_time)
                end_time = str(occupy[0].end_time)
                data_list.append({"status":1,"floor_id":floor_id,"seat_id":i,
                                  "start_time":start_time,
                                  "end_time": end_time,
                                  "msg":"该座位已被预约，预约时间段：{}-{}".format(user_id,start_time,end_time)
                })
            else:
                data_list.append({"status":0,"floor_id":floor_id,"seat_id":i,
                                  "start_time":"",
                                  "end_time": "",
                                  "msg":"该座位未被预约"
                })
    else:       #查询某一张桌子的状态
        query_data["seat_id"] = desk_id
        occupy=Rent.objects.filter(**query_data).filter(status=1)
        if occupy:
            user_id = occupy[0].user_id
            start_time = str(occupy[0].start_time)
            end_time = str(occupy[0].end_time)
            data_list.append({"status": 1, "floor_id": floor_id, "seat_id": desk_id,
                                "start_time": start_time,
                                "end_time": end_time,
                                "msg": "该座位已被预约，预约时间段：{}-{}".format(user_id, start_time, end_time)
                                })
        else:
            data_list.append({"status":0,"floor_id":floor_id,"seat_id":desk_id,
                                "start_time":"",
                                "end_time": "",
                                "msg":"该座位未被预约"
                                    })

    return render(request, 'seat/base.html', locals())
