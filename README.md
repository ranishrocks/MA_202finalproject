# Computational Physics Simulation: Two-Body Problem

## Overview

This project simulates the motion of two celestial bodies interacting under the influence of gravity using numerical integration. Specifically, it employs the Runge-Kutta method to solve the two-body problem, a core issue in celestial mechanics where analytical solutions are often impractical. Numerical methods are used for accurate simulations of such systems.

## Components

The project is divided into several components, implemented in both C and Python:

### 1. Model

- **C Implementation**: A C structure to store data such as positions, velocities, mass ratio, and eccentricity.
- **Python Implementation**: A Python class `TwoBodyModel` to manage the same data.

### 2. Controller

- **C Implementation**: A C structure and functions to handle parameters (eccentricity, mass ratio) and perform simulations using Euler’s method or the fourth-order Runge-Kutta method.
- **Python Implementation**: A Python class `TwoBodyController` with methods to perform the simulation.

### 3. Application

- **Command-Line Interface**: Allows users to specify simulation parameters (total time `T`, time step `t`, mass ratio, eccentricity, and simulation method). Results are saved in a file named `AnalysisResult.txt`.

### 4. Animation

- **Python Script**: `plot_simulation.py` uses Tkinter to visualize simulation results interactively. It reads from `AnalysisResult.txt` and displays the motion of the celestial bodies.

## Setup

### Prerequisites

- **C Compiler**: Ensure you have a C compiler (e.g., GCC).
- **Python**: Version 3.x with Tkinter library.
