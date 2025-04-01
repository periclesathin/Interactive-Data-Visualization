# Interactive-Data-Visualization

**CS2 Interactive Plots** is a Flask-based web application that dynamically generates interactive charts from JSON data files. The application uses Highcharts for charting, along with jQuery and Select2 for an enhanced user interface.

## Features

- **Dynamic Data Loading:** Reads data from JSON files located in the `json_files` directory. Each JSON file contains entries with a date and a price.
- **Interactive Charts:** Displays two types of charts:
  - A dynamic line chart for comparing data over time with zoom and pan functionalities.
  - A stock chart with event plot lines to highlight significant dates (e.g., CS2 release, in-game events).
- **Multiple Data Selection:** Use the Select2-enhanced dropdown to select one or more data sets (cases) to display.

## Technologies
Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Charting: Highcharts, Highstock

UI Enhancements: jQuery, Select2

## Screenshots
![image](https://github.com/user-attachments/assets/78a3ec50-5ee3-47c2-ac03-e3e9aa66c768)



![image](https://github.com/user-attachments/assets/b82c7ad5-d054-48c5-81a7-eaa74b035419)

At the top, there is a multi-select dropdown (enhanced by Select2) where multiple items or cases can be chosen. Each colored line on the chart corresponds to a selected item, with the X-axis representing the day number and the Y-axis indicating the price in USD. The legend below the chart helps identify each line. Users can zoom in, pan around, and compare different data sets interactively.


