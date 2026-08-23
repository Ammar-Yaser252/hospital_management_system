import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

from src.models.doctor import Doctor
from src.models.patient import Patient

# ---- Sample data (temporary, until a real data source/database is added) ----
current_doctor = Doctor("Dr.Ahmed Hasan", "1001", 50, "01560925837", "Internal medicine")
current_doctor.add_slot("09:00 AM")
current_doctor.add_slot("10:00 AM")
current_doctor.add_slot("11:00 AM")

patients = [
    Patient("Ali Ahmed", "101", 35, "01295831679", "A+"),
    Patient("Sayed Abbas", "102", 30, "01097263455", "A-"),
    Patient("Mona Mohammed", "103", 32, "01191736548", "B-"),
]

# ---- Main window ----
window = tk.Tk()
window.title("Hospital Management System")
window.geometry("500x600")

doctor_view = tk.Frame(window)
patient_view = tk.Frame(window)

for view in (doctor_view, patient_view):
    view.grid(row=0, column=0, sticky="nsew")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# ============================================================
# DOCTOR VIEW
# ============================================================
tk.Label(doctor_view, text="Doctor View", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(doctor_view, text="Switch to Patient View", command=lambda: patient_view.tkraise()).pack(pady=5)

tk.Label(doctor_view, text="Select a patient:").pack()
patient_listbox = tk.Listbox(doctor_view)
patient_listbox.pack(fill="x", padx=20)
for patient in patients:
    patient_listbox.insert(tk.END, patient.name)

tk.Label(doctor_view, text="Prescription note:").pack(pady=(10, 0))
prescription_text = tk.Text(doctor_view, height=5)
prescription_text.pack(fill="x", padx=20)

def save_prescription():
    selection = patient_listbox.curselection()
    if not selection:
        messagebox.showwarning("No patient selected", "Please select a patient first.")
        return

    selected_patient = patients[selection[0]]
    note = prescription_text.get("1.0", tk.END).strip()

    if not note:
        messagebox.showwarning("Empty note", "Please write a prescription note.")
        return

    current_doctor.write_prescription_for(selected_patient, note)
    messagebox.showinfo("Saved", f"Prescription saved for {selected_patient.name}.")
    prescription_text.delete("1.0", tk.END)

tk.Button(doctor_view, text="Save Prescription", command=save_prescription).pack(pady=10)

# ============================================================
# PATIENT VIEW
# ============================================================
tk.Label(patient_view, text="Patient View", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(patient_view, text="Switch to Doctor View", command=lambda: doctor_view.tkraise()).pack(pady=5)

tk.Label(patient_view, text="Select yourself (patient):").pack()
patient_select_listbox = tk.Listbox(patient_view, height=4)
patient_select_listbox.pack(fill="x", padx=20)
for patient in patients:
    patient_select_listbox.insert(tk.END, patient.name)

tk.Label(patient_view, text="Select a doctor:").pack(pady=(10, 0))
doctor_combobox = ttk.Combobox(patient_view, values=[current_doctor.name], state="readonly")
doctor_combobox.pack()
doctor_combobox.current(0)

tk.Label(patient_view, text="Select a date:").pack(pady=(10, 0))
calendar = Calendar(patient_view, selectmode="day")
calendar.pack(pady=5)

tk.Label(patient_view, text="Select a time slot:").pack()
slot_combobox = ttk.Combobox(patient_view, values=current_doctor.available_slots, state="readonly")
slot_combobox.pack()

def book():
    patient_selection = patient_select_listbox.curselection()
    if not patient_selection:
        messagebox.showwarning("No patient selected", "Please select who you are.")
        return

    if not slot_combobox.get():
        messagebox.showwarning("No time slot", "Please select a time slot.")
        return

    selected_patient = patients[patient_selection[0]]
    date_str = calendar.get_date()
    time_str = slot_combobox.get()
    date_time = f"{date_str} {time_str}"

    appointment = selected_patient.book_appointment(current_doctor, date_time)
    messagebox.showinfo("Booked", f"Appointment booked with {appointment.doctor.name} on {appointment.date_time}.")

tk.Button(patient_view, text="Book Appointment", command=book).pack(pady=10)

# ---- Start ----
doctor_view.tkraise()
window.mainloop()