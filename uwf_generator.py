import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random

def add_rule():
    port = port_entry.get()
    protocol = protocol_var.get()
    action = action_var.get()
    location = location_var.get()
    interface = interface_entry.get()
    if not port or not protocol:
        messagebox.showerror("Error", "Enter a port and select a protocol")
        return
    if location == "Local":
        subnet = "192.168.0.0/16"
        if interface:
            if protocol == "both":
                rule = f'{action} from {subnet} to any port {port}'
            else:
                rule = f'{action} from {subnet} to any port {port}/{protocol} on {interface}'
        else:
            if protocol == "both":
                rule = f'{action} from {subnet} to any port {port}'
            else:
                rule = f'{action} from {subnet} to any port {port}/{protocol}'
    else:
        if interface:
            if protocol == "both":
                rule = f'{action} to any port {port} on {interface}'
            else:
                rule = f'{action} to any port {port}/{protocol} on {interface}'
        rule = f'{action} to any port {port}/{protocol}'
    generated_rules.append(rule)
    messagebox.showinfo("Success", "Rule added successfully")

def save_rules():
    if not generated_rules:
        messagebox.showerror("Error", "No rules to save.")
        return
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_name:
        return
    with open(file_name, 'w') as file:
        file.write("\n".join(generated_rules))
    messagebox.showinfo("Success", f"Rules saved to: {file_name}")

def is_valid_rule(rule):
    return random.choice([True, False])

root = tk.Tk()
root.title("UFW Rule Generator and Saver")

port_label = tk.Label(root, text="Port:")
port_label.pack()

port_entry = tk.Entry(root)
port_entry.pack()

protocol_label = tk.Label(root, text="Protocol:")
protocol_label.pack()

protocol_var = tk.StringVar()
protocol_var.set("tcp")
protocol_options = ["tcp", "udp", "both"]
protocol_menu = tk.OptionMenu(root, protocol_var, *protocol_options)
protocol_menu.pack()

action_label = tk.Label(root, text="Action:")
action_label.pack()

action_var = tk.StringVar()
action_var.set("allow")
action_options = ["allow", "deny"]
action_menu = tk.OptionMenu(root, action_var, *action_options)
action_menu.pack()

location_label = tk.Label(root, text="Location:")
location_label.pack()

location_var = tk.StringVar()
location_var.set("Local")
location_options = ["Local", "WAN"]
location_menu = tk.OptionMenu(root, location_var, *location_options)
location_menu.pack()

interface_label = tk.Label(root, text="Interface:")
interface_label.pack()

interface_entry = tk.Entry(root)
interface_entry.pack()

add_rule_button = tk.Button(root, text="Add Rule", command=add_rule)
add_rule_button.pack()

save_rules_button = tk.Button(root, text="Save Rules to a File", command=save_rules)
save_rules_button.pack()

generated_rules = []

root.mainloop()
