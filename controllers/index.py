# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect
from application import app
from common.libs.Helper import ops_render

index_page = Blueprint("index_page", __name__)


@index_page.route('/')
def index():
    return ops_render('member/login.html')
