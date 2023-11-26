from Priority_Queue import*
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk


class CandyDispenserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Queue")
        # self.root.geometry("400x400")  # Set the size of the window

        self.patient_pq = Priority_queue() 

        self.max_size = 9
        # Create the  frame for patients
        self.right_frame = tk.Frame(root, bg='white', bd=2, relief="solid", width=900, height=350)
        self.right_frame.pack(side=tk.RIGHT, padx=5, ipadx=20, ipady=10)
        self.right_frame.pack_propagate(0)

        # declaring string to hold patient's name and age
        self.patient_name = tk.StringVar()
        self.patient_age = tk.StringVar()
        self.remove_at_var = tk.StringVar()
        self.old_pos_var = tk.StringVar()
        self.new_pos_var = tk.StringVar()

        # Create frame for buttons
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side=tk.LEFT, padx=5, pady=5)
        # Create buttons with larger font and size
        button_config = {'font': ('Arial', 12), 'height': 2, 'width': 10}
        self.add_button = tk.Button(self.left_frame, text="Add",command=self.add_patient, **button_config)
        self.get_first_button = tk.Button(self.left_frame, text="Get First",command=self.get_first_patient,  **button_config)
        self.remove_first_button = tk.Button(self.left_frame, text="Remove First",command=self.remove_first_patient, **button_config)
        self.is_empty_button = tk.Button(self.left_frame, text="Is Empty",command=self.update_is_empty_label, **button_config)
        self.lenght_button = tk.Button(self.left_frame, text="Length", command=self.update_length_label, **button_config)

        # Create label with larger font
        label_config = {'font': ('Arial', 12)}
        self.info_label = tk.Label(self.right_frame, text="", padx=10, pady=10, font=("Helvetica", 12, "bold"), bg="white")

        # Create a label with a stylish font
        self.title_label = tk.Label(self.left_frame, text="Hospital queue", font=("Helvetica", 16, "bold"), fg="orange")
        # Create labels in the waiting room
        self.waiting_room_label = tk.Label(self.right_frame, text="BACK<------    Waiting room       ----->FRONT", padx=10, pady=10, **label_config, fg="green")
        self.waiting_room_label.pack(side=tk.TOP)

        # create the receptionist
        self.recept_img = Image.open('receptionist_desk.png')  # Replace with your icon image
        self.recept_img = self.recept_img.resize((40, 40))
        self.recept_icon = ImageTk.PhotoImage(self.recept_img)
        
        self.receptionist = tk.Label(self.right_frame, text="Opened..", image=self.recept_icon, compound="bottom",**label_config, fg="green", bg='white')
        self.receptionist.pack(side=tk.TOP)

        self.info_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # self.front_label = tk.Label(self.right_frame, text="FRONT", padx=10, pady=20, **label_config, fg="black", bg='white')
        # self.front_label.pack(side=tk.RIGHT)

        # self.back_label = tk.Label(self.right_frame, text="BACK", padx=10, pady=20, **label_config, fg="black", bg='white')
        # self.back_label.pack(side=tk.LEFT)

        # # create the receptionist
        # self.recept_img = Image.open('receptionist_desk.png')  # Replace with your icon image
        # self.recept_img = self.recept_img.resize((40, 40))
        # self.recept_icon = ImageTk.PhotoImage(self.recept_img)
        
        # self.receptionist = tk.Label(self.right_frame, text="Recept..", image=self.recept_icon, compound="bottom",**label_config, fg="green", bg='white')
        # self.receptionist.pack(side=tk.TOP)

        # create labels and entry widget for age and name
        self.age_label = tk.Label(self.left_frame, text="Enter Age", padx=5, pady=10, **label_config, fg="black")
        self.name_label = tk.Label(self.left_frame, text="Enter Name", padx=5, pady=10, **label_config, fg="black")
        self.enter_age = tk.Entry(self.left_frame,textvariable = self.patient_age, font=('Helvetica',14,'normal'),justify="center",
                                bg="black", fg="blue", width=20, insertbackground="blue")
        self.enter_name = tk.Entry(self.left_frame,textvariable =self.patient_name, font=('Helvetica',14,'normal'),justify="center",
                                bg="black", fg="blue", width=20, insertbackground="blue")
        
        # create labels and entry widget for remove_at
        self.remove_at_label = tk.Label(self.left_frame, text="Enter Position to remove", padx=5, pady=10, **label_config, fg="black")
        self.remove_at_entry = tk.Entry(self.left_frame,textvariable = self.remove_at_var, font=('Helvetica',12,'normal'),justify="center",
                                bg="black", fg="blue", width=20, insertbackground="blue")
        self.remove_at_button = tk.Button(self.left_frame, text="Remove at",command=self.remove_at, **button_config)
        
        # create labels and entry widget for update
        self.update_old_label = tk.Label(self.left_frame, text="Enter old then new Position", padx=5, pady=10, **label_config, fg="black")
        self.update_new_label = tk.Label(self.left_frame, text="Enter New Position", padx=5, pady=10, **label_config, fg="black")
        self.update_old_entry = tk.Entry(self.left_frame,textvariable = self.old_pos_var, font=('Helvetica',12,'normal'),justify="center",
                                bg="black", fg="blue", width=20, insertbackground="blue")
        self.update_new_entry = tk.Entry(self.left_frame,textvariable = self.new_pos_var, font=('Helvetica',12,'normal'),justify="center",
                                bg="black", fg="blue", width=20, insertbackground="blue")
        self.update_button = tk.Button(self.left_frame, text="Update",command=self.update_patient, **button_config)
        
        

        # Pack buttons and label
        self.title_label.pack(side=tk.TOP,padx=5, pady=5)
        

        self.name_label.pack(side=tk.TOP)
        self.enter_name.pack(side=tk.TOP) 

        self.age_label.pack(side=tk.TOP)
        self.enter_age.pack(side=tk.TOP)    

        self.add_button.pack(side=tk.TOP, padx=5, pady=5)
        self.remove_at_label.pack(side=tk.TOP)
        self.remove_at_entry.pack(side=tk.TOP, padx=5, pady=5)
        self.remove_at_button.pack(side=tk.TOP, padx=5, pady=5)

        self.update_old_label.pack(side=tk.TOP, padx=5, pady=5)
        self.update_old_entry.pack(side=tk.TOP, padx=5, pady=5)
        self.update_new_entry.pack(side=tk.TOP, padx=5, pady=5)
        self.update_button.pack(side=tk.TOP, padx=5, pady=5)


        self.get_first_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.remove_first_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.is_empty_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.lenght_button.pack(side=tk.RIGHT, padx=5, pady=5)
        
        # self.remove_at_entry.pack(side=tk.TOP, padx=5, pady=5)
        # self.remove_at_button.pack(side=tk.TOP, padx=5, pady=5)
        # self.update_old_label.pack(side=tk.RIGHT, padx=5, pady=5)
        # self.update_old_entry.pack(side=tk.RIGHT, padx=5, pady=5)
        # self.update_new_label.pack(side=tk.RIGHT, padx=5, pady=5)
        # self.update_new_entry.pack(side=tk.RIGHT, padx=5, pady=5)
        # self.update_button.pack(side=tk.RIGHT, padx=5, pady=5)
        
        # self.draw_patients()

    def draw_patients(self):
    # Clear existing icons by destroying all widgets in self.right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Add the updated patient icons
        patient_icons = []
        self.waiting_room_label = tk.Label(self.right_frame, text="BACK<------    Waiting room       ----->FRONT", padx=10, pady=10, font=("Helvetica", 12, "bold"), fg="green")
        self.waiting_room_label.pack(side=tk.TOP)

        # create the receptionist
        self.recept_img = Image.open('receptionist_desk.png')  # Replace with your icon image
        self.recept_img = self.recept_img.resize((40, 40))
        self.recept_icon = ImageTk.PhotoImage(self.recept_img)

        if self.patient_pq.get_length() >= self.max_size:
            self.receptionist = tk.Label(self.right_frame, text="Closed..", image=self.recept_icon, compound="bottom",font=("Arial", 12, "bold"), fg="red", bg='white')
        else:
            self.receptionist = tk.Label(self.right_frame, text="Opened..", image=self.recept_icon, compound="bottom",font=("Arial", 12, "bold"), fg="green", bg='white')

        
        
        self.receptionist.pack(side=tk.TOP)


        self.info_label = tk.Label(self.right_frame, text="", padx=10, pady=10, font=("Helvetica", 12, "bold"), bg="white")

        self.info_label.pack(side=tk.TOP)
        self.position_of_patient = 0

        for age, name in self.patient_pq.get_pq():
            img = Image.open('user.png')  # Replace with your icon image
            img = img.resize((40, 40))
            img = ImageTk.PhotoImage(img)

            self.position_of_patient += 1
            
            icon_label = tk.Label(self.right_frame, bg='white', text=f'{self.position_of_patient}:{name},{age}yrs', image=img, compound="bottom")
            icon_label.image = img
            icon_label.pack(side=tk.RIGHT, padx=5)
            patient_icons.append(icon_label)

  

    def update_length_label(self):
        length = self.patient_pq.get_length()
        self.info_label.config(text=f"{length} Patients")

    def update_is_empty_label(self):
        is_empty = self.patient_pq.is_empty()
        self.info_label.config(text=f"Empty: {str(is_empty)}")

    def add_patient(self):
        try:
            if self.patient_pq.get_length() < self.max_size:
                age = int(self.patient_age.get())
                name = str(self.patient_name.get())
                self.patient_pq.add(age, name)

                self.draw_patients()

                self.patient_age.set("")
                self.patient_name.set("")
            else:
                self.info_label.config(text=f"CANNOT Add more patients; Maximum patients(9) attained", fg="green")
        except ValueError:
            self.info_label.config(text=f"Invalid Age entered!!!", fg="red")

    def get_first_patient(self):
        if not self.patient_pq.is_empty():
            first_age, first_name = self.patient_pq.first_item()
            self.info_label.config(text=f"First is: {first_name}, {first_age} years old", fg="green")
        else:
            self.info_label.config(text=f"CANNOT SEE 1st patient; Prioriry Queue is Empty", fg="red")

    def remove_first_patient(self):
        if not self.patient_pq.is_empty():
            first_age, first_name = self.patient_pq.remove_first()
            self.draw_patients()
            self.info_label.config(text=f"{first_name} {first_age} years, is Removed", fg="green")
        else:
            self.draw_patients()
            self.info_label.config(text=f"CANNOT REMOVE; Prioriry Queue is Empty", fg="red")

    def remove_at(self):
        try:
            the_pos = int(self.remove_at_var.get())
            if the_pos > 0 and the_pos < self.patient_pq.get_length():
                age, name = self.patient_pq.remove_at(the_pos)
                self.draw_patients()
                self.info_label.config(text=f"{name} {age} years, is Removed", fg="green")
                self.remove_at_var.set("")
            else:
                self.info_label.config(text=f"Patient's position entered does NOT exist", fg="red")
        except ValueError:
            self.info_label.config(text=f"Invalid Position entered!!", fg="red")

    def update_patient(self):
        try:
            old_pos_patient = int(self.old_pos_var.get())
            new_pos_patient = int(self.new_pos_var.get())

            if old_pos_patient > 0 and old_pos_patient < self.patient_pq.get_length():
                self.patient_pq.update_element(old_pos_patient, new_pos_patient)
                self.draw_patients()
                self.old_pos_var.set("")
                self.new_pos_var.set("")
            else:
                self.info_label.config(text=f"Patient's position entered does NOT exist", fg="red")
        except ValueError:
           self.info_label.config(text=f"Invalid Positions entered!!", fg="red")
    

# Run the App
root = tk.Tk()
app = CandyDispenserApp(root)
root.mainloop()
