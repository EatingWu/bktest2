# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context, render_json
from django.http import HttpResponse
from home_application.models import Mynewinformation


def index(request):
    return HttpResponse("bktest2")

def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def bktest2(request):
    """
    bktest2
    """
    data = Mynewinformation.objects.all()
    return render_mako_context(request, '/home_application/bktest2.html',{'data':data})
    #return render_mako_context(request, '/home_application/bktest2.html')

def submit_info(request):
    #if request.method == "POST":
    #    return HttpResponse('congratulation!')
    name_info = request.POST.get('name_info')
    age_info = request.POST.get('age_info')
    sexy_info = request.POST.get('sexy_info')
    Mynewinformation.objects.create(name=name_info, age=age_info,
                                    sexy=sexy_info)
    return render_json({'result': True})

