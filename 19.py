from PIL import Image

def create_white_image(width=300, height=100, background_color='white'):
    """Создаёт изображение заданного размера с указанным цветом фона."""
    img = Image.new('RGB', (width, height), background_color)
    return img

if __name__ == "__main__":
    img = create_white_image(300, 100, 'white')
    img.save('output.png')
    print("Изображение 300×100 с белым фоном сохранено как output.png")
