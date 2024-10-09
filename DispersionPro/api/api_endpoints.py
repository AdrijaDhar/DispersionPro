from flask import Flask, request, jsonify
from DispersionPro.core.gaussian_plume import gaussian_plume
from DispersionPro.core.gaussian_puff import gaussian_puff

app = Flask(__name__)

@app.route('/api/gaussian_plume', methods=['POST'])
def gaussian_plume_api():
    data = request.json
    Q = data.get('Q')
    u = data.get('u')
    x = data.get('x')
    y = data.get('y')
    z = data.get('z')
    H = data.get('H')
    sigma_y = data.get('sigma_y')
    sigma_z = data.get('sigma_z')
    
    concentration = gaussian_plume(Q, u, x, y, z, H, sigma_y, sigma_z)
    return jsonify({'concentration': concentration})

@app.route('/api/gaussian_puff', methods=['POST'])
def gaussian_puff_api():
    data = request.json
    Q = data.get('Q')
    t = data.get('t')
    x = data.get('x')
    y = data.get('y')
    z = data.get('z')
    u = data.get('u')
    sigma_x = data.get('sigma_x')
    sigma_y = data.get('sigma_y')
    sigma_z = data.get('sigma_z')
    
    concentration = gaussian_puff(Q, t, x, y, z, u, sigma_x, sigma_y, sigma_z)
    return jsonify({'concentration': concentration})

if __name__ == '__main__':
    app.run(debug=True)
