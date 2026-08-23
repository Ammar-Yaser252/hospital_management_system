# Hospital Management System

A desktop application for managing doctors, patients, medical records, and appointments — built with Python and Tkinter, using real-world Object-Oriented Programming principles.

## Features

**Doctor View**
- Select a patient from a list
- Write and save prescriptions directly to a patient's medical record

**Patient View**
- Select yourself as a patient
- Pick a doctor, a date (via calendar widget), and an available time slot
- Book an appointment linking both doctor and patient

## Tech Stack

- **Python 3.13**
- **Tkinter** — GUI framework
- **tkcalendar** — calendar/date-picker widget

## OOP Concepts Demonstrated

- **Inheritance** — `Doctor` and `Patient` both inherit shared attributes from a base `Person` class
- **Encapsulation** — `MedicalRecord` keeps prescription history private, only accessible through controlled methods (`write_prescription`, `get_history`)
- **Composition** — `Patient` owns its own `MedicalRecord`; `Appointment` links real `Doctor` and `Patient` objects together

## Project Structure

hospital_management_system/
├── src/
│ ├── models/ # Core backend classes (Person, Doctor, Patient, MedicalRecord, Appointment)
│ ├── gui/ # (reserved for future GUI component breakdown)
│ └── main.py # Application entry point
├── tests/
│ └── test_models.py # Manual tests for backend classes, run independently of the GUI
├── requirements.txt
└── README.md

## How to Run

1. Clone the repository:
git clone https://github.com/Ammar-Yaser252/hospital_management_system.git
cd hospital_management_system

2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\Activate.ps1 # Windows PowerShell

3. Install dependencies:
pip install -r requirements.txt

4. Run the application:
python -m src.main

## Backend Testing

Core classes can be tested independently of the GUI:
python -m tests.test_models

## Planned Improvements

- Patient view of prescription history
- Doctor login/authentication
- Track which doctor wrote each prescription (currently only the note text is stored)
- Display doctor specialization in Patient View

