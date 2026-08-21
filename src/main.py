import tkinter as tk

window = tk.Tk()
window.title("Hospital Management System")

doctor_view = tk.Frame(window)
patient_view = tk.Frame(window)

doctor_view.grid(row=0, column=0, sticky="nsew")
patient_view.grid(row=0, column=0, sticky="nsew")

tk.Label(doctor_view, text="This is the Doctor View").pack()
tk.Label(patient_view, text="This is the patient View").pack()

def show_patient_view():
    patient_view.tkraise()

def show_doctor_view():
    doctor_view.tkraise()

tk.Button(doctor_view, text="Switch to Patient View", command=show_patient_view).pack()
tk.Button(patient_view, text="Switch to Doctor View", command=show_doctor_view).pack()

doctor_view.tkraise()

window.mainloop()
