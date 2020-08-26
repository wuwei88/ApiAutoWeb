# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect
from application import app
from common.libs.Helper import ops_render

project_page = Blueprint("project_page", __name__)


@project_page.route('/projectinfo')
def login():
    return ops_render('/projectManage/projectinfoindex.html')
