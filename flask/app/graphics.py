import pygal

def get_size_graphic():
    bar_chart_size = pygal.Bar()
    bar_chart_size.title = 'Tamanho medio por bloco (Bytes)'
    bar_chart_size.add('MD5', [{ 'value': 139, 'label': 'Tamanho da Chave: 128 bits'}])
    bar_chart_size.add('SHA1', [{ 'value': 146, 'label': 'Tamanho da Chave: 160 bits'}])
    bar_chart_size.add('SHA224', [{ 'value': 160, 'label': 'Tamanho da Chave: 224 bits'}])
    bar_chart_size.add('SHA256', [{ 'value': 168, 'label': 'Tamanho da Chave: 256 bits'}])
    bar_chart_size.add('SHA384', [{ 'value': 196, 'label': 'Tamanho da Chave: 384 bits'}])
    bar_chart_size.add('SHA512', [{ 'value': 226, 'label': 'Tamanho da Chave: 512 bits'}])
    bar_chart_size.render()
    return bar_chart_size.render_data_uri()

def get_time_graphic():
    line_chart_time = pygal.Line()
    line_chart_time.title = 'Tempo de Execução (segundos)'
    line_chart_time.x_labels = map(str, range(2, 4))
    line_chart_time.add('MD5', [0.55, 3.67, 167.30])
    line_chart_time.add('SHA1',  [0.368, 9.60, 112.529])
    line_chart_time.add('SHA224', [0.56, 7.757, 69.658])
    line_chart_time.add('SHA256', [0.292, 5.869, 170.487])
    line_chart_time.add('SHA384', [0.342, 5.76, 115.52])
    line_chart_time.add('SHA512', [0.529, 9.91, 191.25])
    line_chart_time.render()
    return line_chart_time.render_data_uri()

def get_nonce_graphic():
    line_chart_nonce = pygal.Line()
    line_chart_nonce.title = 'HASHs Calculadas'
    line_chart_nonce.x_labels = map(str, range(2, 4))
    line_chart_nonce.add('MD5', [2535, 18943, 868258])
    line_chart_nonce.add('SHA1',  [1837, 48624, 577700])
    line_chart_nonce.add('SHA224', [2388, 39200, 354037])
    line_chart_nonce.add('SHA256', [1176, 29607, 870788])
    line_chart_nonce.add('SHA384', [1219, 1219, 571984])
    line_chart_nonce.add('SHA512', [2174, 47489, 922953])
    line_chart_nonce.render()
    return line_chart_nonce.render_data_uri()
