def receive_data(data):
    try:
        with open(data, "r", encoding="utf-8") as source_data:
            content = source_data.read()
        return content
    except IOError as e:
        raise IOError('Не удалось открыть файл: {data}') from e
