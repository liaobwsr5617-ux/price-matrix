from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canon EOS R8 戰情室與選單手冊</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: #121212;
            color: #e0e0e0;
            margin: 0;
            padding: 15px;
        }
        h1 {
            text-align: center;
            color: #ffffff;
            font-size: 1.5rem;
            margin-bottom: 20px;
        }
        .card {
            background-color: #1e1e1e;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        h2, h3 {
            font-size: 1.2rem;
            margin-top: 0;
        }
        ul {
            padding-left: 20px;
            margin: 0;
            line-height: 1.8;
        }
        li {
            font-size: 0.95rem;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>

    <h1>📷 Canon EOS R8 隨身指揮中心</h1>

    <!-- 拍攝場景與設定指南 -->
    <div class="card" style="border-left: 5px solid #9b59b6;">
        <h3 style="color: #9b59b6;">🌟 拍攝場景快速調校</h3>
        <ul>
            <li><b>風景攝影：</b>光圈 f/8 - f/11，ISO 100，使用三腳架與 CPL 濾鏡。</li>
            <li><b>街頭隨拍：</b>快門優先或光圈優先，開啟電子前簾快門降低延遲。</li>
            <li><b>夜景/黑柔霧：</b>搭配 43mm 黑柔霧鏡，控制高光不過曝，手持注意安全快門。</li>
        </ul>
    </div>

    <!-- Canon EOS R8 選單目錄速查 -->
    <div class="menu-container">
        <h2 style="text-align: center; margin: 20px 0 15px 0;">📑 R8 官方選單速查</h2>

        <!-- 🔴 拍攝選單 (SHOOT) -->
        <div class="card" style="border-left: 5px solid #e74c3c;">
            <h3 style="color: #e74c3c;">🔴 拍攝選單 (SHOOT)</h3>
            <ul>
                <li><b>SHOOT 1：</b>影像畫質 (RAW / C-RAW / JPEG)</li>
                <li><b>SHOOT 3：</b>ISO 感光度設定 / 曝光補償</li>
                <li><b>SHOOT 4：</b>相片風格 (Picture Style) / 白平衡 (WB) 與偏移</li>
                <li><b>SHOOT 6：</b>快門模式 (電子前簾 / 純電子)</li>
                <li><b>SHOOT 8：</b>IS (防手震) 設定 / 數位防手震 (Digital IS)</li>
            </ul>
        </div>

        <!-- 🔵 自動對焦 (AF) -->
        <div class="card" style="border-left: 5px solid #3498db;">
            <h3 style="color: #3498db;">🔵 對焦選單 (AF)</h3>
            <ul>
                <li><b>AF 1：</b>AF 動作 (ONE SHOT / SERVO) & 區域 AF 模式</li>
                <li><b>AF 2：</b>要偵測的主體 (人物/車輛/動物/自動) & 眼睛偵測</li>
                <li><b>AF 3：</b>SERVO AF 追焦特性 (Case 1~4 / Auto)</li>
                <li><b>AF 4：</b>觸控及拖曳 AF 設定 (Touch & Drag AF)</li>
            </ul>
        </div>

        <!-- 🟡 系統設定 (SETUP) -->
        <div class="card" style="border-left: 5px solid #f39c12;">
            <h3 style="color: #f39c12;">🟡 系統設定 (SETUP)</h3>
            <ul>
                <li><b>SETUP 1：</b>格式化記憶卡 (Format)</li>
                <li><b>SETUP 3：</b>螢幕 / EVF 亮度與色調設定</li>
                <li><b>SETUP 4：</b>自訂控制按鈕 (Custom Controls) & 轉盤分配</li>
            </ul>
        </div>

        <!-- 🟢 我的選單 (MY MENU) -->
        <div class="card" style="border-left: 5px solid #2ecc71;">
            <h3 style="color: #2ecc71;">🟢 我的選單 (MY MENU) 建議配置</h3>
            <ul>
                <li><b>首選 1：</b>格式化記憶卡 (Format)</li>
                <li><b>首選 2：</b>快門模式 (電子前簾 / 純電子切換)</li>
                <li><b>首選 3：</b>白平衡偏移 / 包夾 (WB Shift/Bkt)</li>
                <li><b>首選 4：</b>要偵測的主體 (人物 / 車輛)</li>
            </ul>
        </div>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return HTML_TEMPLATE

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)