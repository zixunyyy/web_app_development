# 路由設計文件 (Routes Design)

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 任務首頁/清單 | GET | `/` | `templates/index.html` | 顯示所有任務與儀表板 |
| 新增任務頁面 | GET | `/tasks/new` | `templates/tasks/new.html` | 顯示新增任務的表單 |
| 建立任務 | POST | `/tasks/new` | — (重導向至 `/`) | 接收表單並存入資料庫 |
| 編輯任務頁面 | GET | `/tasks/edit/<int:id>` | `templates/tasks/edit.html` | 顯示編輯任務的表單 |
| 更新任務 | POST | `/tasks/edit/<int:id>` | — (重導向至 `/`) | 接收編輯表單並更新紀錄 |
| 更新任務狀態 | POST | `/tasks/<int:id>/status` | — (重導向至 `/`) | 快速切換狀態 (To Do, In Progress, Done) |
| 刪除任務 | POST | `/tasks/<int:id>/delete` | — (重導向至 `/`) | 刪除單筆任務並重導 |

## 2. 每個路由的詳細說明

### 1. 檢視首頁/列表 (GET `/`)
- **輸入**：無（可接 URL query parameters 例如 `?status=` 作為欄位過濾，選配）
- **處理邏輯**：呼叫 `Task.get_all()` 或帶過濾條件的查詢，撈取所有紀錄
- **輸出**：渲染 `index.html`，傳入含有所有任務清單變數 `tasks`
- **錯誤處理**：無特別錯誤，若無資料則前端顯示空狀態提示

### 2. 新增任務頁面 (GET `/tasks/new`)
- **輸入**：無
- **處理邏輯**：無特殊邏輯，僅回傳頁面
- **輸出**：渲染 `tasks/new.html`，提供填寫標題、日期、優先級、描述等欄位

### 3. 建立任務 (POST `/tasks/new`)
- **輸入**：HTML 表單資料 (`title`, `description`, `status`, `priority`, `due_date`, `tags`)
- **處理邏輯**：
  1. 驗證必填欄位 (例如 title 是否存在)
  2. 呼叫 `Task.create(...)` 並寫入 SQLite
- **輸出**：重導向至首頁 (`redirect('/')`)
- **錯誤處理**：若標題為空而發生失敗，重導回表單頁面並利用 Flash 提示錯誤訊息

### 4. 編輯任務頁面 (GET `/tasks/edit/<int:id>`)
- **輸入**：URL 參數 `id`
- **處理邏輯**：呼叫 `Task.get_by_id(id)`，撈出該任務以帶入表單作為預設值
- **輸出**：渲染 `tasks/edit.html`，並且傳入該名單變數 `task`
- **錯誤處理**：若查無此 ID 時回傳 404

### 5. 更新任務 (POST `/tasks/edit/<int:id>`)
- **輸入**：HTML 表單資料，以及 URL 參數 `id`
- **處理邏輯**：呼叫 `Task.get_by_id(id)` 取出原始物件，進行欄位檢查後，呼叫 `task.update(...)`
- **輸出**：成功後重導向至首頁 (`redirect('/')`)
- **錯誤處理**：查無 ID 回傳 404，資料內容驗證失敗則重新渲染錯誤表單或返回 Flash 訊息

### 6. 更新任務狀態 (POST `/tasks/<int:id>/status`)
- **輸入**：隱藏表單資料 (`status`)，以及 URL 參數 `id`
- **處理邏輯**：主要由清單上的快速切換按鈕或下拉選單直接觸發，單純改變該紀錄狀態欄。
- **輸出**：成功後重導回原頁首頁 (`redirect('/')`)
- **錯誤處理**：查無此 ID 回傳 404；若傳入狀態值不在三種規定範圍則視為無效請求

### 7. 刪除任務 (POST `/tasks/<int:id>/delete`)
- **輸入**：URL 參數 `id`
- **處理邏輯**：取得指定任務後並呼叫 `task.delete()`
- **輸出**：刪除成功後同樣重導向至首頁 (`redirect('/')`)
- **錯誤處理**：查無此 ID 時回傳 404

## 3. Jinja2 模板清單

所有的模板將繼承自一個基礎共用的佈局版型。

- `templates/base.html`
  - 角色：基礎共用版型 (Base Template)，包含 `<head>`、頂部 Navbar、依賴的 CSS/JS 標籤載入與共用的頁尾。
- `templates/index.html` 
  - 角色：提供首頁觀測與列出所有對應任務。
  - 功能：包含「新增任務按鈕」、「顯示各任務卡片」、卡片上獨立的「切換狀態或刪除按鈕表單」等元件。
- `templates/tasks/new.html`
  - 角色：負責顯示與組裝新增任務的 `<form>` 表單
- `templates/tasks/edit.html`
  - 角色：負責顯示編輯任務表單 (帶有從後端傳入 `task` 既有資料之預設值)。

## 4. 路由骨架程式碼

已建立於 `app/routes/task_routes.py`，請前往該檔案查看 Blueprint 與各路由函式的簽章與文件宣告。
