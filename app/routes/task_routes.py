from flask import Blueprint, render_template, request, redirect, url_for, flash
# 需要用到的 Model，此處為假定的 import 路徑
from app.models.task import Task

# 使用 Blueprint 來模組化路由，方便後續擴增時整理程式結構
task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/')
def index():
    """
    任務首頁/清單 (GET)
    呼叫 Task.get_all() 撈取所有資料，並渲染到 index.html
    可在此處理任務列表的過濾(例如: URL參數 `?status=`)
    """
    pass

@task_bp.route('/tasks/new', methods=['GET'])
def new_task_page():
    """
    新增任務頁面 (GET)
    回傳新增任務的空白表單畫面 (tasks/new.html)
    """
    pass

@task_bp.route('/tasks/new', methods=['POST'])
def create_task():
    """
    建立任務 (POST)
    接收表單傳入的欄位 (title, description, status 等) 
    1. 驗證資料後呼叫 Task.create()
    2. 儲存成功後 redirect 至 index
    3. 若資料不完整，可搭配 flash 回到新增頁面
    """
    pass

@task_bp.route('/tasks/edit/<int:id>', methods=['GET'])
def edit_task_page(id):
    """
    編輯任務頁面 (GET)
    依傳入的 ID 從資料庫呼叫 Task.get_by_id(id)
    若存在則渲染 tasks/edit.html，並將原紀錄帶入表單各欄位中
    若不存在引發 404
    """
    pass

@task_bp.route('/tasks/edit/<int:id>', methods=['POST'])
def update_task(id):
    """
    更新任務 (POST)
    接收編輯表單並驗證資料 (例如 title 不可空)
    再呼叫 task.update() 更新到 DB 後 redirect 回 index
    """
    pass

@task_bp.route('/tasks/<int:id>/status', methods=['POST'])
def update_task_status(id):
    """
    更新任務狀態 (POST)
    快速切換任務狀態(例如首頁清單上的捷徑操作)
    接收新的狀態值後更動 DB 並 redirect 回 index
    """
    pass

@task_bp.route('/tasks/<int:id>/delete', methods=['POST'])
def delete_task(id):
    """
    刪除任務 (POST)
    從資料庫中根據傳入的 ID 刪除任務並 redirect 回 index
    """
    pass
