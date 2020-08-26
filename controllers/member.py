# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect
from application import app
from common.libs.Helper import ops_render

member_page = Blueprint("member_page", __name__)


@member_page.route('/login')
def login():
    return ops_render('member/login.html')


@member_page.route('/register')
def register():
    return ops_render('member/register.html')
