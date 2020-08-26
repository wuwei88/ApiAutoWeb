# -*- coding: utf-8 -*-
from application import app
from controllers.index import index_page
from controllers.member import member_page
from controllers.projectManage import project_page
from common.libs.UrlManager import UrlManager

'''
蓝图
'''
app.register_blueprint(index_page, url_prefix='/')
app.register_blueprint(member_page, url_prefix='/')
app.register_blueprint(project_page, url_prefix='/')
'''
模板函数
'''
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
