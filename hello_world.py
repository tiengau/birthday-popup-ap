import tkinter as tk
import random

# Initialize counter for windows
window_count = 0
total_windows = 100  # Increase the total number of windows to cover the screen more effectively
interval = 50  # Faster interval for quicker pop-ups

# List of colors to apply to the text
text_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Function to create a new pop-up window
def create_window():
    global window_count
    if window_count < total_windows:  # Only create up to the specified number of windows
        window = tk.Toplevel(root)
        
        # Random positioning across the screen for full screen effect
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = random.randint(0, screen_width - 150)
        y_position = random.randint(0, screen_height - 100)
        
        # Set the text to display
        message = "CHÚC MỪNG SINH NHẬT CHỊ GÁI!"
        
        # Create label to measure text size and adjust window size
        label = tk.Label(window, text=message, font=("Arial", 12, "bold"), fg="white", bg="pink")  # Pink background for the message
        label.pack(expand=True)
        
        # Update the window size based on text length
        text_width = label.winfo_reqwidth()  # Get the width of the text
        text_height = label.winfo_reqheight()  # Get the height of the text
        window.geometry(f"{text_width + 20}x{text_height + 20}+{x_position}+{y_position}")  # Add some padding

        window.configure(bg="pink")  # Set background color of the pop-up window
        window.title("Thông báo")

        window_count += 1  # Increase the count of created windows
        root.after(interval, create_window)  # Schedule the next pop-up

# Function to start the sequence of pop-ups
def start_popups():
    create_window()

# Function to change the color of the button text each time it's pressed
def change_button_color():
    current_color = button.cget("fg")
    # Find the next color in the list
    next_color = text_colors[(text_colors.index(current_color) + 1) % len(text_colors)]
    button.configure(fg=next_color)  # Change the color of the text on the button

# Main window setup
root = tk.Tk()
root.title("Popup Creator")
root.geometry("300x200")
root.configure(bg="pink")  # Set the background color of the main window to pink

# Button to trigger the pop-ups continuously
button = tk.Button(root, text="HÃY NHẤN VÀO ĐÂY", command=lambda: [start_popups(), change_button_color()], font=("Arial", 12), bg="yellow", fg="red")
button.pack(expand=True)  # Expand and center the button

# Run the application
root.mainloop()
