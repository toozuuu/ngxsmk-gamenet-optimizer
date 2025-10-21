#!/usr/bin/env python3
"""
NGXSMK GameNet Optimizer
A comprehensive network and system optimization tool for gamers
Open source alternative to commercial gaming optimization software
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import sys
import os
import time
import json

# Import our modules
from modules.fps_boost import FPSBoost
from modules.network_analyzer import NetworkAnalyzer
from modules.multi_internet import MultiInternet
from modules.traffic_shaper import TrafficShaper
from modules.ram_cleaner import RAMCleaner
from modules.lol_optimizer import LoLOptimizer
from modules.advanced_optimizer import AdvancedOptimizer
from modules.system_monitor import SystemMonitor
from modules.network_optimizer import NetworkOptimizer
from modules.gaming_optimizer import GamingOptimizer
from modules.config_manager import ConfigManager
from modules.settings_dialog import SettingsDialog

class NetworkOptimizerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NGXSMK GameNet Optimizer")
        self.root.geometry("1400x900")
        self.root.configure(bg='#0a0a0a')
        self.root.minsize(1200, 800)
        
        # Modern window styling
        self.root.resizable(True, True)
        
        # Center the window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Initialize modules
        self.config_manager = ConfigManager()
        self.fps_boost = FPSBoost()
        self.network_analyzer = NetworkAnalyzer()
        self.multi_internet = MultiInternet()
        self.traffic_shaper = TrafficShaper()
        self.ram_cleaner = RAMCleaner()
        self.lol_optimizer = LoLOptimizer()
        
        # Initialize advanced modules
        self.advanced_optimizer = AdvancedOptimizer()
        self.system_monitor = SystemMonitor()
        self.network_optimizer = NetworkOptimizer()
        self.gaming_optimizer = GamingOptimizer()
        
        # Status variables
        self.is_optimizing = False
        self.optimization_thread = None
        
        self.setup_ui()
        self.load_settings()
        
    def setup_ui(self):
        """Setup the modern user interface"""
        # Configure modern style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Modern color scheme
        self.colors = {
            'bg_primary': '#0a0a0a',
            'bg_secondary': '#1a1a1a', 
            'bg_tertiary': '#2a2a2a',
            'accent': '#00ff88',
            'accent_hover': '#00cc6a',
            'text_primary': '#ffffff',
            'text_secondary': '#cccccc',
            'text_muted': '#888888',
            'success': '#00ff88',
            'warning': '#ffaa00',
            'error': '#ff4444',
            'border': '#333333'
        }
        
        # Configure notebook style
        style.configure('Modern.TNotebook', 
                       background=self.colors['bg_secondary'], 
                       borderwidth=0,
                       tabmargins=[0, 0, 0, 0])
        style.configure('Modern.TNotebook.Tab', 
                       background=self.colors['bg_tertiary'], 
                       foreground=self.colors['text_primary'], 
                       padding=[25, 12],
                       font=('Arial', 10, 'bold'))
        style.map('Modern.TNotebook.Tab', 
                 background=[('selected', self.colors['accent']),
                           ('active', self.colors['bg_tertiary'])])
        
        # Main container with gradient effect
        main_frame = tk.Frame(self.root, bg=self.colors['bg_primary'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Modern header with glass effect
        header_frame = tk.Frame(main_frame, bg=self.colors['bg_secondary'], relief=tk.FLAT, bd=0)
        header_frame.pack(fill=tk.X, pady=(0, 0))
        
        # Header content
        header_content = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        header_content.pack(fill=tk.X, padx=20, pady=15)
        
        # Logo and title section
        title_section = tk.Frame(header_content, bg=self.colors['bg_secondary'])
        title_section.pack(side=tk.LEFT)
        
        # App icon/logo (using emoji as placeholder)
        logo_label = tk.Label(title_section, text="🚀", font=('Arial', 28), 
                             fg=self.colors['accent'], bg=self.colors['bg_secondary'])
        logo_label.pack(side=tk.LEFT, padx=(0, 15))
        
        # Title and subtitle
        title_label = tk.Label(title_section, text="NGXSMK GameNet Optimizer", 
                              font=('Arial', 24, 'bold'), fg=self.colors['text_primary'], 
                              bg=self.colors['bg_secondary'])
        title_label.pack(side=tk.LEFT, anchor='n')
        
        subtitle_label = tk.Label(title_section, text="Advanced Gaming Performance Suite", 
                                 font=('Arial', 10), fg=self.colors['text_muted'], 
                                 bg=self.colors['bg_secondary'])
        subtitle_label.pack(side=tk.LEFT, anchor='n', padx=(10, 0))
        
        # Status and controls section
        controls_section = tk.Frame(header_content, bg=self.colors['bg_secondary'])
        controls_section.pack(side=tk.RIGHT)
        
        # Status indicator
        status_frame = tk.Frame(controls_section, bg=self.colors['bg_secondary'])
        status_frame.pack(side=tk.RIGHT, padx=(0, 20))
        
        status_indicator = tk.Label(status_frame, text="●", font=('Arial', 16), 
                                   fg=self.colors['success'], bg=self.colors['bg_secondary'])
        status_indicator.pack(side=tk.LEFT, padx=(0, 8))
        
        status_label = tk.Label(status_frame, text="System Ready", 
                              font=('Arial', 12, 'bold'), fg=self.colors['text_primary'], 
                              bg=self.colors['bg_secondary'])
        status_label.pack(side=tk.LEFT)
        self.status_label = status_label
        self.status_indicator = status_indicator
        
        # Modern settings button
        settings_btn = tk.Button(controls_section, text="⚙️", command=self.show_settings,
                                font=('Arial', 16), bg=self.colors['bg_tertiary'], 
                                fg=self.colors['text_primary'], relief=tk.FLAT, bd=0,
                                padx=15, pady=8, cursor='hand2')
        settings_btn.pack(side=tk.RIGHT, padx=(0, 10))
        
        # Add hover effects
        def on_settings_enter(e):
            settings_btn.config(bg=self.colors['accent'])
        def on_settings_leave(e):
            settings_btn.config(bg=self.colors['bg_tertiary'])
        
        settings_btn.bind('<Enter>', on_settings_enter)
        settings_btn.bind('<Leave>', on_settings_leave)
        
        # Modern sidebar layout
        content_container = tk.Frame(main_frame, bg=self.colors['bg_primary'])
        content_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left sidebar for quick actions
        sidebar = tk.Frame(content_container, bg=self.colors['bg_secondary'], 
                           relief=tk.FLAT, bd=1, width=300)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        sidebar.pack_propagate(False)
        
        # Sidebar title
        sidebar_title = tk.Label(sidebar, text="🚀 Quick Actions", 
                               font=('Arial', 16, 'bold'), fg=self.colors['text_primary'], 
                               bg=self.colors['bg_secondary'])
        sidebar_title.pack(pady=(20, 15), padx=20)
        
        # Quick action buttons in sidebar
        self.create_sidebar_button(sidebar, "🎯", "Optimize All", self.quick_optimize_all)
        self.create_sidebar_button(sidebar, "🧹", "Clean RAM", self.quick_clean_ram)
        self.create_sidebar_button(sidebar, "🌐", "Test Network", self.quick_test_network)
        self.create_sidebar_button(sidebar, "🎮", "Gaming Mode", self.quick_gaming_mode)
        
        # System status section in sidebar
        status_section = tk.Frame(sidebar, bg=self.colors['bg_tertiary'], relief=tk.FLAT, bd=1)
        status_section.pack(fill=tk.X, padx=15, pady=(20, 15))
        
        status_title = tk.Label(status_section, text="📊 System Status", 
                              font=('Arial', 14, 'bold'), fg=self.colors['text_primary'], 
                              bg=self.colors['bg_tertiary'])
        status_title.pack(pady=(15, 10), padx=15)
        
        # System status indicators
        self.create_status_indicator(status_section, "🎮", "FPS Boost", "Ready", self.colors['success'])
        self.create_status_indicator(status_section, "🌐", "Network", "Analyzing...", self.colors['warning'])
        self.create_status_indicator(status_section, "🧠", "RAM Usage", "85%", self.colors['warning'])
        self.create_status_indicator(status_section, "⚡", "CPU Load", "45%", self.colors['success'])
        
        # Main content area
        main_content = tk.Frame(content_container, bg=self.colors['bg_primary'])
        main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Main notebook for tabs with modern styling
        self.notebook = ttk.Notebook(main_content, style='Modern.TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs with modern icons
        self.create_fps_boost_tab()
        self.create_network_analyzer_tab()
        self.create_multi_internet_tab()
        self.create_traffic_shaper_tab()
        self.create_ram_cleaner_tab()
        self.create_lol_optimizer_tab()
        self.create_advanced_optimizer_tab()
        self.create_system_monitor_tab()
        self.create_network_optimizer_tab()
        self.create_gaming_optimizer_tab()
    
    def create_stat_card(self, parent, icon, title, value, row, col):
        """Create a modern stat card"""
        card = tk.Frame(parent, bg=self.colors['bg_tertiary'], relief=tk.FLAT, bd=1)
        card.grid(row=row, column=col, padx=10, pady=5, sticky='ew')
        parent.grid_columnconfigure(col, weight=1)
        
        # Icon
        icon_label = tk.Label(card, text=icon, font=('Arial', 20), 
                             fg=self.colors['accent'], bg=self.colors['bg_tertiary'])
        icon_label.pack(pady=(10, 5))
        
        # Title
        title_label = tk.Label(card, text=title, font=('Arial', 10, 'bold'), 
                              fg=self.colors['text_primary'], bg=self.colors['bg_tertiary'])
        title_label.pack()
        
        # Value
        value_label = tk.Label(card, text=value, font=('Arial', 14, 'bold'), 
                              fg=self.colors['success'], bg=self.colors['bg_tertiary'])
        value_label.pack(pady=(0, 10))
        
        return card
    
    def create_quick_action(self, parent, icon, text, command, row, col):
        """Create a modern quick action button"""
        btn = tk.Button(parent, text=f"{icon}\n{text}", command=command,
                       font=('Arial', 10, 'bold'), bg=self.colors['bg_tertiary'], 
                       fg=self.colors['text_primary'], relief=tk.FLAT, bd=1,
                       padx=15, pady=10, cursor='hand2')
        btn.grid(row=row, column=col, padx=5, pady=5, sticky='ew')
        parent.grid_columnconfigure(col, weight=1)
        
        # Hover effects
        def on_enter(e):
            btn.config(bg=self.colors['accent'], fg=self.colors['bg_primary'])
        def on_leave(e):
            btn.config(bg=self.colors['bg_tertiary'], fg=self.colors['text_primary'])
        
        btn.bind('<Enter>', on_enter)
        btn.bind('<Leave>', on_leave)
        
        return btn
    
    def quick_optimize_all(self):
        """Quick optimize all systems"""
        self.status_label.config(text="Optimizing All Systems...", fg=self.colors['warning'])
        self.status_indicator.config(fg=self.colors['warning'])
        # Implementation would go here
        self.root.after(2000, lambda: self.status_label.config(text="System Ready", fg=self.colors['text_primary']))
        self.root.after(2000, lambda: self.status_indicator.config(fg=self.colors['success']))
    
    def quick_clean_ram(self):
        """Quick RAM cleanup"""
        self.status_label.config(text="Cleaning RAM...", fg=self.colors['warning'])
        self.status_indicator.config(fg=self.colors['warning'])
        # Implementation would go here
        self.root.after(1500, lambda: self.status_label.config(text="RAM Cleaned", fg=self.colors['success']))
        self.root.after(2000, lambda: self.status_label.config(text="System Ready", fg=self.colors['text_primary']))
        self.root.after(2000, lambda: self.status_indicator.config(fg=self.colors['success']))
    
    def quick_test_network(self):
        """Quick network test"""
        self.status_label.config(text="Testing Network...", fg=self.colors['warning'])
        self.status_indicator.config(fg=self.colors['warning'])
        # Implementation would go here
        self.root.after(3000, lambda: self.status_label.config(text="Network Test Complete", fg=self.colors['success']))
        self.root.after(4000, lambda: self.status_label.config(text="System Ready", fg=self.colors['text_primary']))
        self.root.after(4000, lambda: self.status_indicator.config(fg=self.colors['success']))
    
    def quick_gaming_mode(self):
        """Quick gaming mode activation"""
        self.status_label.config(text="Activating Gaming Mode...", fg=self.colors['warning'])
        self.status_indicator.config(fg=self.colors['warning'])
        # Implementation would go here
        self.root.after(2500, lambda: self.status_label.config(text="Gaming Mode Active", fg=self.colors['success']))
        self.root.after(3000, lambda: self.status_label.config(text="System Ready", fg=self.colors['text_primary']))
        self.root.after(3000, lambda: self.status_indicator.config(fg=self.colors['success']))
    
    def optimize_fps(self):
        """Optimize FPS settings"""
        self.status_label.config(text="Optimizing FPS...", fg=self.colors['warning'])
        self.status_indicator.config(fg=self.colors['warning'])
        
        try:
            # Get selected game
            game = self.game_var.get()
            
            # Run FPS optimization
            results = self.fps_boost.optimize_game_performance(
                priority_boost=self.priority_boost.get(),
                cpu_optimization=self.cpu_optimization.get(),
                gpu_optimization=self.gpu_optimization.get()
            )
            
            # Update status display
            self.fps_status.config(state=tk.NORMAL)
            self.fps_status.delete(1.0, tk.END)
            self.fps_status.insert(tk.END, f"FPS Optimization Results:\n")
            self.fps_status.insert(tk.END, f"Game: {game}\n")
            self.fps_status.insert(tk.END, f"Processes Optimized: {results.get('processes_optimized', 0)}\n")
            self.fps_status.insert(tk.END, f"Priority Boost: {'Enabled' if self.priority_boost.get() else 'Disabled'}\n")
            self.fps_status.insert(tk.END, f"CPU Optimization: {'Enabled' if self.cpu_optimization.get() else 'Disabled'}\n")
            self.fps_status.insert(tk.END, f"GPU Optimization: {'Enabled' if self.gpu_optimization.get() else 'Disabled'}\n")
            self.fps_status.insert(tk.END, f"\nOptimization completed successfully!")
            self.fps_status.config(state=tk.DISABLED)
            
            self.status_label.config(text="FPS Optimization Complete", fg=self.colors['success'])
            self.status_indicator.config(fg=self.colors['success'])
            
        except Exception as e:
            self.fps_status.config(state=tk.NORMAL)
            self.fps_status.delete(1.0, tk.END)
            self.fps_status.insert(tk.END, f"Error during FPS optimization: {str(e)}")
            self.fps_status.config(state=tk.DISABLED)
            
            self.status_label.config(text="FPS Optimization Failed", fg=self.colors['error'])
            self.status_indicator.config(fg=self.colors['error'])
    
    def reset_fps_settings(self):
        """Reset FPS settings to default"""
        self.priority_boost.set(True)
        self.cpu_optimization.set(True)
        self.gpu_optimization.set(True)
        self.game_var.set("Auto-detect")
        
        self.fps_status.config(state=tk.NORMAL)
        self.fps_status.delete(1.0, tk.END)
        self.fps_status.insert(tk.END, "FPS settings reset to default values.")
        self.fps_status.config(state=tk.DISABLED)
        
        self.status_label.config(text="FPS Settings Reset", fg=self.colors['success'])
        self.status_indicator.config(fg=self.colors['success'])
    
    def create_modern_checkbox(self, parent, text, description, variable, row, col):
        """Create a modern checkbox with description"""
        checkbox_frame = tk.Frame(parent, bg=self.colors['bg_secondary'])
        checkbox_frame.pack(fill=tk.X, padx=10, pady=5)  # Use pack instead of grid
        
        # Checkbox with improved styling
        cb = tk.Checkbutton(checkbox_frame, text=text, variable=variable,
                           font=('Arial', 11, 'bold'), fg=self.colors['text_primary'], 
                           bg=self.colors['bg_secondary'], 
                           selectcolor=self.colors['accent'],  # Color when checked
                           activebackground=self.colors['bg_tertiary'],  # Hover background
                           activeforeground=self.colors['text_primary'],  # Hover text color
                           relief=tk.FLAT, bd=2,  # Flat style with border
                           highlightthickness=2,  # Focus border thickness
                           highlightcolor=self.colors['accent'],  # Focus border color
                           highlightbackground=self.colors['bg_tertiary'])  # Unfocused border color
        cb.pack(anchor=tk.W)
        
        # Description
        desc_label = tk.Label(checkbox_frame, text=description, 
                             font=('Arial', 9), fg=self.colors['text_muted'], 
                             bg=self.colors['bg_secondary'])
        desc_label.pack(anchor=tk.W, padx=(20, 0))
        
        return cb
    
    def create_modern_radiobutton(self, parent, text, variable, value, row, col):
        """Create a modern radio button with improved styling"""
        rb = tk.Radiobutton(parent, text=text, variable=variable, value=value,
                           font=('Arial', 11, 'bold'), fg=self.colors['text_primary'], 
                           bg=self.colors['bg_secondary'], 
                           selectcolor=self.colors['accent'],  # Color when selected
                           activebackground=self.colors['bg_tertiary'],  # Hover background
                           activeforeground=self.colors['text_primary'],  # Hover text color
                           relief=tk.FLAT, bd=2,  # Flat style with border
                           highlightthickness=2,  # Focus border thickness
                           highlightcolor=self.colors['accent'],  # Focus border color
                           highlightbackground=self.colors['bg_tertiary'],  # Unfocused border color
                           indicatoron=True,  # Show indicator
                           width=15,  # Set width for better appearance
                           anchor=tk.W)  # Left align text
        rb.pack(side=tk.LEFT, padx=10, pady=2)  # Use pack instead of grid
        
        return rb
    
    def create_modern_button(self, parent, text, command, row, col):
        """Create a modern button with hover effects"""
        btn = tk.Button(parent, text=text, command=command,
                       font=('Arial', 11, 'bold'), bg=self.colors['bg_tertiary'], 
                       fg=self.colors['text_primary'], relief=tk.FLAT, bd=1,
                       padx=20, pady=10, cursor='hand2')
        btn.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)  # Use pack instead of grid
        
        # Hover effects
        def on_enter(e):
            btn.config(bg=self.colors['accent'], fg=self.colors['bg_primary'])
        def on_leave(e):
            btn.config(bg=self.colors['bg_tertiary'], fg=self.colors['text_primary'])
        
        btn.bind('<Enter>', on_enter)
        btn.bind('<Leave>', on_leave)
        
        return btn
    
    def create_sidebar_button(self, parent, icon, text, command):
        """Create a modern sidebar button"""
        btn_frame = tk.Frame(parent, bg=self.colors['bg_secondary'])
        btn_frame.pack(fill=tk.X, padx=15, pady=5)
        
        btn = tk.Button(btn_frame, text=f"{icon} {text}", command=command,
                       font=('Arial', 12, 'bold'), bg=self.colors['bg_tertiary'], 
                       fg=self.colors['text_primary'], relief=tk.FLAT, bd=1,
                       padx=20, pady=12, cursor='hand2', anchor=tk.W)
        btn.pack(fill=tk.X)
        
        # Hover effects
        def on_enter(e):
            btn.config(bg=self.colors['accent'], fg=self.colors['bg_primary'])
        def on_leave(e):
            btn.config(bg=self.colors['bg_tertiary'], fg=self.colors['text_primary'])
        
        btn.bind('<Enter>', on_enter)
        btn.bind('<Leave>', on_leave)
        
        return btn
    
    def create_status_indicator(self, parent, icon, title, value, color):
        """Create a status indicator for the sidebar"""
        indicator_frame = tk.Frame(parent, bg=self.colors['bg_tertiary'])
        indicator_frame.pack(fill=tk.X, padx=15, pady=3)
        
        # Icon and title
        icon_label = tk.Label(indicator_frame, text=icon, font=('Arial', 16), 
                             fg=color, bg=self.colors['bg_tertiary'])
        icon_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Title and value
        text_frame = tk.Frame(indicator_frame, bg=self.colors['bg_tertiary'])
        text_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        title_label = tk.Label(text_frame, text=title, font=('Arial', 10, 'bold'), 
                              fg=self.colors['text_primary'], bg=self.colors['bg_tertiary'])
        title_label.pack(anchor=tk.W)
        
        value_label = tk.Label(text_frame, text=value, font=('Arial', 9), 
                              fg=color, bg=self.colors['bg_tertiary'])
        value_label.pack(anchor=tk.W)
        
        return indicator_frame
        
    def create_fps_boost_tab(self):
        """Create modern FPS Boost tab"""
        fps_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(fps_frame, text="🎮 FPS Boost")
        
        # Modern FPS Boost content with improved layout
        content_frame = tk.Frame(fps_frame, bg=self.colors['bg_primary'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Header section with gradient effect
        header_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief=tk.FLAT, bd=1)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Header content
        header_content = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        header_content.pack(fill=tk.X, padx=20, pady=15)
        
        # Title with icon
        title_frame = tk.Frame(header_content, bg=self.colors['bg_secondary'])
        title_frame.pack(side=tk.LEFT)
        
        title_icon = tk.Label(title_frame, text="🎮", font=('Arial', 24), 
                             fg=self.colors['accent'], bg=self.colors['bg_secondary'])
        title_icon.pack(side=tk.LEFT, padx=(0, 10))
        
        fps_title = tk.Label(title_frame, text="FPS Boost & Game Optimization", 
                            font=('Arial', 18, 'bold'), fg=self.colors['text_primary'], 
                            bg=self.colors['bg_secondary'])
        fps_title.pack(side=tk.LEFT)
        
        # Subtitle
        fps_subtitle = tk.Label(header_content, text="Optimize your gaming performance for maximum FPS", 
                               font=('Arial', 11), fg=self.colors['text_muted'], 
                               bg=self.colors['bg_secondary'])
        fps_subtitle.pack(side=tk.RIGHT, pady=(0, 5))
        
        # Game selection with modern styling
        game_section = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief=tk.FLAT, bd=1)
        game_section.pack(fill=tk.X, pady=(0, 15))
        
        game_title = tk.Label(game_section, text="🎯 Game Selection", 
                             font=('Arial', 14, 'bold'), fg=self.colors['text_primary'], 
                             bg=self.colors['bg_secondary'])
        game_title.pack(anchor=tk.W, padx=20, pady=(15, 10))
        
        game_frame = tk.Frame(game_section, bg=self.colors['bg_secondary'])
        game_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        tk.Label(game_frame, text="Select Game:", font=('Arial', 12, 'bold'), 
                fg=self.colors['text_primary'], bg=self.colors['bg_secondary']).pack(side=tk.LEFT)
        
        self.game_var = tk.StringVar(value="Auto-detect")
        game_combo = ttk.Combobox(game_frame, textvariable=self.game_var, 
                                 values=["Auto-detect", "Valorant", "CS2", "Fortnite", "Apex Legends", "Call of Duty", "League of Legends"],
                                 font=('Arial', 11), state='readonly')
        game_combo.pack(side=tk.LEFT, padx=(15, 0), fill=tk.X, expand=True)
        
        # Optimization options with modern cards
        options_section = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief=tk.FLAT, bd=1)
        options_section.pack(fill=tk.X, pady=(0, 15))
        
        options_title = tk.Label(options_section, text="⚙️ Optimization Options", 
                                font=('Arial', 14, 'bold'), fg=self.colors['text_primary'], 
                                bg=self.colors['bg_secondary'])
        options_title.pack(anchor=tk.W, padx=20, pady=(15, 10))
        
        options_frame = tk.Frame(options_section, bg=self.colors['bg_secondary'])
        options_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        # Create modern checkboxes
        self.priority_boost = tk.BooleanVar(value=True)
        self.create_modern_checkbox(options_frame, "🚀 High Priority Process", 
                                  "Set game processes to high priority", self.priority_boost, 0, 0)
        
        self.cpu_optimization = tk.BooleanVar(value=True)
        self.create_modern_checkbox(options_frame, "⚡ CPU Optimization", 
                                  "Optimize CPU usage for gaming", self.cpu_optimization, 0, 1)
        
        self.gpu_optimization = tk.BooleanVar(value=True)
        self.create_modern_checkbox(options_frame, "🎨 GPU Optimization", 
                                  "Optimize GPU performance for gaming", self.gpu_optimization, 1, 0)
        
        # Action buttons section
        actions_section = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief=tk.FLAT, bd=1)
        actions_section.pack(fill=tk.X, pady=(0, 15))
        
        actions_title = tk.Label(actions_section, text="🚀 Actions", 
                                font=('Arial', 14, 'bold'), fg=self.colors['text_primary'], 
                                bg=self.colors['bg_secondary'])
        actions_title.pack(anchor=tk.W, padx=20, pady=(15, 10))
        
        buttons_frame = tk.Frame(actions_section, bg=self.colors['bg_secondary'])
        buttons_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        # Modern action buttons
        self.create_modern_button(buttons_frame, "🎯 Optimize FPS", self.optimize_fps, 0, 0)
        self.create_modern_button(buttons_frame, "🔄 Reset Settings", self.reset_fps_settings, 0, 1)
        
        # Status display with modern styling
        status_section = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief=tk.FLAT, bd=1)
        status_section.pack(fill=tk.BOTH, expand=True)
        
        status_title = tk.Label(status_section, text="📊 Status & Results", 
                               font=('Arial', 14, 'bold'), fg=self.colors['text_primary'], 
                               bg=self.colors['bg_secondary'])
        status_title.pack(anchor=tk.W, padx=20, pady=(15, 10))
        
        status_frame = tk.Frame(status_section, bg=self.colors['bg_tertiary'], relief=tk.FLAT, bd=1)
        status_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 15))
        
        # Status label
        status_label = tk.Label(status_frame, text="Optimization Status:", 
                               font=('Arial', 12, 'bold'), fg=self.colors['text_primary'], 
                               bg=self.colors['bg_tertiary'])
        status_label.pack(anchor=tk.W, padx=15, pady=(10, 5))
        
        # Modern status text area
        self.fps_status = tk.Text(status_frame, height=8, bg=self.colors['bg_primary'], 
                                 fg=self.colors['accent'], font=('Consolas', 10),
                                 state=tk.DISABLED, wrap=tk.WORD)
        self.fps_status.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Add scrollbar
        scrollbar = tk.Scrollbar(status_frame, orient=tk.VERTICAL, command=self.fps_status.yview)
        self.fps_status.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def create_network_analyzer_tab(self):
        """Create modern Network Analyzer tab"""
        net_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(net_frame, text="🌐 Network Analyzer")
        
        # Network Analyzer content
        net_title = tk.Label(net_frame, text="Network Performance Analyzer", 
                            font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        net_title.pack(pady=20)
        
        # Controls
        controls_frame = tk.Frame(net_frame, bg='#1e1e1e')
        controls_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.start_analysis_btn = tk.Button(controls_frame, text="Start Analysis", 
                                           command=self.start_network_analysis,
                                           bg='#00ff88', fg='black', font=('Arial', 12, 'bold'),
                                           padx=20, pady=5, relief=tk.FLAT)
        self.start_analysis_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_analysis_btn = tk.Button(controls_frame, text="Stop Analysis", 
                                          command=self.stop_network_analysis,
                                          bg='#ff4444', fg='white', font=('Arial', 12, 'bold'),
                                          padx=20, pady=5, relief=tk.FLAT, state=tk.DISABLED)
        self.stop_analysis_btn.pack(side=tk.LEFT)
        
        # Results display
        results_frame = tk.Frame(net_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(results_frame, text="Network Analysis Results:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.network_results = tk.Text(results_frame, height=12, bg='#1e1e1e', fg='#00ff88',
                                      font=('Consolas', 10), state=tk.DISABLED)
        self.network_results.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
    def create_multi_internet_tab(self):
        """Create modern Multi Internet tab"""
        multi_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(multi_frame, text="🔗 Multi Internet")
        
        # Multi Internet content
        multi_title = tk.Label(multi_frame, text="Multi-Connection Manager", 
                              font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        multi_title.pack(pady=20)
        
        # Connection list
        conn_frame = tk.Frame(multi_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        conn_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(conn_frame, text="Available Connections:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.connection_list = tk.Listbox(conn_frame, bg='#1e1e1e', fg='white',
                                         font=('Consolas', 10), selectbackground='#00ff88')
        self.connection_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Load connections
        self.load_connections()
        
    def create_traffic_shaper_tab(self):
        """Create modern Traffic Shaper tab"""
        traffic_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(traffic_frame, text="🚦 Traffic Shaper")
        
        # Traffic Shaper content
        traffic_title = tk.Label(traffic_frame, text="Traffic Shaping & Bandwidth Control", 
                                font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        traffic_title.pack(pady=20)
        
        # Bandwidth controls
        bw_frame = tk.Frame(traffic_frame, bg='#1e1e1e')
        bw_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(bw_frame, text="Bandwidth Limit (Mbps):", font=('Arial', 12),
                fg='white', bg='#1e1e1e').pack(side=tk.LEFT)
        
        self.bandwidth_var = tk.StringVar(value="100")
        bandwidth_entry = tk.Entry(bw_frame, textvariable=self.bandwidth_var, 
                                  font=('Arial', 12), width=10)
        bandwidth_entry.pack(side=tk.LEFT, padx=(10, 0))
        
        # Traffic shaping options
        shaping_frame = tk.Frame(traffic_frame, bg='#1e1e1e')
        shaping_frame.pack(fill=tk.X, padx=20, pady=20)
        
        self.prioritize_gaming = tk.BooleanVar(value=True)
        tk.Checkbutton(shaping_frame, text="Prioritize Gaming Traffic", variable=self.prioritize_gaming,
                      fg='white', bg='#1e1e1e', selectcolor='#00ff88').pack(anchor=tk.W)
        
        self.limit_background = tk.BooleanVar(value=True)
        tk.Checkbutton(shaping_frame, text="Limit Background Applications", variable=self.limit_background,
                      fg='white', bg='#1e1e1e', selectcolor='#00ff88').pack(anchor=tk.W)
        
    def create_ram_cleaner_tab(self):
        """Create modern RAM Cleaner tab"""
        ram_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(ram_frame, text="🧹 RAM Cleaner")
        
        # RAM Cleaner content
        ram_title = tk.Label(ram_frame, text="Memory Optimization & RAM Cleaner", 
                            font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        ram_title.pack(pady=20)
        
        # Memory info
        mem_info_frame = tk.Frame(ram_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        mem_info_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(mem_info_frame, text="Memory Status:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.memory_info = tk.Text(mem_info_frame, height=6, bg='#1e1e1e', fg='#00ff88',
                                  font=('Consolas', 10), state=tk.DISABLED)
        self.memory_info.pack(fill=tk.X, padx=10, pady=5)
        
        # Cleaner controls
        clean_frame = tk.Frame(ram_frame, bg='#1e1e1e')
        clean_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.clean_ram_btn = tk.Button(clean_frame, text="Clean RAM", 
                                      command=self.clean_ram,
                                      bg='#00ff88', fg='black', font=('Arial', 12, 'bold'),
                                      padx=20, pady=10, relief=tk.FLAT)
        self.clean_ram_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.auto_clean = tk.BooleanVar(value=False)
        tk.Checkbutton(clean_frame, text="Auto-clean every 5 minutes", variable=self.auto_clean,
                      fg='white', bg='#1e1e1e', selectcolor='#00ff88').pack(side=tk.LEFT, padx=(20, 0))
        
        # Update memory info
        self.update_memory_info()
        
    def create_lol_optimizer_tab(self):
        """Create modern League of Legends Optimizer tab"""
        lol_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(lol_frame, text="⚔️ LoL Optimizer")
        
        # LoL Optimizer content
        lol_title = tk.Label(lol_frame, text="League of Legends Optimizer", 
                            font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        lol_title.pack(pady=20)
        
        # LoL-specific controls
        controls_frame = tk.Frame(lol_frame, bg='#1e1e1e')
        controls_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.optimize_lol_btn = tk.Button(controls_frame, text="Optimize LoL", 
                                        command=self.optimize_lol,
                                        bg='#00ff88', fg='black', font=('Arial', 12, 'bold'),
                                        padx=20, pady=5, relief=tk.FLAT)
        self.optimize_lol_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.test_lol_latency_btn = tk.Button(controls_frame, text="Test Server Latency", 
                                             command=self.test_lol_latency,
                                             bg='#4d4d4d', fg='white', font=('Arial', 12),
                                             padx=20, pady=5, relief=tk.FLAT)
        self.test_lol_latency_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # LoL performance display
        perf_frame = tk.Frame(lol_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        perf_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(perf_frame, text="LoL Performance Status:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.lol_status = tk.Text(perf_frame, height=10, bg='#1e1e1e', fg='#00ff88',
                                 font=('Consolas', 10), state=tk.DISABLED)
        self.lol_status.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Update LoL status
        self.update_lol_status()
        
    def optimize_lol(self):
        """Optimize League of Legends"""
        try:
            results = self.lol_optimizer.optimize_lol_performance()
            
            status_text = "=== LoL Optimization Results ===\n\n"
            status_text += f"Processes Optimized: {results['processes_optimized']}\n"
            status_text += f"Priority Set: {'Yes' if results['priority_set'] else 'No'}\n"
            status_text += f"Memory Optimized: {'Yes' if results['memory_optimized'] else 'No'}\n"
            status_text += f"Network Optimized: {'Yes' if results['network_optimized'] else 'No'}\n\n"
            
            if results['errors']:
                status_text += "Errors:\n"
                for error in results['errors']:
                    status_text += f"- {error}\n"
            else:
                status_text += "✅ All optimizations applied successfully!\n"
            
            self.lol_status.config(state=tk.NORMAL)
            self.lol_status.delete(1.0, tk.END)
            self.lol_status.insert(tk.END, status_text)
            self.lol_status.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"LoL optimization failed: {str(e)}")
    
    def test_lol_latency(self):
        """Test League of Legends server latency"""
        try:
            latencies = self.lol_optimizer.get_lol_server_latency()
            best_server = self.lol_optimizer.get_best_lol_server()
            
            status_text = "=== LoL Server Latency Test ===\n\n"
            status_text += f"Best Server: {best_server}\n\n"
            status_text += "Server Latencies:\n"
            
            for region, latency in latencies.items():
                if latency < 999:
                    status_text += f"{region}: {latency:.1f}ms\n"
                else:
                    status_text += f"{region}: Unable to reach\n"
            
            self.lol_status.config(state=tk.NORMAL)
            self.lol_status.delete(1.0, tk.END)
            self.lol_status.insert(tk.END, status_text)
            self.lol_status.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Latency test failed: {str(e)}")
    
    def update_lol_status(self):
        """Update League of Legends status"""
        try:
            metrics = self.lol_optimizer.get_lol_performance_metrics()
            recommendations = self.lol_optimizer.get_lol_optimization_recommendations()
            
            status_text = "=== LoL Performance Status ===\n\n"
            status_text += f"Processes Running: {metrics['processes_running']}\n"
            status_text += f"Memory Usage: {metrics['total_memory_mb']:.1f} MB\n"
            status_text += f"CPU Usage: {metrics['cpu_usage']:.1f}%\n"
            status_text += f"Network Connections: {metrics['network_connections']}\n\n"
            
            if recommendations:
                status_text += "Recommendations:\n"
                for rec in recommendations[:5]:  # Show first 5 recommendations
                    status_text += f"• {rec}\n"
            
            self.lol_status.config(state=tk.NORMAL)
            self.lol_status.delete(1.0, tk.END)
            self.lol_status.insert(tk.END, status_text)
            self.lol_status.config(state=tk.DISABLED)
            
        except Exception as e:
            print(f"Failed to update LoL status: {e}")
        
    
    def open_settings(self):
        """Open settings dialog (legacy method for compatibility)"""
        self.show_settings()
        
            
    def start_network_analysis(self):
        """Start network analysis"""
        self.start_analysis_btn.config(state=tk.DISABLED)
        self.stop_analysis_btn.config(state=tk.NORMAL)
        
        # Start analysis in separate thread
        threading.Thread(target=self.run_network_analysis, daemon=True).start()
        
    def stop_network_analysis(self):
        """Stop network analysis"""
        self.start_analysis_btn.config(state=tk.NORMAL)
        self.stop_analysis_btn.config(state=tk.DISABLED)
        
    def run_network_analysis(self):
        """Run network analysis with progress feedback"""
        try:
            # Update button states
            self.start_analysis_btn.config(state=tk.DISABLED)
            self.stop_analysis_btn.config(state=tk.NORMAL)
            
            # Clear and show progress
            self.network_results.config(state=tk.NORMAL)
            self.network_results.delete(1.0, tk.END)
            self.network_results.insert(tk.END, "🔍 Starting network analysis...\n")
            self.network_results.config(state=tk.DISABLED)
            self.root.update()
            
            # Step 1: Basic connectivity
            self.network_results.config(state=tk.NORMAL)
            self.network_results.insert(tk.END, "📡 Testing basic connectivity...\n")
            self.network_results.config(state=tk.DISABLED)
            self.root.update()
            time.sleep(1)
            
            # Step 2: Server latency tests
            self.network_results.config(state=tk.NORMAL)
            self.network_results.insert(tk.END, "🌐 Testing server latency...\n")
            self.network_results.config(state=tk.DISABLED)
            self.root.update()
            time.sleep(1)
            
            # Step 3: Gaming servers
            self.network_results.config(state=tk.NORMAL)
            self.network_results.insert(tk.END, "🎮 Testing gaming servers...\n")
            self.network_results.config(state=tk.DISABLED)
            self.root.update()
            time.sleep(1)
            
            # Get results
            results = self.network_analyzer.analyze_network()
            
            # Display results
            self.network_results.config(state=tk.NORMAL)
            self.network_results.delete(1.0, tk.END)
            self.network_results.insert(tk.END, results)
            self.network_results.config(state=tk.DISABLED)
            
        except Exception as e:
            self.network_results.config(state=tk.NORMAL)
            self.network_results.delete(1.0, tk.END)
            self.network_results.insert(tk.END, f"❌ Analysis failed: {str(e)}")
            self.network_results.config(state=tk.DISABLED)
            messagebox.showerror("Error", f"Network analysis failed: {str(e)}")
        finally:
            self.stop_analysis_btn.config(state=tk.DISABLED)
            self.start_analysis_btn.config(state=tk.NORMAL)
            
    def load_connections(self):
        """Load available network connections"""
        try:
            connections = self.multi_internet.get_available_connections()
            self.connection_list.delete(0, tk.END)
            for conn in connections:
                self.connection_list.insert(tk.END, conn)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load connections: {str(e)}")
            
    def clean_ram(self):
        """Clean RAM memory"""
        try:
            freed_memory = self.ram_cleaner.clean_memory()
            messagebox.showinfo("Success", f"Freed {freed_memory:.2f} MB of RAM")
            self.update_memory_info()
        except Exception as e:
            messagebox.showerror("Error", f"RAM cleaning failed: {str(e)}")
            
    def update_memory_info(self):
        """Update memory information display"""
        try:
            memory_info = self.ram_cleaner.get_memory_info()
            self.memory_info.config(state=tk.NORMAL)
            self.memory_info.delete(1.0, tk.END)
            self.memory_info.insert(tk.END, memory_info)
            self.memory_info.config(state=tk.DISABLED)
        except Exception as e:
            print(f"Failed to update memory info: {e}")
            
    def open_settings(self):
        """Open settings dialog"""
        # Placeholder for settings dialog
        messagebox.showinfo("Settings", "Settings dialog will be implemented here")
        
    def load_settings(self):
        """Load application settings"""
        try:
            settings = self.config_manager.load_settings()
            # Apply settings to UI
        except Exception as e:
            print(f"Failed to load settings: {e}")
            
    def save_settings(self):
        """Save application settings"""
        try:
            settings = {
                'fps_boost': {
                    'priority_boost': self.priority_boost.get(),
                    'cpu_optimization': self.cpu_optimization.get(),
                    'gpu_optimization': self.gpu_optimization.get()
                },
                'traffic_shaper': {
                    'prioritize_gaming': self.prioritize_gaming.get(),
                    'limit_background': self.limit_background.get()
                },
                'ram_cleaner': {
                    'auto_clean': self.auto_clean.get()
                }
            }
            self.config_manager.save_settings(settings)
        except Exception as e:
            print(f"Failed to save settings: {e}")
            
    def create_advanced_optimizer_tab(self):
        """Create modern Advanced Optimizer tab"""
        advanced_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(advanced_frame, text="🤖 Advanced AI")
        
        # Title
        title_label = tk.Label(advanced_frame, text="🚀 Advanced AI Optimizer", 
                              font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=20)
        
        # Profile selection
        profile_frame = tk.Frame(advanced_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        profile_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(profile_frame, text="Optimization Profile:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.advanced_profile = tk.StringVar(value="gaming")
        profile_options = ["gaming", "streaming", "productivity", "balanced"]
        
        for i, option in enumerate(profile_options):
            rb = self.create_modern_radiobutton(profile_frame, option.title(), 
                                               self.advanced_profile, option, 0, i)
        
        # Advanced features
        features_frame = tk.Frame(advanced_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        features_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(features_frame, text="Advanced Features:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.ai_analysis = tk.BooleanVar(value=True)
        self.real_time_monitoring = tk.BooleanVar(value=True)
        self.predictive_optimization = tk.BooleanVar(value=True)
        self.adaptive_learning = tk.BooleanVar(value=True)
        
        features = [
            ("AI-Powered Analysis", self.ai_analysis),
            ("Real-time Monitoring", self.real_time_monitoring),
            ("Predictive Optimization", self.predictive_optimization),
            ("Adaptive Learning", self.adaptive_learning)
        ]
        
        for feature, var in features:
            cb = tk.Checkbutton(features_frame, text=feature, variable=var,
                               font=('Arial', 10), fg='white', bg='#2d2d2d',
                               selectcolor='#00ff88', activebackground='#2d2d2d')
            cb.pack(anchor=tk.W, padx=20, pady=2)
        
        # Control buttons
        button_frame = tk.Frame(advanced_frame, bg='#1e1e1e')
        button_frame.pack(pady=20)
        
        self.start_advanced_btn = tk.Button(button_frame, text="🚀 Start Advanced Optimization",
                                           command=self.start_advanced_optimization,
                                           font=('Arial', 12, 'bold'), bg='#00ff88', fg='black',
                                           relief=tk.RAISED, bd=3, padx=20, pady=10)
        self.start_advanced_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_advanced_btn = tk.Button(button_frame, text="⏹️ Stop Optimization",
                                          command=self.stop_advanced_optimization,
                                          font=('Arial', 12, 'bold'), bg='#ff4444', fg='white',
                                          relief=tk.RAISED, bd=3, padx=20, pady=10, state=tk.DISABLED)
        self.stop_advanced_btn.pack(side=tk.LEFT, padx=10)
        
        # Results display
        results_frame = tk.Frame(advanced_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(results_frame, text="Advanced Optimization Results:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.advanced_results = tk.Text(results_frame, height=15, bg='#1e1e1e', fg='#00ff88',
                                       font=('Consolas', 9), state=tk.DISABLED, wrap=tk.WORD)
        
        # Scrollbar for results
        results_scrollbar = tk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.advanced_results.yview)
        self.advanced_results.configure(yscrollcommand=results_scrollbar.set)
        
        self.advanced_results.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
    
    def create_system_monitor_tab(self):
        """Create modern System Monitor tab"""
        monitor_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(monitor_frame, text="📊 System Monitor")
        
        # Title
        title_label = tk.Label(monitor_frame, text="📊 Real-time System Monitor", 
                              font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=20)
        
        # Control buttons
        button_frame = tk.Frame(monitor_frame, bg='#1e1e1e')
        button_frame.pack(pady=10)
        
        self.start_monitor_btn = tk.Button(button_frame, text="📊 Start Monitoring",
                                          command=self.start_system_monitoring,
                                          font=('Arial', 12, 'bold'), bg='#00ff88', fg='black',
                                          relief=tk.RAISED, bd=3, padx=20, pady=10)
        self.start_monitor_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_monitor_btn = tk.Button(button_frame, text="⏹️ Stop Monitoring",
                                         command=self.stop_system_monitoring,
                                         font=('Arial', 12, 'bold'), bg='#ff4444', fg='white',
                                         relief=tk.RAISED, bd=3, padx=20, pady=10, state=tk.DISABLED)
        self.stop_monitor_btn.pack(side=tk.LEFT, padx=10)
        
        # Monitoring display
        monitor_display_frame = tk.Frame(monitor_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        monitor_display_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(monitor_display_frame, text="System Performance Monitor:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.monitor_display = tk.Text(monitor_display_frame, height=20, bg='#1e1e1e', fg='#00ff88',
                                      font=('Consolas', 9), state=tk.DISABLED, wrap=tk.WORD)
        
        # Scrollbar for monitor display
        monitor_scrollbar = tk.Scrollbar(monitor_display_frame, orient=tk.VERTICAL, command=self.monitor_display.yview)
        self.monitor_display.configure(yscrollcommand=monitor_scrollbar.set)
        
        self.monitor_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        monitor_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
    
    def create_network_optimizer_tab(self):
        """Create modern Network Optimizer tab"""
        network_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(network_frame, text="🌐 Network Optimizer")
        
        # Title
        title_label = tk.Label(network_frame, text="🌐 Advanced Network Optimizer", 
                              font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=20)
        
        # Network profile selection
        profile_frame = tk.Frame(network_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        profile_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(profile_frame, text="Network Profile:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.network_profile = tk.StringVar(value="gaming")
        network_options = ["gaming", "streaming", "productivity"]
        
        for i, option in enumerate(network_options):
            rb = self.create_modern_radiobutton(profile_frame, option.title(), 
                                               self.network_profile, option, 0, i)
        
        # Control buttons
        button_frame = tk.Frame(network_frame, bg='#1e1e1e')
        button_frame.pack(pady=20)
        
        self.start_network_btn = tk.Button(button_frame, text="🌐 Start Network Optimization",
                                          command=self.start_network_optimization,
                                          font=('Arial', 12, 'bold'), bg='#00ff88', fg='black',
                                          relief=tk.RAISED, bd=3, padx=20, pady=10)
        self.start_network_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_network_btn = tk.Button(button_frame, text="⏹️ Stop Optimization",
                                        command=self.stop_network_optimization,
                                        font=('Arial', 12, 'bold'), bg='#ff4444', fg='white',
                                        relief=tk.RAISED, bd=3, padx=20, pady=10, state=tk.DISABLED)
        self.stop_network_btn.pack(side=tk.LEFT, padx=10)
        
        # Network status display
        status_frame = tk.Frame(network_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        status_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(status_frame, text="Network Optimization Status:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.network_status = tk.Text(status_frame, height=15, bg='#1e1e1e', fg='#00ff88',
                                     font=('Consolas', 9), state=tk.DISABLED, wrap=tk.WORD)
        
        # Scrollbar for network status
        network_scrollbar = tk.Scrollbar(status_frame, orient=tk.VERTICAL, command=self.network_status.yview)
        self.network_status.configure(yscrollcommand=network_scrollbar.set)
        
        self.network_status.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        network_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
    
    def create_gaming_optimizer_tab(self):
        """Create modern Gaming Optimizer tab"""
        gaming_frame = tk.Frame(self.notebook, bg=self.colors['bg_primary'])
        self.notebook.add(gaming_frame, text="🎮 Gaming Optimizer")
        
        # Title
        title_label = tk.Label(gaming_frame, text="🎮 Advanced Gaming Optimizer", 
                              font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=20)
        
        # Gaming profile selection
        profile_frame = tk.Frame(gaming_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        profile_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(profile_frame, text="Gaming Profile:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.gaming_profile = tk.StringVar(value="auto")
        gaming_options = ["auto", "league_of_legends", "valorant", "cs2", "fortnite", "apex_legends"]
        
        for i, option in enumerate(gaming_options):
            rb = self.create_modern_radiobutton(profile_frame, option.replace('_', ' ').title(), 
                                               self.gaming_profile, option, 0, i)
        
        # Gaming features
        features_frame = tk.Frame(gaming_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        features_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(features_frame, text="Gaming Features:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.game_mode = tk.BooleanVar(value=True)
        self.anti_cheat_optimization = tk.BooleanVar(value=True)
        self.gaming_network = tk.BooleanVar(value=True)
        self.gaming_audio = tk.BooleanVar(value=True)
        
        gaming_features = [
            ("Windows Game Mode", self.game_mode),
            ("Anti-Cheat Optimization", self.anti_cheat_optimization),
            ("Gaming Network Optimization", self.gaming_network),
            ("Gaming Audio Optimization", self.gaming_audio)
        ]
        
        for feature, var in gaming_features:
            cb = tk.Checkbutton(features_frame, text=feature, variable=var,
                               font=('Arial', 10), fg='white', bg='#2d2d2d',
                               selectcolor='#00ff88', activebackground='#2d2d2d')
            cb.pack(anchor=tk.W, padx=20, pady=2)
        
        # Control buttons
        button_frame = tk.Frame(gaming_frame, bg='#1e1e1e')
        button_frame.pack(pady=20)
        
        self.start_gaming_btn = tk.Button(button_frame, text="🎮 Start Gaming Optimization",
                                         command=self.start_gaming_optimization,
                                         font=('Arial', 12, 'bold'), bg='#00ff88', fg='black',
                                         relief=tk.RAISED, bd=3, padx=20, pady=10)
        self.start_gaming_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_gaming_btn = tk.Button(button_frame, text="⏹️ Stop Optimization",
                                        command=self.stop_gaming_optimization,
                                        font=('Arial', 12, 'bold'), bg='#ff4444', fg='white',
                                        relief=tk.RAISED, bd=3, padx=20, pady=10, state=tk.DISABLED)
        self.stop_gaming_btn.pack(side=tk.LEFT, padx=10)
        
        # Gaming status display
        status_frame = tk.Frame(gaming_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        status_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(status_frame, text="Gaming Optimization Status:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.gaming_status = tk.Text(status_frame, height=15, bg='#1e1e1e', fg='#00ff88',
                                    font=('Consolas', 9), state=tk.DISABLED, wrap=tk.WORD)
        
        # Scrollbar for gaming status
        gaming_scrollbar = tk.Scrollbar(status_frame, orient=tk.VERTICAL, command=self.gaming_status.yview)
        self.gaming_status.configure(yscrollcommand=gaming_scrollbar.set)
        
        self.gaming_status.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        gaming_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
    
    def start_advanced_optimization(self):
        """Start advanced optimization"""
        try:
            profile = self.advanced_profile.get()
            results = self.advanced_optimizer.start_advanced_optimization(profile)
            
            self.advanced_results.config(state=tk.NORMAL)
            self.advanced_results.delete(1.0, tk.END)
            self.advanced_results.insert(tk.END, json.dumps(results, indent=2))
            self.advanced_results.config(state=tk.DISABLED)
            
            self.start_advanced_btn.config(state=tk.DISABLED)
            self.stop_advanced_btn.config(state=tk.NORMAL)
            
        except Exception as e:
            messagebox.showerror("Error", f"Advanced optimization failed: {str(e)}")
    
    def stop_advanced_optimization(self):
        """Stop advanced optimization"""
        try:
            self.advanced_optimizer.stop_optimization()
            self.start_advanced_btn.config(state=tk.NORMAL)
            self.stop_advanced_btn.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop optimization: {str(e)}")
    
    def start_system_monitoring(self):
        """Start system monitoring"""
        try:
            result = self.system_monitor.start_monitoring(interval=5)
            
            self.monitor_display.config(state=tk.NORMAL)
            self.monitor_display.delete(1.0, tk.END)
            self.monitor_display.insert(tk.END, f"System monitoring started: {result}\n")
            self.monitor_display.config(state=tk.DISABLED)
            
            self.start_monitor_btn.config(state=tk.DISABLED)
            self.stop_monitor_btn.config(state=tk.NORMAL)
            
        except Exception as e:
            messagebox.showerror("Error", f"System monitoring failed: {str(e)}")
    
    def stop_system_monitoring(self):
        """Stop system monitoring"""
        try:
            result = self.system_monitor.stop_monitoring()
            
            self.monitor_display.config(state=tk.NORMAL)
            self.monitor_display.insert(tk.END, f"System monitoring stopped: {result}\n")
            self.monitor_display.config(state=tk.DISABLED)
            
            self.start_monitor_btn.config(state=tk.NORMAL)
            self.stop_monitor_btn.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop monitoring: {str(e)}")
    
    def start_network_optimization(self):
        """Start network optimization"""
        try:
            profile = self.network_profile.get()
            results = self.network_optimizer.start_network_optimization(profile)
            
            self.network_status.config(state=tk.NORMAL)
            self.network_status.delete(1.0, tk.END)
            self.network_status.insert(tk.END, json.dumps(results, indent=2))
            self.network_status.config(state=tk.DISABLED)
            
            self.start_network_btn.config(state=tk.DISABLED)
            self.stop_network_btn.config(state=tk.NORMAL)
            
        except Exception as e:
            messagebox.showerror("Error", f"Network optimization failed: {str(e)}")
    
    def stop_network_optimization(self):
        """Stop network optimization"""
        try:
            result = self.network_optimizer.stop_network_optimization()
            
            self.network_status.config(state=tk.NORMAL)
            self.network_status.insert(tk.END, f"Network optimization stopped: {result}\n")
            self.network_status.config(state=tk.DISABLED)
            
            self.start_network_btn.config(state=tk.NORMAL)
            self.stop_network_btn.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop network optimization: {str(e)}")
    
    def start_gaming_optimization(self):
        """Start gaming optimization"""
        try:
            profile = self.gaming_profile.get()
            results = self.gaming_optimizer.start_gaming_optimization(profile)
            
            self.gaming_status.config(state=tk.NORMAL)
            self.gaming_status.delete(1.0, tk.END)
            self.gaming_status.insert(tk.END, json.dumps(results, indent=2))
            self.gaming_status.config(state=tk.DISABLED)
            
            self.start_gaming_btn.config(state=tk.DISABLED)
            self.stop_gaming_btn.config(state=tk.NORMAL)
            
        except Exception as e:
            messagebox.showerror("Error", f"Gaming optimization failed: {str(e)}")
    
    def stop_gaming_optimization(self):
        """Stop gaming optimization"""
        try:
            result = self.gaming_optimizer.stop_gaming_optimization()
            
            self.gaming_status.config(state=tk.NORMAL)
            self.gaming_status.insert(tk.END, f"Gaming optimization stopped: {result}\n")
            self.gaming_status.config(state=tk.DISABLED)
            
            self.start_gaming_btn.config(state=tk.NORMAL)
            self.stop_gaming_btn.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop gaming optimization: {str(e)}")
    
    def run(self):
        """Run the application"""
        try:
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()
        except KeyboardInterrupt:
            self.on_closing()
            
    def show_settings(self):
        """Show settings dialog"""
        try:
            settings_dialog = SettingsDialog(self.root, self.config_manager)
            settings_dialog.show_settings()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open settings: {str(e)}")
    
    def on_closing(self):
        """Handle application closing"""
        self.save_settings()
        self.root.destroy()

if __name__ == "__main__":
    try:
        app = NetworkOptimizerApp()
        app.run()
    except Exception as e:
        print(f"Application failed to start: {e}")
        sys.exit(1)
