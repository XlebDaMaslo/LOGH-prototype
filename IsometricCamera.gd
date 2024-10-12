extends Camera3D

# Скорость перемещения камеры
var speed = 10.0

func _process(delta):
	var input_direction = Vector3.ZERO

	# Проверяем нажатие клавиш и задаем направление движения
	if Input.is_action_pressed("ui_left"):
		input_direction.x -= 1
	if Input.is_action_pressed("ui_right"):
		input_direction.x += 1
	if Input.is_action_pressed("ui_up"):
		input_direction.z -= 1
	if Input.is_action_pressed("ui_down"):
		input_direction.z += 1

	# Нормализуем направление, чтобы скорость движения не зависела от количества нажатых клавиш
	input_direction = input_direction.normalized()

	# Перемещаем камеру, но с учётом изометрической системы координат
	var move_direction = Vector3(input_direction.x - input_direction.z, 0, input_direction.x + input_direction.z)
	
	# Умножаем направление на скорость и время
	translate(move_direction * speed * delta)
