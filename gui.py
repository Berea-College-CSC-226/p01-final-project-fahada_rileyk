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