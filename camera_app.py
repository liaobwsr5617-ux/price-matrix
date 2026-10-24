import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EOS R8 戰情室與選單設定手冊</title>
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: #131c2e;
            --main-color: #00d2ff;
            --accent-color: #ff007f;
            --text-color: #e0e0e0;
            --border-color: #1f3a60;
        }
        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 15px;
            text-align: left;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
        h1 {
            color: var(--main-color);
            font-size: 22px;
            text-align: center;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            color: #888;
            font-size: 13px;
            margin-bottom: 20px;
        }
        .gear-box {
            background: #1a1528;
            border: 1px solid #4a155c;
            padding: 12px 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            font-size: 13px;
        }
        .gear-box b { color: #ff758c; }
        .card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 15px 20px;
            margin-bottom: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .card h2 {
            color: var(--main-color);
            font-size: 18px;
            margin-top: 0;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
        }
        ul {
            padding-left: 20px;
            margin: 8px 0;
            font-size: 14px;
            line-height: 1.6;
        }
        li span {
            color: #00ff66;
            font-weight: bold;
        }
        .warning {
            background: #2e1111;
            border-left: 4px solid #ff4d4d;
            padding: 8px 12px;
            margin-top: 10px;
            font-size: 12px;
            color: #ffb3b3;
            border-radius: 0 4px 4px 0;
        }
        .tip {
            background: #112e1e;
            border-left: 4px solid #00ff66;
            padding: 8px 12px;
            margin-top: 10px;
            font-size: 12px;
            color: #a3ffc9;
            border-radius: 0 4px 4px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📷 EOS R8 實戰參數與選單手冊</h1>
        <div class="subtitle">Cyber Mobile Camera Hub (Pro Edition)</div>

        <div class="gear-box">
            <b>🎒 裝備清單：</b> Canon EOS R8 | RF 24-240mm | RF 50mm f/1.8 | CPL偏光鏡 | 43mm黑柔鏡 | Fotopro腳架
        </div>

        <div class="card">
            <h2>🚨 R8 硬性限制與避坑指南</h2>
            <ul>
                <li>🛡️ 無機身防抖：<span>防抖全靠鏡頭 IS</span>，手持快門切勿低於焦距倒數，無 IS 鏡頭需拉高快門。</li>
                <li>⚡ 閃光燈限制：<span>必須外接閃光燈</span>；快門務必切到「電子前帘快門」（最高同步 1/200s），<span>電子快門無法使用閃光</span>。</li>
                <li>📉 ISO 與曝光：<span>ISO 盡量控制在 3200 內</span>；光線變化時，優先確保安全快門，再調整 ISO。</li>
            </ul>
            <div class="warning">🔥 避坑：使用閃光燈切記用「電子前帘」，用電子快門會導致閃光燈不工作！手持快門建議再提高一檔防糊片。</div>
        </div>

        <div class="card">
            <h2>🎨 照片風格與高級膚色調校</h2>
            <ul>
                <li>🎞️ 照片風格參數：
                    <br>• 👤 人像：<span>0, 2, 1, 0, -1, 0</span>
                    <br>• 🌲 風景：<span>2, 2, 1, 0, 0, 0</span>
                    <br>• ⚖️ 標準：<span>0, 0, 0, 0, 0, 0</span>
                </li>
                <li>☀️ 白平衡偏移（僅對 JPG 生效）：
                    <br>• ❄️ 冷白皮：<span>B3 G1</span>（適合陰天、樹蔭、窗邊冷光）
                    <br>• 🍑 奶油暖膚：<span>A3 M1</span>（適合夕陽、室內暖燈）
                </li>
            </ul>
            <div class="tip">💡 提示：冷白皮避開正午強光；奶油暖膚在冷白光下容易發黃怪異，需注意場景搭配。</div>
        </div>

        <div class="card">
            <h2>🎬 R8 影片與快速鍵設定 (達人精華)</h2>
            <ul>
                <li>⭐ C1 / C2 快捷坑位：
                    <br>• <b>C1 檔位：</b>設定為「高頻幀（慢動作）」快速切換。
                    <br>• <b>C2 檔位：</b>設定為「Canon Log 3（C-Log 3）」保留最大後期空間。
                </li>
                <li>🎙️ 外接麥克風收音：建議切到<b>「手動」</b>，觀察波形在 <b>12 左右</b>，避免過大破音。</li>
                <li>⚡ 實用短片功能：開啟<b>「預錄功能 (Pre-REC)」</b>；短片快門改為全按「開始/停止」。</li>
            </ul>
        </div>

        <div class="card">
            <h2>🌄 1. 風景與戶外大景</h2>
            <ul>
                <li>🎛️ 拍攝模式：<span>M 檔 / Av 檔</span></li>
                <li>🔍 光圈設定：<span>f/8 ～ f/11</span>（畫質最銳利甜頭區）</li>
                <li>🎞️ 感光度：<span>ISO 100</span>（維持最高細緻度）</li>
                <li>🎯 對焦方式：<span>單次 (ONE SHOT) + 畫面1/3處</span></li>
            </ul>
            <div class="tip">💡 技巧：裝上 CPL 消除反光；上腳架務必「關閉鏡頭防手震」並用 2 秒定時快門。</div>
        </div>

        <div class="card">
            <h2>🏙️ 2. 街頭隨拍與人文</h2>
            <ul>
                <li>🎛️ 拍攝模式：<span>Tv 檔（快門先決）或 Auto ISO</span></li>
                <li>🔍 光圈設定：<span>f/1.8 ～ f/2.8 (50mm散景) / f/4 ～ f/5.6 (街景)</span></li>
                <li>⏱️ 快門速度：<span>1/250s ~ 1/500s</span>（日常移動抓拍）</li>
                <li>🎯 對焦方式：<span>伺服 (SERVO) + 臉部/眼睛追蹤</span></li>
            </ul>
        </div>

        <div class="card">
            <h2>🌃 3. 夜景與光影街拍 (黑柔鏡)</h2>
            <ul>
                <li>🎛️ 拍攝模式：<span>M 檔（手動掌控光圈快門）</span></li>
                <li>🔍 光圈設定：<span>f/1.8 ～ f/2.8</span>（最大進光量）</li>
                <li>⏱️ 快門速度：<span>1/60s ~ 1/125s</span>（手持安全快門）</li>
                <li>📏 測光模式：<span>重點測光 / 權衡式高光保護</span></li>
            </ul>
            <div class="tip">💡 技巧：搭配 43mm 黑柔鏡，夜間燈光會產生漂亮的電影感暈散（Diffusion）。</div>
        </div>

        <div class="card">
            <h2>🏃‍♂️ 4. 動態與寵物抓拍</h2>
            <ul>
                <li>🎛️ 拍攝模式：<span>Tv 檔（快門先決）</span></li>
                <li>⏱️ 快門速度：<span>大於等於 1/1000s</span>（凝結奔跑瞬間，極高速運動建議 1/2000s 以上）</li>
                <li>🎯 對焦設定：<span>伺服 (SERVO) + 動物/車輛偵測 + 追焦特性 Case 2</span></li>
            </ul>
        </div>

        <div class="card">
            <h2>🌌 5. 星空與銀河攝影</h2>
            <ul>
                <li>🎛️ 拍攝模式：<span>M 檔（全手動）</span></li>
                <li>🔍 光圈與快門：<span>最大光圈 + 15s ~ 20s</span></li>
                <li>🎞️ 感光度與色溫：<span>ISO 3200 ~ 6400 | WB 3800K</span></li>
            </ul>
            <div class="tip">💡 技巧：手動對焦 (MF) 放大 10 倍對準亮星；務必關閉鏡頭防手震與上三腳架。</div>
        </div>

        <div class="card">
            <h2>🍣 6. 美食與靜物特寫</h2>
            <ul>
                <li>🎛️ 拍攝模式：<span>Av 檔（光圈先決）</span></li>
                <li>🔍 光圈設定：<span>f/2 ～ f/2.8</span>（營造柔和淺景深）</li>
                <li>💡 曝光補償：<span>+0.3 至 +0.7 EV</span>（讓食物看起來更明亮誘人）</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)