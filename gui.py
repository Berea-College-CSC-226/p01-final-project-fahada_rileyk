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