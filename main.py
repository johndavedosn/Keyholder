from flask import Flask, request, jsonify
import Paramify
import sqlite3
from migrations import mig_funcs
config = Paramify.ConfigFile("global_config.json")

db_name = config.load_param("db_name", "", "global_db.db")
run_migs = config.load_param("run_migrations", "", True)
dev_env = config.load_param("dev_env", "", "prod")
if dev_env == "prod":
    token = config.load_param("token", "", None)
    if token == None:
        print("To change your environment from production to development, change the 'dev_env' parameter in your global config file.")
        raise RuntimeError("Production configured environments require a token")
conn = sqlite3.connect(db_name)
cur = conn.cursor()
if run_migs == True:
    with open("./migrations/make_keys_table.sql", "r")as mig_f:
        migs = mig_f.read()
    print("Running migrations...")

    cur.execute(migs)
    strm = Paramify.ConfigStream("global_config.json")
    strm.update_param("run_migrations", False)
app = Flask(__name__)

@app.route("/add-key", methods=["POST"])
def add():
    data = request.get_json()
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    if dev_env == "prod":
        if data["token"] != token:
            return jsonify({"status": 400, "message":"unauthorized"})
        else:
            mig_funcs.add_row([data["key"], data["value"]], cur)
            conn.commit()
            return jsonify({"status":200, "message":"OK"})
    else:
        mig_funcs.add_row([data["key"], data["value"]], cur)
        conn.commit()
        return jsonify({"status":200, "message":"OK"})
@app.route("/get-key", methods=["POST"])
def get_key():
    data = request.get_json()
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    if dev_env == "prod":
        if data["token"] != token:
            return jsonify({"status": 400, "message":"unauthorized"})
        else:
            cur.execute(f"SELECT key_value FROM keys WHERE key_name=\"{data["name"]}\"")
            rows = cur.fetchall()
            return jsonify({"status": 200, "message": rows})
    else:
            cur.execute(f"SELECT key_value FROM keys WHERE key_name={data["name"]}")
            rows = cur.fetchall()
            return jsonify({"status": 200, "message": rows})
@app.route("/remove-key", methods=["POST"])
def remove_key():
    data = request.get_json()
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    if dev_env == "prod":
        if data["token"] != token:
            return jsonify({"status": 400, "message":"unauthorized"})
        else:
            mig_funcs.remove_row(data["name"], cur)
            conn.commit()
            return jsonify({"status":200, "message": "OK"})
    else:
        mig_funcs.remove_row(data["name"], cur)
        conn.commit()
        return jsonify[{"status": 200, "message": "OK"}]
                    
app.run(host="192.168.8.100", port=8080, debug=True)