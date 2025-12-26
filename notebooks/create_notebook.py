# في نفس المجلد، أنشئ ملف Python جديد باسم create_notebook.py
# وأضف هذا الكود:

import json

# محتوى Notebook أساسي
notebook_content = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# House Price Prediction Project\n",
                "## Project - 1\n",
                "\n",
                "### Objectives:\n",
                "- Load housing dataset\n",
                "- Clean and explore features\n",
                "- Train Linear Regression model\n",
                "- Evaluate using RMSE and R²\n",
                "- Interpret coefficients\n",
                "- Save model and show predictions"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print('✅ Notebook created successfully!')"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# حفظ الملف
with open('house_price_prediction.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=2)

print("✅ تم إنشاء ملف house_price_prediction.ipynb")