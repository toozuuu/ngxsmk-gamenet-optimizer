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
    
    def _initialize_variables(self):
        """Initialize all tkinter variables"""
        # General settings
        self.auto_start = tk.BooleanVar(value=self.settings.get('general', {}).get('auto_start', False))
        self.start_minimized = tk.BooleanVar(value=self.settings.get('general', {}).get('start_minimized', False))
        self.auto_optimize = tk.BooleanVar(value=self.settings.get('general', {}).get('auto_optimize', False))
        self.theme = tk.StringVar(value=self.settings.get('general', {}).get('theme', 'dark'))
        self.language = tk.StringVar(value=self.settings.get('general', {}).get('language', 'en'))
        
        # Optimization settings
        self.cpu_aggressive = tk.BooleanVar(value=self.settings.get('optimization', {}).get('cpu_aggressive', False))
        self.cpu_priority = tk.StringVar(value=self.settings.get('optimization', {}).get('cpu_priority', 'high'))
        self.mem_aggressive = tk.BooleanVar(value=self.settings.get('optimization', {}).get('mem_aggressive', False))
        self.mem_threshold = tk.IntVar(value=self.settings.get('optimization', {}).get('mem_threshold', 80))
        
        # Network settings
        self.custom_dns = tk.BooleanVar(value=self.settings.get('network', {}).get('custom_dns', False))
        self.dns_primary = tk.StringVar(value=self.settings.get('network', {}).get('dns_primary', '8.8.8.8'))
        self.dns_secondary = tk.StringVar(value=self.settings.get('network', {}).get('dns_secondary', '1.1.1.1'))
        self.tcp_optimization = tk.BooleanVar(value=self.settings.get('network', {}).get('tcp_optimization', True))
        self.udp_optimization = tk.BooleanVar(value=self.settings.get('network', {}).get('udp_optimization', True))
        self.qos_enabled = tk.BooleanVar(value=self.settings.get('network', {}).get('qos_enabled', False))
        
        # Gaming settings
        self.auto_detect_games = tk.BooleanVar(value=self.settings.get('gaming', {}).get('auto_detect_games', True))
        self.game_mode = tk.BooleanVar(value=self.settings.get('gaming', {}).get('game_mode', True))
        self.anti_cheat_optimization = tk.BooleanVar(value=self.settings.get('gaming', {}).get('anti_cheat_optimization', True))
        self.gaming_priority = tk.StringVar(value=self.settings.get('gaming', {}).get('gaming_priority', 'high'))
        self.fps_boost = tk.BooleanVar(value=self.settings.get('gaming', {}).get('fps_boost', True))
        self.latency_optimization = tk.BooleanVar(value=self.settings.get('gaming', {}).get('latency_optimization', True))
        
        # Monitoring settings
        self.monitoring_enabled = tk.BooleanVar(value=self.settings.get('monitoring', {}).get('monitoring_enabled', True))
        self.monitoring_interval = tk.IntVar(value=self.settings.get('monitoring', {}).get('monitoring_interval', 5))
        self.alerts_enabled = tk.BooleanVar(value=self.settings.get('monitoring', {}).get('alerts_enabled', True))
        self.cpu_threshold = tk.IntVar(value=self.settings.get('monitoring', {}).get('cpu_threshold', 80))
        self.memory_threshold = tk.IntVar(value=self.settings.get('monitoring', {}).get('memory_threshold', 80))
        self.temperature_threshold = tk.IntVar(value=self.settings.get('monitoring', {}).get('temperature_threshold', 80))
        
        # Advanced settings
        self.ai_enabled = tk.BooleanVar(value=self.settings.get('advanced', {}).get('ai_enabled', False))
        self.predictive_optimization = tk.BooleanVar(value=self.settings.get('advanced', {}).get('predictive_optimization', False))
        self.adaptive_learning = tk.BooleanVar(value=self.settings.get('advanced', {}).get('adaptive_learning', False))
        self.debug_mode = tk.BooleanVar(value=self.settings.get('advanced', {}).get('debug_mode', False))
        self.verbose_logging = tk.BooleanVar(value=self.settings.get('advanced', {}).get('verbose_logging', False))
        self.performance_logging = tk.BooleanVar(value=self.settings.get('advanced', {}).get('performance_logging', False))
        
    def create_settings_notebook(self):
        """Create settings notebook with different categories"""
        # Main frame
        main_frame = tk.Frame(self.dialog, bg='#1e1e1e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Initialize all variables
        self._initialize_variables()
        
        # Notebook for settings categories
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create different setting tabs
        self.create_general_settings()
        self.create_optimization_settings()
        self.create_network_settings()
        self.create_gaming_settings()
        self.create_monitoring_settings()
        self.create_advanced_settings()
    
    def create_general_settings(self):
        """Create general settings tab"""
        general_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(general_frame, text="🔧 General")
        
        # Auto-start settings
        auto_frame = tk.LabelFrame(general_frame, text="Auto-Start Settings:", 
                                  font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                  relief=tk.RAISED, bd=2)
        auto_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(auto_frame, text="Start with Windows", variable=self.auto_start,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(auto_frame, text="Start minimized", variable=self.start_minimized,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(auto_frame, text="Auto-optimize on startup", variable=self.auto_optimize,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        # UI settings
        ui_frame = tk.LabelFrame(general_frame, text="UI Settings:", 
                                font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                relief=tk.RAISED, bd=2)
        ui_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Theme selection
        theme_frame = tk.Frame(ui_frame, bg='#2d2d2d')
        theme_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(theme_frame, text="Theme:", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        tk.Radiobutton(theme_frame, text="Dark", variable=self.theme, value="dark",
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(theme_frame, text="Light", variable=self.theme, value="light",
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(theme_frame, text="Gaming", variable=self.theme, value="gaming",
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(side=tk.LEFT, padx=10)
        
        # Language selection
        lang_frame = tk.Frame(ui_frame, bg='#2d2d2d')
        lang_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(lang_frame, text="Language:", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        lang_combo = ttk.Combobox(lang_frame, textvariable=self.language, 
                                 values=['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'zh', 'ja', 'ko'],
                                 state='readonly', width=10)
        lang_combo.pack(side=tk.LEFT, padx=10)
    
    def create_optimization_settings(self):
        """Create optimization settings tab"""
        opt_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(opt_frame, text="⚡ Optimization")
        
        # CPU settings
        cpu_frame = tk.LabelFrame(opt_frame, text="CPU Optimization:", 
                                 font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                 relief=tk.RAISED, bd=2)
        cpu_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(cpu_frame, text="Aggressive CPU optimization", variable=self.cpu_aggressive,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        # CPU Priority
        priority_frame = tk.Frame(cpu_frame, bg='#2d2d2d')
        priority_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(priority_frame, text="CPU Priority:", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        tk.Radiobutton(priority_frame, text="High", variable=self.cpu_priority, value="high",
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(priority_frame, text="Normal", variable=self.cpu_priority, value="normal",
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(priority_frame, text="Low", variable=self.cpu_priority, value="low",
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(side=tk.LEFT, padx=10)
        
        # Memory settings
        mem_frame = tk.LabelFrame(opt_frame, text="Memory Optimization:", 
                                 font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                 relief=tk.RAISED, bd=2)
        mem_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(mem_frame, text="Aggressive memory cleanup", variable=self.mem_aggressive,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        # Memory threshold
        threshold_frame = tk.Frame(mem_frame, bg='#2d2d2d')
        threshold_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(threshold_frame, text="Memory threshold (%):", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        threshold_scale = tk.Scale(threshold_frame, from_=50, to=95, orient=tk.HORIZONTAL,
                                  variable=self.mem_threshold, bg='#2d2d2d', fg='white',
                                  highlightbackground='#2d2d2d', troughcolor='#404040')
        threshold_scale.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
    
    def create_network_settings(self):
        """Create network settings tab"""
        net_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(net_frame, text="🌐 Network")
        
        # DNS settings
        dns_frame = tk.LabelFrame(net_frame, text="DNS Settings:", 
                                 font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                 relief=tk.RAISED, bd=2)
        dns_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(dns_frame, text="Use custom DNS servers", variable=self.custom_dns,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        # DNS servers
        dns_servers_frame = tk.Frame(dns_frame, bg='#2d2d2d')
        dns_servers_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(dns_servers_frame, text="Primary DNS:", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        tk.Entry(dns_servers_frame, textvariable=self.dns_primary, font=('Arial', 11),
                bg='#404040', fg='white', insertbackground='white').pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        tk.Label(dns_servers_frame, text="Secondary DNS:", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT, padx=10)
        
        tk.Entry(dns_servers_frame, textvariable=self.dns_secondary, font=('Arial', 11),
                bg='#404040', fg='white', insertbackground='white').pack(side=tk.LEFT, padx=10)
        
        # Network optimization
        net_opt_frame = tk.LabelFrame(net_frame, text="Network Optimization:", 
                                     font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                     relief=tk.RAISED, bd=2)
        net_opt_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(net_opt_frame, text="TCP optimization", variable=self.tcp_optimization,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(net_opt_frame, text="UDP optimization", variable=self.udp_optimization,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(net_opt_frame, text="Enable QoS", variable=self.qos_enabled,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
    
    def create_gaming_settings(self):
        """Create gaming settings tab"""
        gaming_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(gaming_frame, text="🎮 Gaming")
        
        # Game detection
        detection_frame = tk.LabelFrame(gaming_frame, text="Game Detection:", 
                                      font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                      relief=tk.RAISED, bd=2)
        detection_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(detection_frame, text="Auto-detect games", variable=self.auto_detect_games,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        # Gaming optimization
        gaming_opt_frame = tk.LabelFrame(gaming_frame, text="Gaming Optimization:", 
                                       font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                       relief=tk.RAISED, bd=2)
        gaming_opt_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(gaming_opt_frame, text="Enable Game Mode", variable=self.game_mode,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(gaming_opt_frame, text="Anti-cheat optimization", variable=self.anti_cheat_optimization,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(gaming_opt_frame, text="FPS Boost", variable=self.fps_boost,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(gaming_opt_frame, text="Latency optimization", variable=self.latency_optimization,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        # Gaming priority
        priority_frame = tk.Frame(gaming_opt_frame, bg='#2d2d2d')
        priority_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(priority_frame, text="Gaming Priority:", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        tk.Radiobutton(priority_frame, text="High", variable=self.gaming_priority, value="high",
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(priority_frame, text="Normal", variable=self.gaming_priority, value="normal",
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(priority_frame, text="Low", variable=self.gaming_priority, value="low",
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(side=tk.LEFT, padx=10)
    
    def create_monitoring_settings(self):
        """Create monitoring settings tab"""
        monitor_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(monitor_frame, text="📊 Monitoring")
        
        # Monitoring settings
        monitor_opt_frame = tk.LabelFrame(monitor_frame, text="Monitoring Settings:", 
                                        font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                        relief=tk.RAISED, bd=2)
        monitor_opt_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(monitor_opt_frame, text="Enable monitoring", variable=self.monitoring_enabled,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(monitor_opt_frame, text="Enable alerts", variable=self.alerts_enabled,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        # Monitoring interval
        interval_frame = tk.Frame(monitor_opt_frame, bg='#2d2d2d')
        interval_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(interval_frame, text="Monitoring interval (seconds):", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        interval_scale = tk.Scale(interval_frame, from_=1, to=60, orient=tk.HORIZONTAL,
                                 variable=self.monitoring_interval, bg='#2d2d2d', fg='white',
                                 highlightbackground='#2d2d2d', troughcolor='#404040')
        interval_scale.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Thresholds
        threshold_frame = tk.LabelFrame(monitor_frame, text="Alert Thresholds:", 
                                      font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                      relief=tk.RAISED, bd=2)
        threshold_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # CPU threshold
        cpu_thresh_frame = tk.Frame(threshold_frame, bg='#2d2d2d')
        cpu_thresh_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(cpu_thresh_frame, text="CPU threshold (%):", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        cpu_scale = tk.Scale(cpu_thresh_frame, from_=50, to=100, orient=tk.HORIZONTAL,
                            variable=self.cpu_threshold, bg='#2d2d2d', fg='white',
                            highlightbackground='#2d2d2d', troughcolor='#404040')
        cpu_scale.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Memory threshold
        mem_thresh_frame = tk.Frame(threshold_frame, bg='#2d2d2d')
        mem_thresh_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(mem_thresh_frame, text="Memory threshold (%):", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        mem_scale = tk.Scale(mem_thresh_frame, from_=50, to=100, orient=tk.HORIZONTAL,
                            variable=self.memory_threshold, bg='#2d2d2d', fg='white',
                            highlightbackground='#2d2d2d', troughcolor='#404040')
        mem_scale.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Temperature threshold
        temp_thresh_frame = tk.Frame(threshold_frame, bg='#2d2d2d')
        temp_thresh_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(temp_thresh_frame, text="Temperature threshold (°C):", font=('Arial', 11, 'bold'), 
                fg='white', bg='#2d2d2d').pack(side=tk.LEFT)
        
        temp_scale = tk.Scale(temp_thresh_frame, from_=60, to=100, orient=tk.HORIZONTAL,
                             variable=self.temperature_threshold, bg='#2d2d2d', fg='white',
                             highlightbackground='#2d2d2d', troughcolor='#404040')
        temp_scale.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
    
    def create_advanced_settings(self):
        """Create advanced settings tab"""
        advanced_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(advanced_frame, text="🔬 Advanced")
        
        # AI settings
        ai_frame = tk.LabelFrame(advanced_frame, text="AI Features:", 
                                font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                relief=tk.RAISED, bd=2)
        ai_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(ai_frame, text="Enable AI optimization", variable=self.ai_enabled,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(ai_frame, text="Predictive optimization", variable=self.predictive_optimization,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(ai_frame, text="Adaptive learning", variable=self.adaptive_learning,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        # Debug settings
        debug_frame = tk.LabelFrame(advanced_frame, text="Debug Settings:", 
                                   font=('Arial', 12, 'bold'), fg='white', bg='#2d2d2d', 
                                   relief=tk.RAISED, bd=2)
        debug_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Checkbutton(debug_frame, text="Debug mode", variable=self.debug_mode,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(debug_frame, text="Verbose logging", variable=self.verbose_logging,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Checkbutton(debug_frame, text="Performance logging", variable=self.performance_logging,
                      font=('Arial', 11), fg='white', bg='#2d2d2d', selectcolor='#00ff88',
                      activebackground='#2d2d2d', activeforeground='white').pack(anchor=tk.W, padx=10, pady=5)
    
    def create_buttons(self):
        """Create dialog buttons"""
        button_frame = tk.Frame(self.dialog, bg='#1e1e1e')
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Save & Close button
        tk.Button(button_frame, text="Save & Close", command=self.save_and_close,
                 font=('Arial', 14, 'bold'), bg='#00ff88', fg='black',
                 relief=tk.RAISED, bd=3, padx=20, pady=5).pack(side=tk.RIGHT, padx=5)
        
        # Cancel button
        tk.Button(button_frame, text="Cancel", command=self.cancel_settings,
                 font=('Arial', 14, 'bold'), bg='#666666', fg='white',
                 relief=tk.RAISED, bd=3, padx=20, pady=5).pack(side=tk.RIGHT, padx=5)
        
        # Apply button
        tk.Button(button_frame, text="Apply", command=self.apply_settings,
                 font=('Arial', 14, 'bold'), bg='#0066cc', fg='white',
                 relief=tk.RAISED, bd=3, padx=20, pady=5).pack(side=tk.RIGHT, padx=5)
    
    def center_dialog(self):
        """Center the dialog on screen"""
        self.dialog.update_idletasks()
        width = self.dialog.winfo_width()
        height = self.dialog.winfo_height()
        x = (self.dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (height // 2)
        self.dialog.geometry(f'{width}x{height}+{x}+{y}')
    
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
    
    def save_and_close(self):
        """Save settings and close dialog"""
        try:
            # Apply settings first
            self.apply_settings()
            # Close dialog
            self.dialog.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {str(e)}")