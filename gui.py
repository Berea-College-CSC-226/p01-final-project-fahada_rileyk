"""
GUI Layer - Tkinter Interface
Provides graphical user interface for Berea Quad Walmart inventory system.

Features:
- Product addition
- Product search
- Stock in/out operations
- Display area for results
"""

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from inventory import InventoryManager


class InventoryGUI:
    """
    Tkinter-based GUI for inventory management.
    Thin UI layer - all logic delegated to InventoryManager.
    """

    def __init__(self, root):
        """
        Initialize the GUI.

        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Berea Quad Walmart - Inventory Management")
        self.root.geometry("800x700")
        self.root.configure(bg="#f0f0f0")

        # Initialize inventory manager
        self.inventory = InventoryManager()

        # Build UI components
        self.create_widgets()

    def create_widgets(self):
        """Create all GUI widgets."""

        # ===== HEADER WITH IMAGE =====
        header_frame = tk.Frame(self.root, bg="#003d82", height=150)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        header_frame.pack_propagate(False)

        # Title
        title_label = tk.Label(
            header_frame,
            text="Berea Quad Walmart",
            font=("Arial", 24, "bold"),
            bg="#003d82",
            fg="white"
        )
        title_label.pack(pady=10)

        # Image placeholder with instructions
        self.load_quad_image(header_frame)

        # ===== MAIN CONTAINER =====
        main_container = tk.Frame(self.root, bg="#f0f0f0")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20)

        # ===== INPUT SECTION =====
        input_frame = tk.LabelFrame(
            main_container,
            text="Product Information",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            padx=15,
            pady=15
        )
        input_frame.pack(fill=tk.X, pady=(0, 15))

        # UPC Input
        tk.Label(input_frame, text="UPC Code:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        self.upc_entry = tk.Entry(input_frame, font=("Arial", 10), width=30)
        self.upc_entry.grid(row=0, column=1, pady=5, padx=5)

        # Product Name Input
        tk.Label(input_frame, text="Product Name:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        self.name_entry = tk.Entry(input_frame, font=("Arial", 10), width=30)
        self.name_entry.grid(row=1, column=1, pady=5, padx=5)

        # Quantity Input
        tk.Label(input_frame, text="Quantity:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        self.quantity_entry = tk.Entry(input_frame, font=("Arial", 10), width=30)
        self.quantity_entry.grid(row=2, column=1, pady=5, padx=5)

        # ===== BUTTON SECTION =====
        button_frame = tk.Frame(main_container, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, pady=(0, 15))

        # Configure button style
        button_config = {
            "font": ("Arial", 10, "bold"),
            "width": 15,
            "height": 2
        }

        # Add Product Button
        self.add_btn = tk.Button(
            button_frame,
            text="Add Product",
            bg="#4CAF50",
            fg="white",
            command=self.add_product,
            **button_config
        )
        self.add_btn.grid(row=0, column=0, padx=5, pady=5)

        # Search Product Button
        self.search_btn = tk.Button(
            button_frame,
            text="Search Product",
            bg="#2196F3",
            fg="white",
            command=self.search_product,
            **button_config
        )
        self.search_btn.grid(row=0, column=1, padx=5, pady=5)

        # Stock In Button
        self.stock_in_btn = tk.Button(
            button_frame,
            text="Stock In",
            bg="#FF9800",
            fg="white",
            command=self.stock_in,
            **button_config
        )
        self.stock_in_btn.grid(row=1, column=0, padx=5, pady=5)

        # Stock Out Button
        self.stock_out_btn = tk.Button(
            button_frame,
            text="Stock Out",
            bg="#f44336",
            fg="white",
            command=self.stock_out,
            **button_config
        )
        self.stock_out_btn.grid(row=1, column=1, padx=5, pady=5)

        # Clear Button
        self.clear_btn = tk.Button(
            button_frame,
            text="Clear Fields",
            bg="#9E9E9E",
            fg="white",
            command=self.clear_fields,
            **button_config
        )
        self.clear_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # ===== OUTPUT SECTION =====
        output_frame = tk.LabelFrame(
            main_container,
            text="Output / Results",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            padx=15,
            pady=15
        )
        output_frame.pack(fill=tk.BOTH, expand=True)

        # Text widget with scrollbar
        self.output_text = tk.Text(
            output_frame,
            font=("Courier", 10),
            height=12,
            wrap=tk.WORD,
            bg="white"
        )
        scrollbar = tk.Scrollbar(output_frame, command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)

        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def load_quad_image(self, parent_frame):
        """
        Load and display Berea Quad image.

        """

        try:
            img = Image.open("image/berea_quad.jpg")
            img = img.resize((400, 80), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            img_label = tk.Label(parent_frame, image=photo, bg="#003d82")
            img_label.image = photo  # Keep reference
            img_label.pack()

        except Exception as e:
            print(f"Error loading image: {e}")

    def display_message(self, message, clear=True):
        """
        Display message in output area.

        Args:
            message (str): Message to display
            clear (bool): Whether to clear previous messages
        """
        if clear:
            self.output_text.delete(1.0, tk.END)

        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)

    def clear_fields(self):
        """Clear all input fields and output."""
        self.upc_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.output_text.delete(1.0, tk.END)

    def add_product(self):
        """Handle Add Product button click."""
        upc = self.upc_entry.get().strip()
        name = self.name_entry.get().strip()
        quantity_str = self.quantity_entry.get().strip()

        # Validate quantity input
        try:
            quantity = int(quantity_str)
        except ValueError:
            self.display_message(" Error: Quantity must be a number.")
            return

        # Call inventory manager
        success, message = self.inventory.add_product(upc, name, quantity)

        if success:
            self.display_message(f" SUCCESS\n{message}")
            self.clear_fields()
        else:
            self.display_message(f" ERROR\n{message}")

    def search_product(self):
        """Handle Search Product button click."""
        upc = self.upc_entry.get().strip()

        success, message, product_data = self.inventory.search_product(upc)

        if success:
            self.display_message(f" SEARCH RESULTS\n{message}")
        else:
            self.display_message(f" {message}")

    def stock_in(self):
        """Handle Stock In button click."""
        upc = self.upc_entry.get().strip()
        quantity_str = self.quantity_entry.get().strip()

        try:
            quantity = int(quantity_str)
        except ValueError:
            self.display_message(" Error: Quantity must be a number.")
            return

        success, message = self.inventory.stock_in(upc, quantity)

        if success:
            self.display_message(f" STOCK IN\n{message}")
        else:
            self.display_message(f" ERROR\n{message}")

    def stock_out(self):
        """Handle Stock Out button click."""
        upc = self.upc_entry.get().strip()
        quantity_str = self.quantity_entry.get().strip()

        try:
            quantity = int(quantity_str)
        except ValueError:
            self.display_message(" Error: Quantity must be a number.")
            return

        success, message = self.inventory.stock_out(upc, quantity)

        if success:
            self.display_message(f" STOCK OUT\n{message}")
        else:
            self.display_message(f" ERROR\n{message}")

    def on_closing(self):
        """Handle window closing event."""
        self.inventory.close()
        self.root.destroy()

def main():
    """Entry point for GUI application."""
    root = tk.Tk()
    app = InventoryGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

    if __name__ == "__main__":
        main()
