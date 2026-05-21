from flask import Flask, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/image')
def get_image():
    """Генерирует белое изображение 300×100 и возвращает его как PNG."""
    # Создаём изображение
    img = Image.new('RGB', (300, 100), 'white')
    
    # Сохраняем в байтовый поток
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    # Отправляем как HTTP-ответ
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
