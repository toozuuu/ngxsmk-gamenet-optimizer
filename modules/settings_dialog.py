"""
Settings Dialog Module
Advanced settings dialog with comprehensive configuration options
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from typing import Dict, Any, Optional

class SettingsDialog:
    """Advanced settings dialog for NGXSMK GameNet Optimizer"""
    
    def __init__(self, parent, config_manager):
        self.parent = parent
        self.config_manager = config_manager
        self.settings = {}
        self.dialog = None
        
    def show_settings(self):
        """Show the settings dialog"""
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title("⚙️ NGXSMK GameNet Optimizer - Settings")
        self.dialog.geometry("800x600")
        self.dialog.configure(bg='#1e1e1e')
        self.dialog.resizable(True, True)
        
        # Center the dialog
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # Load current settings
        self.settings = self.config_manager.load_settings()
        
        # Create notebook for different setting categories
        self.create_settings_notebook()
        
        # Create buttons
        self.create_buttons()
        
        # Center the dialog
        self.center_dialog()
        
    def create_settings_notebook(self):
        """Create settings notebook with different categories"""
        # Main frame
        main_frame = tk.Frame(self.dialog, bg='#1e1e1e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Notebook for settings categories
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Configure notebook style
        style = ttk.Style()
        style.configure('TNotebook', background='#2d2d2d')
        style.configure('TNotebook.Tab', background='#2d2d2d', foreground='white')
        
        # Create different setting tabs
        self.create_general_tab()
        self.create_optimization_tab()
        self.create_network_tab()
        self.create_gaming_tab()
        self.create_monitoring_tab()
        self.create_advanced_tab()
        
    def create_general_tab(self):
        """Create general settings tab"""
        general_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(general_frame, text="General")
        
        # Title
        title_label = tk.Label(general_frame, text="🔧 General Settings", 
                              font=('Arial', 14, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=10)
        
        # Auto-start settings
        auto_frame = tk.Frame(general_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        auto_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(auto_frame, text="Auto-Start Settings:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.auto_start = tk.BooleanVar(value=self.settings.get('general', {}).get('auto_start', False))
        self.start_minimized = tk.BooleanVar(value=self.settings.get('general', {}).get('start_minimized', False))
        self.auto_optimize = tk.BooleanVar(value=self.settings.get('general', {}).get('auto_optimize', False))
        
        tk.Checkbutton(auto_frame, text="Start with Windows", variable=self.auto_start,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(auto_frame, text="Start minimized", variable=self.start_minimized,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(auto_frame, text="Auto-optimize on startup", variable=self.auto_optimize,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        # UI settings
        ui_frame = tk.Frame(general_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        ui_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(ui_frame, text="UI Settings:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.theme = tk.StringVar(value=self.settings.get('general', {}).get('theme', 'dark'))
        self.language = tk.StringVar(value=self.settings.get('general', {}).get('language', 'en'))
        
        # Theme selection
        theme_frame = tk.Frame(ui_frame, bg='#2d2d2d')
        theme_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(theme_frame, text="Theme:", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        theme_options = ["dark", "light", "gaming"]
        for i, option in enumerate(theme_options):
            rb = tk.Radiobutton(theme_frame, text=option.title(), variable=self.theme,
                              value=option, font=('Arial', 9), fg='white', bg='#2d2d2d',
                              selectcolor='#00ff88', activebackground='#2d2d2d')
            rb.pack(side=tk.LEFT, padx=10)
            # Ensure proper grouping by setting the same variable
            rb.config(variable=self.theme)
        
        # Language selection
        lang_frame = tk.Frame(ui_frame, bg='#2d2d2d')
        lang_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(lang_frame, text="Language:", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        lang_combo = ttk.Combobox(lang_frame, textvariable=self.language, 
                               values=["en", "es", "fr", "de", "zh", "ja"], state="readonly")
        lang_combo.pack(side=tk.LEFT, padx=10)
        
    def create_optimization_tab(self):
        """Create optimization settings tab"""
        opt_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(opt_frame, text="Optimization")
        
        # Title
        title_label = tk.Label(opt_frame, text="⚡ Optimization Settings", 
                              font=('Arial', 14, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=10)
        
        # CPU optimization
        cpu_frame = tk.Frame(opt_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        cpu_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(cpu_frame, text="CPU Optimization:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.cpu_aggressive = tk.BooleanVar(value=self.settings.get('optimization', {}).get('cpu_aggressive', False))
        self.cpu_priority = tk.StringVar(value=self.settings.get('optimization', {}).get('cpu_priority', 'normal'))
        
        tk.Checkbutton(cpu_frame, text="Aggressive CPU optimization", variable=self.cpu_aggressive,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        # CPU priority selection
        priority_frame = tk.Frame(cpu_frame, bg='#2d2d2d')
        priority_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(priority_frame, text="CPU Priority:", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        priority_options = ["low", "normal", "high", "realtime"]
        for i, option in enumerate(priority_options):
            rb = tk.Radiobutton(priority_frame, text=option.title(), variable=self.cpu_priority,
                              value=option, font=('Arial', 9), fg='white', bg='#2d2d2d',
                              selectcolor='#00ff88', activebackground='#2d2d2d')
            rb.pack(side=tk.LEFT, padx=5)
            # Ensure proper grouping by setting the same variable
            rb.config(variable=self.cpu_priority)
        
        # Memory optimization
        mem_frame = tk.Frame(opt_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        mem_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(mem_frame, text="Memory Optimization:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.mem_aggressive = tk.BooleanVar(value=self.settings.get('optimization', {}).get('mem_aggressive', False))
        self.mem_threshold = tk.IntVar(value=self.settings.get('optimization', {}).get('mem_threshold', 80))
        
        tk.Checkbutton(mem_frame, text="Aggressive memory cleanup", variable=self.mem_aggressive,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        # Memory threshold
        threshold_frame = tk.Frame(mem_frame, bg='#2d2d2d')
        threshold_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(threshold_frame, text="Memory threshold (%):", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        threshold_scale = tk.Scale(threshold_frame, from_=50, to=95, orient=tk.HORIZONTAL,
                                 variable=self.mem_threshold, bg='#2d2d2d', fg='white',
                                 highlightbackground='#2d2d2d', troughcolor='#404040')
        threshold_scale.pack(side=tk.LEFT, padx=10)
        
    def create_network_tab(self):
        """Create network settings tab"""
        net_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(net_frame, text="Network")
        
        # Title
        title_label = tk.Label(net_frame, text="🌐 Network Settings", 
                              font=('Arial', 14, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=10)
        
        # DNS settings
        dns_frame = tk.Frame(net_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        dns_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(dns_frame, text="DNS Settings:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.custom_dns = tk.BooleanVar(value=self.settings.get('network', {}).get('custom_dns', False))
        self.dns_primary = tk.StringVar(value=self.settings.get('network', {}).get('dns_primary', '8.8.8.8'))
        self.dns_secondary = tk.StringVar(value=self.settings.get('network', {}).get('dns_secondary', '8.8.4.4'))
        
        tk.Checkbutton(dns_frame, text="Use custom DNS servers", variable=self.custom_dns,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        # DNS server inputs
        dns_input_frame = tk.Frame(dns_frame, bg='#2d2d2d')
        dns_input_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(dns_input_frame, text="Primary DNS:", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        dns_primary_entry = tk.Entry(dns_input_frame, textvariable=self.dns_primary, width=15)
        dns_primary_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Label(dns_input_frame, text="Secondary DNS:", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT, padx=(20, 0))
        dns_secondary_entry = tk.Entry(dns_input_frame, textvariable=self.dns_secondary, width=15)
        dns_secondary_entry.pack(side=tk.LEFT, padx=5)
        
        # Network optimization
        net_opt_frame = tk.Frame(net_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        net_opt_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(net_opt_frame, text="Network Optimization:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.tcp_optimization = tk.BooleanVar(value=self.settings.get('network', {}).get('tcp_optimization', True))
        self.udp_optimization = tk.BooleanVar(value=self.settings.get('network', {}).get('udp_optimization', True))
        self.qos_enabled = tk.BooleanVar(value=self.settings.get('network', {}).get('qos_enabled', True))
        
        tk.Checkbutton(net_opt_frame, text="TCP optimization", variable=self.tcp_optimization,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(net_opt_frame, text="UDP optimization", variable=self.udp_optimization,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(net_opt_frame, text="Quality of Service (QoS)", variable=self.qos_enabled,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
    def create_gaming_tab(self):
        """Create gaming settings tab"""
        gaming_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(gaming_frame, text="Gaming")
        
        # Title
        title_label = tk.Label(gaming_frame, text="🎮 Gaming Settings", 
                              font=('Arial', 14, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=10)
        
        # Game detection
        detection_frame = tk.Frame(gaming_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        detection_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(detection_frame, text="Game Detection:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.auto_detect_games = tk.BooleanVar(value=self.settings.get('gaming', {}).get('auto_detect_games', True))
        self.game_mode = tk.BooleanVar(value=self.settings.get('gaming', {}).get('game_mode', True))
        self.anti_cheat_optimization = tk.BooleanVar(value=self.settings.get('gaming', {}).get('anti_cheat_optimization', True))
        
        tk.Checkbutton(detection_frame, text="Auto-detect running games", variable=self.auto_detect_games,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(detection_frame, text="Enable Windows Game Mode", variable=self.game_mode,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(detection_frame, text="Anti-cheat optimization", variable=self.anti_cheat_optimization,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        # Gaming performance
        perf_frame = tk.Frame(gaming_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        perf_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(perf_frame, text="Gaming Performance:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.gaming_priority = tk.StringVar(value=self.settings.get('gaming', {}).get('gaming_priority', 'high'))
        self.fps_boost = tk.BooleanVar(value=self.settings.get('gaming', {}).get('fps_boost', True))
        self.latency_optimization = tk.BooleanVar(value=self.settings.get('gaming', {}).get('latency_optimization', True))
        
        # Gaming priority
        priority_frame = tk.Frame(perf_frame, bg='#2d2d2d')
        priority_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(priority_frame, text="Gaming Priority:", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        gaming_priority_options = ["low", "normal", "high", "realtime"]
        for i, option in enumerate(gaming_priority_options):
            rb = tk.Radiobutton(priority_frame, text=option.title(), variable=self.gaming_priority,
                              value=option, font=('Arial', 9), fg='white', bg='#2d2d2d',
                              selectcolor='#00ff88', activebackground='#2d2d2d')
            rb.pack(side=tk.LEFT, padx=5)
            # Ensure proper grouping by setting the same variable
            rb.config(variable=self.gaming_priority)
        
        tk.Checkbutton(perf_frame, text="FPS boost optimization", variable=self.fps_boost,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(perf_frame, text="Latency optimization", variable=self.latency_optimization,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
    def create_monitoring_tab(self):
        """Create monitoring settings tab"""
        monitor_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(monitor_frame, text="Monitoring")
        
        # Title
        title_label = tk.Label(monitor_frame, text="📊 Monitoring Settings", 
                              font=('Arial', 14, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=10)
        
        # Real-time monitoring
        rt_frame = tk.Frame(monitor_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        rt_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(rt_frame, text="Real-time Monitoring:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.monitoring_enabled = tk.BooleanVar(value=self.settings.get('monitoring', {}).get('monitoring_enabled', True))
        self.monitoring_interval = tk.IntVar(value=self.settings.get('monitoring', {}).get('monitoring_interval', 5))
        self.alerts_enabled = tk.BooleanVar(value=self.settings.get('monitoring', {}).get('alerts_enabled', True))
        
        tk.Checkbutton(rt_frame, text="Enable real-time monitoring", variable=self.monitoring_enabled,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        # Monitoring interval
        interval_frame = tk.Frame(rt_frame, bg='#2d2d2d')
        interval_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(interval_frame, text="Monitoring interval (seconds):", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        interval_scale = tk.Scale(interval_frame, from_=1, to=60, orient=tk.HORIZONTAL,
                                 variable=self.monitoring_interval, bg='#2d2d2d', fg='white',
                                 highlightbackground='#2d2d2d', troughcolor='#404040')
        interval_scale.pack(side=tk.LEFT, padx=10)
        
        tk.Checkbutton(rt_frame, text="Enable performance alerts", variable=self.alerts_enabled,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        # Alert thresholds
        alert_frame = tk.Frame(monitor_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        alert_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(alert_frame, text="Alert Thresholds:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.cpu_threshold = tk.IntVar(value=self.settings.get('monitoring', {}).get('cpu_threshold', 80))
        self.memory_threshold = tk.IntVar(value=self.settings.get('monitoring', {}).get('memory_threshold', 85))
        self.temperature_threshold = tk.IntVar(value=self.settings.get('monitoring', {}).get('temperature_threshold', 75))
        
        # CPU threshold
        cpu_thresh_frame = tk.Frame(alert_frame, bg='#2d2d2d')
        cpu_thresh_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(cpu_thresh_frame, text="CPU threshold (%):", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        cpu_scale = tk.Scale(cpu_thresh_frame, from_=50, to=95, orient=tk.HORIZONTAL,
                            variable=self.cpu_threshold, bg='#2d2d2d', fg='white',
                            highlightbackground='#2d2d2d', troughcolor='#404040')
        cpu_scale.pack(side=tk.LEFT, padx=10)
        
        # Memory threshold
        mem_thresh_frame = tk.Frame(alert_frame, bg='#2d2d2d')
        mem_thresh_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(mem_thresh_frame, text="Memory threshold (%):", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        mem_scale = tk.Scale(mem_thresh_frame, from_=50, to=95, orient=tk.HORIZONTAL,
                            variable=self.memory_threshold, bg='#2d2d2d', fg='white',
                            highlightbackground='#2d2d2d', troughcolor='#404040')
        mem_scale.pack(side=tk.LEFT, padx=10)
        
        # Temperature threshold
        temp_thresh_frame = tk.Frame(alert_frame, bg='#2d2d2d')
        temp_thresh_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Label(temp_thresh_frame, text="Temperature threshold (°C):", font=('Arial', 10), fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        temp_scale = tk.Scale(temp_thresh_frame, from_=50, to=90, orient=tk.HORIZONTAL,
                             variable=self.temperature_threshold, bg='#2d2d2d', fg='white',
                             highlightbackground='#2d2d2d', troughcolor='#404040')
        temp_scale.pack(side=tk.LEFT, padx=10)
        
    def create_advanced_tab(self):
        """Create advanced settings tab"""
        advanced_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(advanced_frame, text="Advanced")
        
        # Title
        title_label = tk.Label(advanced_frame, text="🔬 Advanced Settings", 
                              font=('Arial', 14, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(pady=10)
        
        # AI settings
        ai_frame = tk.Frame(advanced_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        ai_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(ai_frame, text="AI Optimization:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.ai_enabled = tk.BooleanVar(value=self.settings.get('advanced', {}).get('ai_enabled', True))
        self.predictive_optimization = tk.BooleanVar(value=self.settings.get('advanced', {}).get('predictive_optimization', True))
        self.adaptive_learning = tk.BooleanVar(value=self.settings.get('advanced', {}).get('adaptive_learning', True))
        
        tk.Checkbutton(ai_frame, text="Enable AI optimization", variable=self.ai_enabled,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(ai_frame, text="Predictive optimization", variable=self.predictive_optimization,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(ai_frame, text="Adaptive learning", variable=self.adaptive_learning,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        # Debug settings
        debug_frame = tk.Frame(advanced_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        debug_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(debug_frame, text="Debug Settings:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.debug_mode = tk.BooleanVar(value=self.settings.get('advanced', {}).get('debug_mode', False))
        self.verbose_logging = tk.BooleanVar(value=self.settings.get('advanced', {}).get('verbose_logging', False))
        self.performance_logging = tk.BooleanVar(value=self.settings.get('advanced', {}).get('performance_logging', False))
        
        tk.Checkbutton(debug_frame, text="Debug mode", variable=self.debug_mode,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(debug_frame, text="Verbose logging", variable=self.verbose_logging,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Checkbutton(debug_frame, text="Performance logging", variable=self.performance_logging,
                      font=('Arial', 10), fg='white', bg='#2d2d2d',
                      selectcolor='#00ff88', activebackground='#2d2d2d').pack(anchor=tk.W, padx=20, pady=2)
        
        # Export/Import settings
        export_frame = tk.Frame(advanced_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        export_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(export_frame, text="Settings Management:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        # Export/Import buttons
        button_frame = tk.Frame(export_frame, bg='#2d2d2d')
        button_frame.pack(anchor=tk.W, padx=20, pady=5)
        
        tk.Button(button_frame, text="Export Settings", command=self.export_settings,
                 font=('Arial', 10), bg='#00ff88', fg='black', relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Import Settings", command=self.import_settings,
                 font=('Arial', 10), bg='#0066cc', fg='white', relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Reset to Defaults", command=self.reset_settings,
                 font=('Arial', 10), bg='#ff4444', fg='white', relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=5)
        
    def create_buttons(self):
        """Create dialog buttons"""
        button_frame = tk.Frame(self.dialog, bg='#1e1e1e')
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Buttons
        tk.Button(button_frame, text="Save", command=self.save_settings,
                 font=('Arial', 12, 'bold'), bg='#00ff88', fg='black',
                 relief=tk.RAISED, bd=3, padx=20, pady=5).pack(side=tk.RIGHT, padx=5)
        
        tk.Button(button_frame, text="Cancel", command=self.cancel_settings,
                 font=('Arial', 12, 'bold'), bg='#666666', fg='white',
                 relief=tk.RAISED, bd=3, padx=20, pady=5).pack(side=tk.RIGHT, padx=5)
        
        tk.Button(button_frame, text="Apply", command=self.apply_settings,
                 font=('Arial', 12, 'bold'), bg='#0066cc', fg='white',
                 relief=tk.RAISED, bd=3, padx=20, pady=5).pack(side=tk.RIGHT, padx=5)
        
    def center_dialog(self):
        """Center the dialog on the parent window"""
        self.dialog.update_idletasks()
        width = self.dialog.winfo_width()
        height = self.dialog.winfo_height()
        x = (self.dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (height // 2)
        self.dialog.geometry(f"{width}x{height}+{x}+{y}")
        
    def save_settings(self):
        """Save all settings"""
        try:
            # Collect all settings
            settings = {
                'general': {
                    'auto_start': self.auto_start.get(),
                    'start_minimized': self.start_minimized.get(),
                    'auto_optimize': self.auto_optimize.get(),
                    'theme': self.theme.get(),
                    'language': self.language.get()
                },
                'optimization': {
                    'cpu_aggressive': self.cpu_aggressive.get(),
                    'cpu_priority': self.cpu_priority.get(),
                    'mem_aggressive': self.mem_aggressive.get(),
                    'mem_threshold': self.mem_threshold.get()
                },
                'network': {
                    'custom_dns': self.custom_dns.get(),
                    'dns_primary': self.dns_primary.get(),
                    'dns_secondary': self.dns_secondary.get(),
                    'tcp_optimization': self.tcp_optimization.get(),
                    'udp_optimization': self.udp_optimization.get(),
                    'qos_enabled': self.qos_enabled.get()
                },
                'gaming': {
                    'auto_detect_games': self.auto_detect_games.get(),
                    'game_mode': self.game_mode.get(),
                    'anti_cheat_optimization': self.anti_cheat_optimization.get(),
                    'gaming_priority': self.gaming_priority.get(),
                    'fps_boost': self.fps_boost.get(),
                    'latency_optimization': self.latency_optimization.get()
                },
                'monitoring': {
                    'monitoring_enabled': self.monitoring_enabled.get(),
                    'monitoring_interval': self.monitoring_interval.get(),
                    'alerts_enabled': self.alerts_enabled.get(),
                    'cpu_threshold': self.cpu_threshold.get(),
                    'memory_threshold': self.memory_threshold.get(),
                    'temperature_threshold': self.temperature_threshold.get()
                },
                'advanced': {
                    'ai_enabled': self.ai_enabled.get(),
                    'predictive_optimization': self.predictive_optimization.get(),
                    'adaptive_learning': self.adaptive_learning.get(),
                    'debug_mode': self.debug_mode.get(),
                    'verbose_logging': self.verbose_logging.get(),
                    'performance_logging': self.performance_logging.get()
                }
            }
            
            # Save settings
            self.config_manager.save_settings(settings)
            
            messagebox.showinfo("Settings", "Settings saved successfully!")
            self.dialog.destroy()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {str(e)}")
    
    def apply_settings(self):
        """Apply settings without closing dialog"""
        try:
            # Collect all settings
            settings = {
                'general': {
                    'auto_start': self.auto_start.get(),
                    'start_minimized': self.start_minimized.get(),
                    'auto_optimize': self.auto_optimize.get(),
                    'theme': self.theme.get(),
                    'language': self.language.get()
                },
                'optimization': {
                    'cpu_aggressive': self.cpu_aggressive.get(),
                    'cpu_priority': self.cpu_priority.get(),
                    'mem_aggressive': self.mem_aggressive.get(),
                    'mem_threshold': self.mem_threshold.get()
                },
                'network': {
                    'custom_dns': self.custom_dns.get(),
                    'dns_primary': self.dns_primary.get(),
                    'dns_secondary': self.dns_secondary.get(),
                    'tcp_optimization': self.tcp_optimization.get(),
                    'udp_optimization': self.udp_optimization.get(),
                    'qos_enabled': self.qos_enabled.get()
                },
                'gaming': {
                    'auto_detect_games': self.auto_detect_games.get(),
                    'game_mode': self.game_mode.get(),
                    'anti_cheat_optimization': self.anti_cheat_optimization.get(),
                    'gaming_priority': self.gaming_priority.get(),
                    'fps_boost': self.fps_boost.get(),
                    'latency_optimization': self.latency_optimization.get()
                },
                'monitoring': {
                    'monitoring_enabled': self.monitoring_enabled.get(),
                    'monitoring_interval': self.monitoring_interval.get(),
                    'alerts_enabled': self.alerts_enabled.get(),
                    'cpu_threshold': self.cpu_threshold.get(),
                    'memory_threshold': self.memory_threshold.get(),
                    'temperature_threshold': self.temperature_threshold.get()
                },
                'advanced': {
                    'ai_enabled': self.ai_enabled.get(),
                    'predictive_optimization': self.predictive_optimization.get(),
                    'adaptive_learning': self.adaptive_learning.get(),
                    'debug_mode': self.debug_mode.get(),
                    'verbose_logging': self.verbose_logging.get(),
                    'performance_logging': self.performance_logging.get()
                }
            }
            
            # Save settings
            self.config_manager.save_settings(settings)
            
            messagebox.showinfo("Settings", "Settings applied successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply settings: {str(e)}")
    
    def cancel_settings(self):
        """Cancel settings changes"""
        self.dialog.destroy()
    
    def export_settings(self):
        """Export settings to file"""
        try:
            filename = filedialog.asksaveasfilename(
                title="Export Settings",
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            
            if filename:
                settings = {
                    'general': {
                        'auto_start': self.auto_start.get(),
                        'start_minimized': self.start_minimized.get(),
                        'auto_optimize': self.auto_optimize.get(),
                        'theme': self.theme.get(),
                        'language': self.language.get()
                    },
                    'optimization': {
                        'cpu_aggressive': self.cpu_aggressive.get(),
                        'cpu_priority': self.cpu_priority.get(),
                        'mem_aggressive': self.mem_aggressive.get(),
                        'mem_threshold': self.mem_threshold.get()
                    },
                    'network': {
                        'custom_dns': self.custom_dns.get(),
                        'dns_primary': self.dns_primary.get(),
                        'dns_secondary': self.dns_secondary.get(),
                        'tcp_optimization': self.tcp_optimization.get(),
                        'udp_optimization': self.udp_optimization.get(),
                        'qos_enabled': self.qos_enabled.get()
                    },
                    'gaming': {
                        'auto_detect_games': self.auto_detect_games.get(),
                        'game_mode': self.game_mode.get(),
                        'anti_cheat_optimization': self.anti_cheat_optimization.get(),
                        'gaming_priority': self.gaming_priority.get(),
                        'fps_boost': self.fps_boost.get(),
                        'latency_optimization': self.latency_optimization.get()
                    },
                    'monitoring': {
                        'monitoring_enabled': self.monitoring_enabled.get(),
                        'monitoring_interval': self.monitoring_interval.get(),
                        'alerts_enabled': self.alerts_enabled.get(),
                        'cpu_threshold': self.cpu_threshold.get(),
                        'memory_threshold': self.memory_threshold.get(),
                        'temperature_threshold': self.temperature_threshold.get()
                    },
                    'advanced': {
                        'ai_enabled': self.ai_enabled.get(),
                        'predictive_optimization': self.predictive_optimization.get(),
                        'adaptive_learning': self.adaptive_learning.get(),
                        'debug_mode': self.debug_mode.get(),
                        'verbose_logging': self.verbose_logging.get(),
                        'performance_logging': self.performance_logging.get()
                    }
                }
                
                with open(filename, 'w') as f:
                    json.dump(settings, f, indent=2)
                
                messagebox.showinfo("Export", f"Settings exported to {filename}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export settings: {str(e)}")
    
    def import_settings(self):
        """Import settings from file"""
        try:
            filename = filedialog.askopenfilename(
                title="Import Settings",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            
            if filename:
                with open(filename, 'r') as f:
                    settings = json.load(f)
                
                # Apply imported settings
                if 'general' in settings:
                    self.auto_start.set(settings['general'].get('auto_start', False))
                    self.start_minimized.set(settings['general'].get('start_minimized', False))
                    self.auto_optimize.set(settings['general'].get('auto_optimize', False))
                    self.theme.set(settings['general'].get('theme', 'dark'))
                    self.language.set(settings['general'].get('language', 'en'))
                
                messagebox.showinfo("Import", f"Settings imported from {filename}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import settings: {str(e)}")
    
    def reset_settings(self):
        """Reset settings to defaults"""
        if messagebox.askyesno("Reset Settings", "Are you sure you want to reset all settings to defaults?"):
            try:
                # Reset to default values
                self.auto_start.set(False)
                self.start_minimized.set(False)
                self.auto_optimize.set(False)
                self.theme.set('dark')
                self.language.set('en')
                
                self.cpu_aggressive.set(False)
                self.cpu_priority.set('normal')
                self.mem_aggressive.set(False)
                self.mem_threshold.set(80)
                
                self.custom_dns.set(False)
                self.dns_primary.set('8.8.8.8')
                self.dns_secondary.set('8.8.4.4')
                self.tcp_optimization.set(True)
                self.udp_optimization.set(True)
                self.qos_enabled.set(True)
                
                self.auto_detect_games.set(True)
                self.game_mode.set(True)
                self.anti_cheat_optimization.set(True)
                self.gaming_priority.set('high')
                self.fps_boost.set(True)
                self.latency_optimization.set(True)
                
                self.monitoring_enabled.set(True)
                self.monitoring_interval.set(5)
                self.alerts_enabled.set(True)
                self.cpu_threshold.set(80)
                self.memory_threshold.set(85)
                self.temperature_threshold.set(75)
                
                self.ai_enabled.set(True)
                self.predictive_optimization.set(True)
                self.adaptive_learning.set(True)
                self.debug_mode.set(False)
                self.verbose_logging.set(False)
                self.performance_logging.set(False)
                
                messagebox.showinfo("Reset", "Settings reset to defaults!")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to reset settings: {str(e)}")
