from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canon EOS R8 終極戰情室與選單手冊</title>
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
            font-size: 1.1rem;
            margin-top: 0;
        }
        ul {
            padding-left: 20px;
            margin: 0;
            line-height: 1.7;
        }
        li {
            font-size: 0.92rem;
            margin-bottom: 6px;
        }
        .highlight {
            color: #f1c40f;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>📷 Canon EOS R8 終極指揮中心</h1>

    <!-- 抖音全場景拍攝參數與避坑指南 -->
    <div class="card" style="border-left: 5px solid #e67e22;">
        <h3 style="color: #e67e22;">🔥 R8 全場景拍攝參數與避坑指南</h3>
        <ul>
            <li><b>硬性防抖：</b>R8 無機身防抖，全靠鏡頭 IS；手持快門不慢於焦距倒數，無 IS 鏡頭須提高快門。</li>
            <li><b>閃光燈限制：</b>無內閃須外接；外接閃光燈務必切換為 <span class="highlight">【電子前簾快門】</span>（最高同步 1/200s），純電子快門無法使用閃光燈！</li>
            <li><b>照片風格固定參數：</b>
                <br>• 人像風格：0, 2, 1, 0, -1, 0
                <br>• 風景風格：2, 2, 1, 0, 0, 0
                <br>• 標準風格：0, 0, 0, 0, 0, 0
            </li>
            <li><b>白平衡偏移 (僅對 JPG 生效，RAW 不受影響)：</b>
                <br>• 冷白皮（陰天/樹蔭/窗邊冷光）：<span class="highlight">B3 G1</span>
                <br>• 奶油暖膚（下午夕陽/室內暖燈）：<span class="highlight">A3 M1</span>
            </li>
            <li><b>核心避坑：</b>ISO 盡量控制在 3200 內防噪；明暗變化優先保證安全快門，再調整 ISO。</li>
        </ul>
    </div>

    <!-- Canon EOS R8 選單目錄速查 -->
    <div class="menu-container">
        <h2 style="text-align: center; margin: 20px 0 15px 0; color: #fff;">📑 R8 官方選單設置速查</h2>

        <!-- 🔴 拍攝選單 (SHOOT) -->
        <div class="card" style="border-left: 5px solid #e74c3c;">
            <h3 style="color: #e74c3c;">🔴 拍攝選單 (SHOOT)</h3>
            <ul>
                <li><b>SHOOT 1：</b>影像畫質 (RAW / C-RAW / JPEG)</li>
                <li><b>SHOOT 3：</b>ISO 感光度設定 / 曝光補償</li>
                <li><b>SHOOT 4：</b>相片風格設定 & 白平衡偏移 (WB Shift 調整冷白皮/奶油肌)</li>
                <li><b>SHOOT 6：</b>快門模式設定（外接閃光燈必切「電子前簾」）</li>
                <li><b>SHOOT 8：</b>IS (防手震) 設定 / 數位防手震</li>
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
            <h3 style="color: #2ecc71;">🟢 我的選單 (MY MENU) 推薦配置</h3>
            <ul>
                <li><b>首選 1：</b>格式化記憶卡 (Format)</li>
                <li><b>首選 2：</b>快門模式 (電子前簾 / 純電子切換)</li>
                <li><b>首選 3：</b>白平衡偏移 (快速切換 B3G1 / A3M1)</li>
                <li><b>首選 4：</b>主體偵測 (人物 / 車輛切換)</li>
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