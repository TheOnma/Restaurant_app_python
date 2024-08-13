# Restaurant Invoicing System

## Overview

This project is a graphical user interface (GUI) application for a restaurant invoicing system. It is built using Python's Tkinter library and allows users to select food, drinks, and desserts, calculate the total cost, and generate an invoice. The application features various panels for item selection, cost calculation, and a calculator for convenience.

## Features

- **GUI Design**: A user-friendly interface that makes it easy to select items and generate invoices.
- **Item Selection**: Organized panels for selecting food, drinks, and desserts.
- **Cost Calculation**: Automatic calculation of costs based on selected items, including subtotal, taxes, and total.
- **Disable/Enable Inputs**: Item quantities can be adjusted only if the corresponding item is selected.

## Project Structure

- **Main Application Window**: The primary window is set with a fixed size of 1020x630 pixels and has a burlywood background color. The window title is set as "My Restaurant - Invoicing System".
- **Panels**:
  - **Top Panel**: Displays the title of the application.
  - **Left Panel**: Contains the food, drink, and dessert selection panels, and the cost panel.
  - **Right Panel**: Houses the calculator, invoice, and buttons panel (to be implemented).
- **Item Lists**: Food, drink, and dessert items are listed with corresponding Checkbuttons and input fields for quantities.

## Panels

1. **Top Panel**: 
   - Displays the title "Invoicing System" in a large font.

2. **Left Panel**:
   - **Food Panel**: Contains Checkbuttons for various food items and associated input fields for quantity.
   - **Drink Panel**: Contains Checkbuttons for drink items and associated input fields for quantity.
   - **Dessert Panel**: Contains Checkbuttons for dessert items and associated input fields for quantity.
   - **Cost Panel**: Displays the cost of selected food, drinks, desserts, and calculates subtotal, taxes, and total costs.

3. **Right Panel**:
   - Placeholder panels for calculator, invoice, and buttons (to be implemented).

## Item Selection

- Each item in the food, drink, and dessert lists has an associated Checkbutton and input field:
  - The Checkbutton allows the user to select or deselect an item.
  - The input field is initially disabled and only becomes enabled when the corresponding Checkbutton is selected.
  - By default, all input fields have a value of "0".

## Variables

The following variables are used to store and display costs:

- `food_cost_var`: Stores the cost of selected food items.
- `drink_cost_var`: Stores the cost of selected drink items.
- `dessert_cost_var`: Stores the cost of selected dessert items.
- `subtotal_cost_var`: Stores the subtotal of all items.
- `taxes_cost_var`: Stores the calculated taxes.
- `total_cost_var`: Stores the total cost including taxes.

## Running the Application

### Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed on your system.

### Steps to Run

1. **Install Tkinter**: Tkinter is usually included with Python. If it's not installed, you can install it using `pip`:
   ```bash
   pip install tk
