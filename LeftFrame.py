import tkinter as tk
from tkinter import ttk
import RightFrame as Rf


class LeftFrame(tk.Frame):

    def __init__(self, master, root, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.root = root
        self.right_frame = tk.Frame()  # temp frame so that we can use .destroy right before calling the new updated frame
        self.build_frame()

    def build_frame(self):
        type_label = tk.Label(self, text="Choose type of data to visualize:")
        type_label.pack()

        type_combo = ttk.Combobox(self, values=('Traffic Accidents', 'Traffic Volume'))
        type_combo.pack()

        year_label = tk.Label(self, text="Choose a year:")
        year_label.pack()

        year_combo = ttk.Combobox(self, values=('2016', '2017', '2018'))
        year_combo.pack()

        # Event listener for read button
        def read_cmd():
            if type_combo.get() == 'Traffic Volume':
                if year_combo.get() == '2016':
                    # Clears the previous message
                    status_text.delete('1.0', tk.END)
                    # Message that helped me check what I was doing, we don't necessarily need to display this
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2016")
                    # Builds frame, no filter means the data will be displayed as it is on the file
                    # Because this button is for read only, all the method calls will have this no filter
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficFlow2016')
                    self.right_frame.pack(fill='both', expand=True)
                elif year_combo.get() == '2017':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2017")
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficFlow2017')
                    self.right_frame.pack(fill='both', expand=True)
                elif year_combo.get() == '2018':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2018")
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficFlow2018')
                    self.right_frame.pack(fill='both', expand=True)
                # If there is no year selected
                else:
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Please select a year")

            elif type_combo.get() == 'Traffic Accidents':
                if year_combo.get() == '2016':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2016")
                    # I pulled all the data from the same file, we can delete the other ones from out database
                    # The added argument filters, from the file, only data that happened in that year
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficIncidents', '2016')
                    self.right_frame.pack(fill='both', expand=True)
                elif year_combo.get() == '2017':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2017")
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficIncidents', '2017')
                    self.right_frame.pack(fill='both', expand=True)
                elif year_combo.get() == '2018':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2018")
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficIncidents', '2018')
                    self.right_frame.pack(fill='both', expand=True)
                else:
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Please select a year")
            # If year selected but not type
            else:
                status_text.delete('1.0', tk.END)
                status_text.insert(tk.END, "Please select Volume\nor Accidents")

        read_btn = tk.Button(self, text="Read", width=10, command=read_cmd)
        read_btn.pack()

        # Event listener for sort button
        def sort_cmd():
            if type_combo.get() == 'Traffic Volume':
                if year_combo.get() == '2016':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2016\nSorted by Volume")
                    # For all the method calls to build frame in sort button
                    # the argument sorted will return sorted data
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficFlow2016', '2016')
                    self.right_frame.pack(fill='both', expand=True)
                elif year_combo.get() == '2017':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2017\nSorted by Volume")
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficFlow2017', '2017')
                    self.right_frame.pack(fill='both', expand=True)
                elif year_combo.get() == '2018':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2018\nSorted by Volume")
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficFlow2018', '2018')
                    self.right_frame.pack(fill='both', expand=True)
                else:
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Please select a year")
            elif type_combo.get() == 'Traffic Accidents':
                if year_combo.get() == '2016':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2016\nSorted by Number of\nIncidents")
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficIncidents', '2016')
                    self.right_frame.pack(fill='both', expand=True)
                elif year_combo.get() == '2017':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2017\nSorted by Number of\nIncidents")
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficIncidents', '2017')
                    self.right_frame.pack(fill='both', expand=True)
                elif year_combo.get() == '2018':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2018\nSorted by Number of\nIncidents")
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficIncidents', '2018')
                    self.right_frame.pack(fill='both', expand=True)
                else:
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Please select a year")
            else:
                status_text.delete('1.0', tk.END)
                status_text.insert(tk.END, "Please select Volume\nor Accidents")

        sort_btn = tk.Button(self, text="Sort", width=10, command=sort_cmd)
        sort_btn.pack()

        analysis_btn = tk.Button(self, text="Analysis", width=10)
        analysis_btn.pack()

        map_btn = tk.Button(self, text="Map", width=10)
        map_btn.pack()

        status_label = tk.Label(self, text="Status:")
        status_label.pack()

        status_text = tk.Text(self, width=20, height=4)
        status_text.pack()



