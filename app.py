from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    client_ip = request.remote_addr
    reversed_ip = '.'.join(reversed(client_ip.split('.')))
    conn = sqlite3.connect('ips.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS ips (ip TEXT)")
    c.execute("INSERT INTO ips VALUES (?)", (reversed_ip,))
    conn.commit()
    conn.close()
    return f'Your reversed IP is: {reversed_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
