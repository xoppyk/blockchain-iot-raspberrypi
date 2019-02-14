from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from script import *
from graphics import *

app = Flask(__name__)

dificulty = '000'

# ROOT
@app.route('/', methods=['GET'])
def index():
    return view()

# CREATE
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        to_whom = request.form['to_whom']
        data = {
            "name": name,
            "amount": amount,
            "to_whom": to_whom
        }
        create_block("./block/list/", data)
        return view()
    return render_template('./list/create.html', active = 'list')

# VIEW
@app.route('/view', methods=['GET'])
def view():
    values, totals = get_values("./block/list/")
    need_mining = vefirfic_need_mining(values)
    totals['execution_time'] = read_json("./time/time" + str(dificulty.count('0')))['execution_time']
    return render_template('./list/view.html', values = values, need_mining = need_mining, totals = totals, active = 'list' )

# CHECKING
@app.route('/integrity', methods=['GET'])
def integrity():
    results = blockchain_integrity_verification("./block/list/", dificulty = dificulty)
    return render_template('./list/integrity.html', results = results, active = 'list')

# MAINING
@app.route('/maining', methods=['POST'])
def maining():
    execution_time = {}
    folder = request.form['folder']
    path = "./block/" + folder + "/"

    #TIMER
    old_time = read_json("./time/time" + str(dificulty.count('0')))
    start_time = get_time()
    blocks_mined = block_chain_maining(path, dificulty)
    end_time = get_time()
    execution_time['execution_time'] = end_time - start_time + old_time['execution_time']
    write_to_file("./time/time" + str(dificulty.count('0')), execution_time)
    #SYNC
    try:
        sync_with_others(ip = '10.3.141.1', blocks = blocks_mined)
        print("Sync")
    except Exception as e:
        raise
    return redirect(url_for('view'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        amount = request.form['amount']
        name = request.form['name']
        nonce = request.form['nonce']
        prev_hash = request.form['prev_hash']
        to_whom = request.form['to_whom']
        data = {
            "amount": amount,
            "name": name,
            "nonce": int(nonce),
            "prev_hash": prev_hash,
            "to_whom": to_whom
        }
        hash = calculate_hash_of_json_block(data)
        if hash.startswith(dificulty = dificulty):
            create_block("./block/list/", data)
        return "OK"
    return 0
# IOT
@app.route('/iot', methods=['GET', 'POST'])
def iot():
    if request.method == 'POST':
        temp = request.form['temp']
        hum = request.form['hum']
        date = request.form['date']
        time = request.form['time']
        data = {
            "temp": temp,
            "hum": hum,
            "date": date,
            "time": time
        }
        create_block("./block/iot/", data)
        block_chain_maining(path = "./block/iot/", dificulty = dificulty)
        return redirect(url_for('iot'))
    values, totals = get_values("./block/iot/")
    return render_template('./iot/view.html', values=values, totals = totals, active = 'iot')

@app.route('/checking-iot', methods=['GET'])
def check_iot():
    results = blockchain_integrity_verification("./block/iot/", dificulty = dificulty)
    values = get_values("./block/iot/")
    return render_template('./iot/integrity.html', results = results, values=values, active = 'iot')

@app.route('/graphics', methods=['GET'])
def graphics():
    graph_data_size = get_size_graphic()
    graph_data_time = get_time_graphic()
    graph_data_nonce = get_nonce_graphic()
    return render_template('./graphics/statistics.html', graph_data_time = graph_data_time, graph_data_size = graph_data_size, graph_data_nonce = graph_data_nonce, active = 'graphics')
    # return render_template("graphing.html", graph_data = graph_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
