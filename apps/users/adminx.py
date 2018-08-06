__author__ = 'asy'
__data__ = '2018-6-24 11:01'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting():
    enable_themes = True
    use_bootswatch = True


class GlobalSetting():
    site_title = '学到自闭管理系统'
    site_footer = '自闭在线网'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin():
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', ]
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
