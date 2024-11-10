from ursina import *
import noise

app = Ursina()

window.vsync = False
window.fps_limit = 60

# Параметры генерации
platform_size = 20  # Размер платформы
scale_factor = 1.1  # Масштаб шума (влияет на "плавность" рельефа)
height_factor = 5   # Масштаб высоты (максимальная высота блока)

# Цветовая палитра для высоты
color_low = color.rgb(0.4, 0.2, 0.1)  # Темный цвет для низких уровней
color_high = color.rgb(0.8, 0.8, 0.6)  # Светлый цвет для высоких уровней

# Массив для хранения высот платформы
height_map = [[0 for _ in range(platform_size)] for _ in range(platform_size)]

# Функция для генерации платформы по шуму
def generate_platform():
    for x in range(platform_size):
        for z in range(platform_size):
            # Генерация высоты для каждой клетки с помощью Perlin шума
            height = noise.pnoise2(x / scale_factor, z / scale_factor, octaves=4, persistence=0.5, lacunarity=2.0) * height_factor
            height = max(0, height)  # Если высота отрицательная, ставим её на 0
            height_map[x][z] = height

# Функция для создания блоков на основе высот
def create_blocks():
    for x in range(platform_size):
        for z in range(platform_size):
            height = height_map[x][z]
            color_factor = min(1, max(0, height / height_factor))  # Нормализуем значение высоты
            color = lerp(color_low, color_high, color_factor)  # Интерполируем между двумя цветами
            
            # Создаём блок с определённой высотой и цветом
            block = Entity(model='cube', color=color, scale=(1, height, 1), position=(x, height / 2, z), collider='box')

# Создание игрока
player = Entity(model='cube', color=color.azure, scale=(1, 1, 1), position=(0, 1, 0), collider='box')

# Настройка изометрической камеры
camera.rotation_x = 30  # угол по оси X (наклон сверху)
camera.rotation_y = 0  # угол по оси Y

# Генерация платформы
generate_platform()

# Создание блоков
create_blocks()

# Управление движением куба на WASD с проверкой коллизий
def update():
    base_speed = 5  # Базовая скорость
    boost_multiplier = 2  # Множитель скорости при зажатом Shift
    speed = base_speed * time.dt
    
    # Если зажат Shift, увеличиваем скорость
    if held_keys['shift']:
        speed *= boost_multiplier
    
    # Определяем направление движения с помощью вектора
    direction = Vec3(
        (held_keys['d'] - held_keys['a']),  # Вправо-влево
        0,  # Движение по оси Y не затрагиваем
        (held_keys['w'] - held_keys['s'])   # Вперёд-назад
    )

    # Нормализация вектора, чтобы скорость оставалась одинаковой при движении по диагонали
    if direction.length() > 0:
        direction = direction.normalized() * speed
    
    # Проверка на коллизии по оси X
    new_position = player.position + direction
    player.position = new_position
    
    # Если столкновение происходит по оси X (влево-вправо)
    if player.intersects():
        # Восстановление позиции до столкновения
        player.position -= direction

    # Камера следит за игроком
    camera.position = Vec3(player.x, 10, player.z - 15)

# Запуск приложения
app.run()
