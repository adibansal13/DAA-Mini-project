# Smart Delivery Route Finder

A Flask-based web application that finds the optimal delivery route between different locations in a city distribution network. The application visualizes the routes on an interactive map and calculates the shortest path between selected locations.

## Features

- Interactive web interface for selecting source and destination points
- Visualization of the city distribution network
- Calculation of shortest paths between locations
- Distance calculation for optimal routes
- Dynamic route highlighting on the map
- Support for multiple waypoints

## Tech Stack

- Python 3.12
- Flask
- Matplotlib
- HTML/CSS
- Bootstrap 5
- JavaScript

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd smart-delivery-route-finder
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install the required packages:
```bash
pip install flask matplotlib
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Select source and destination points from the dropdown menus
4. Click "Find Shortest Route" to calculate and display the optimal path

## Project Structure

```
smart-delivery-route-finder/
├── app.py              # Main Flask application
├── templates/
│   └── index.html     # HTML template
├── static/            # Generated map images
└── README.md
```

## Features Explained

- **Distance Calculation**: Uses a pre-defined distance matrix for calculating optimal routes
- **Visualization**: Dynamic generation of route maps using Matplotlib
- **Intermediate Points**: Supports finding routes through intermediate points for better optimization
- **Real-time Updates**: Map updates dynamically when new routes are calculated

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask framework documentation
- Matplotlib visualization library
- Bootstrap for the UI components