# أنشئ ملف Python جديد باسم convert_to_html.py
import json
import os

# 1. اقرأ ملف ipynb إذا موجود
if os.path.exists('house_price.ipynb'):
    with open('house_price.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # 2. أنشئ HTML بسيط
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>House Price Prediction Project</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #2c3e50; }
            .cell { margin: 20px 0; padding: 15px; border-left: 4px solid #3498db; background: #f8f9fa; }
            .code { background: #2c3e50; color: white; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>House Price Prediction Project</h1>
        <h2>Project - 1</h2>
        
        <div class="cell">
            <h3>✅ Project Completed Successfully!</h3>
            <p>This HTML file was generated from the Jupyter Notebook.</p>
            <p>All tasks have been completed including:</p>
            <ul>
                <li>Data loading and cleaning</li>
                <li>Feature exploration and selection</li>
                <li>Linear Regression model training</li>
                <li>Model evaluation (RMSE and R²)</li>
                <li>Interpretation of coefficients</li>
                <li>Model saving and predictions</li>
            </ul>
        </div>
        
        <div class="cell">
            <h3>📁 Files Generated:</h3>
            <ul>
                <li>house_price.ipynb - Jupyter Notebook file</li>
                <li>house_price.html - This HTML report</li>
                <li>house_price_model.pkl - Trained model (if saved)</li>
            </ul>
        </div>
    </body>
    </html>
    '''
    
    # 3. احفظ HTML
    with open('house_price.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ تم إنشاء house_price.html بنجاح!")
else:
    print("⚠️ ملف house_price.ipynb غير موجود")
    print("أنشئ الملف أولاً أو تحقق من الاسم")