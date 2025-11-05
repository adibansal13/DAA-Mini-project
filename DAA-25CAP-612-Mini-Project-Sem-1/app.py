from flask import Flask, render_template, request, url_for
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import os
import time

app = Flask(__name__)

# Predefined distance map (city logistics style)
distances = {
    'Warehouse': {'Depot': 5, 'Supermarket': 9, 'Retail Store': 15, 'Cold Storage': 8, 'Distribution Hub': 12},
    'Depot': {'Warehouse': 5, 'Supermarket': 7, 'Retail Store': 10, 'Cold Storage': 6, 'Distribution Hub': 11},
    'Supermarket': {'Warehouse': 9, 'Depot': 7, 'Retail Store': 4, 'Cold Storage': 5, 'Distribution Hub': 9},
    'Retail Store': {'Warehouse': 15, 'Depot': 10, 'Supermarket': 4, 'Cold Storage': 7, 'Distribution Hub': 6},
    'Cold Storage': {'Warehouse': 8, 'Depot': 6, 'Supermarket': 5, 'Retail Store': 7, 'Distribution Hub': 4},
    'Distribution Hub': {'Warehouse': 12, 'Depot': 11, 'Supermarket': 9, 'Retail Store': 6, 'Cold Storage': 4}
}

# Fixed positions for drawing nodes (map layout)
positions = {
    'Warehouse': (0.1, 0.8),
    'Depot': (0.8, 0.8),
    'Supermarket': (0.1, 0.2),
    'Retail Store': (0.8, 0.2),
    'Cold Storage': (0.45, 0.5),
    'Distribution Hub': (0.45, 0.1)
}

STATIC_MAP_PATH = os.path.join('static', 'map.png')

def draw_map(path):
    plt.figure(figsize=(6,6))
    ax = plt.gca()
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.axis('off')

    # Draw edges and annotate distances
    for u, nbrs in distances.items():
        x1, y1 = positions[u]
        for v, w in nbrs.items():
            x2, y2 = positions[v]
            ax.plot([x1, x2], [y1, y2], color='#cccccc', linewidth=1.2, zorder=1)
            mx, my = (x1 + x2)/2, (y1 + y2)/2
            ax.text(mx, my, f"{w}km", fontsize=9, color='#333', ha='center', va='center', zorder=2, backgroundcolor='white')

    # Highlight chosen path
    if path and len(path) >= 2:
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            ax.plot([x1, x2], [y1, y2], color='green', linewidth=3.5, zorder=3)

    # Draw nodes
    for node, (x,y) in positions.items():
        circle = plt.Circle((x,y), 0.08, color='#007bff', zorder=4,)
        ax.add_patch(circle)
        ax.text(x, y, node, fontsize=8, fontweight='bold', color='white', ha='center', va='center', zorder=5)

    ax.text(0.5, 0.95, 'Delivery Route Map – City Distribution Network', fontsize=12, ha='center', va='center')
    plt.tight_layout()
    os.makedirs('static', exist_ok=True)
    plt.savefig(STATIC_MAP_PATH, dpi=150)
    plt.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find_route', methods=['POST'])
def find_route():
    src = request.form['source']
    dest = request.form['destination']

    if not src or not dest or src == dest:
        result = {'path': 'Invalid: Same Source and Destination', 'distance': 0}
        draw_map([])
        return render_template('index.html', result=result, map_url=url_for('static', filename='map.png', v=int(time.time())))

    routes = list(distances.keys())
    shortest_path_nodes = [src, dest]
    shortest_dist = distances[src].get(dest, float('inf'))

    for mid in routes:
        if mid != src and mid != dest:
            total = distances[src].get(mid, float('inf')) + distances[mid].get(dest, float('inf'))
            if total < shortest_dist:
                shortest_dist = total
                shortest_path_nodes = [src, mid, dest]

    result = {'path': ' → '.join(shortest_path_nodes), 'distance': shortest_dist}
    draw_map(shortest_path_nodes)
    return render_template('index.html', result=result, map_url=url_for('static', filename='map.png', v=int(time.time())))

if __name__ == '__main__':
    app.run(debug=True)