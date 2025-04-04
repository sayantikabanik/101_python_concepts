# Stock Price Analysis Dashboard

A Python-based dashboard for analyzing stock price data using Kaggle datasets and Bokeh visualization.

## Project Overview

This project demonstrates interactive visualization and analysis tools for stock market data using Python and Bokeh. The data is sourced from Kaggle datasets and processed locally.

## Tools & Technologies

- **Python 3.8+** - Core programming language
- **Jupyter Notebook** - Interactive development environment 
- **Bokeh** - Interactive visualization library
- **Pixi** - Environment and dependency management
- **Kaggle API** - For dataset download

## Project Structure

```
├── dashboard/
│   └── stock_analysis_dashboard.ipynb     # Main dashboard implementation
├── dataset/
│   ├── fetch_online.py                    # Kaggle dataset read & store locally script
│   └── local_TWLO_stock.csv               # csv data
├── 101_python                             # Project configuration
│   └── pixi.toml                          # env source and truth

```

## Setup & Usage

1. Clone the repository

2. Configure Kaggle API credentials:
```sh
export KAGGLE_USERNAME=<your_username>
export KAGGLE_KEY=<your_api_key>
```

3. Install dependencies using Pixi:
```sh 
pixi install
```

4. Download dataset using Pixi task:
```sh
pixi run 101_kaggle_data
```

5. Launch the dashboard:
```sh
pixi run dashboard
```

6. Navigate to `dashboard/stock_analysis_dashboard.ipynb`

## Features

- Interactive stock price visualization
- Technical analysis indicators
- Historical data analysis 
- Export capabilities

## Development

To add new packages or modify existing ones:

1. Activate Pixi environment:
```sh
pixi shell
```

2. Install additional dependencies:
```sh
pixi add <package_name>
```

## License

This project is licensed under the MIT License. See LICENSE file for details.
