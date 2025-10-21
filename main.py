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

# Import our modules
from modules.fps_boost import FPSBoost
from modules.network_analyzer import NetworkAnalyzer
from modules.multi_internet import MultiInternet
from modules.traffic_shaper import TrafficShaper
from modules.ram_cleaner import RAMCleaner
from modules.lol_optimizer import LoLOptimizer
from modules.config_manager import ConfigManager

class NetworkOptimizerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NGXSMK GameNet Optimizer")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1e1e1e')
        
        # Initialize modules
        self.config_manager = ConfigManager()
        self.fps_boost = FPSBoost()
        self.network_analyzer = NetworkAnalyzer()
        self.multi_internet = MultiInternet()
        self.traffic_shaper = TrafficShaper()
        self.ram_cleaner = RAMCleaner()
        self.lol_optimizer = LoLOptimizer()
        
        # Status variables
        self.is_optimizing = False
        
        self.setup_ui()
        self.load_settings()
        
    def setup_ui(self):
        """Setup the main user interface"""
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background='#2d2d2d', borderwidth=0)
        style.configure('TNotebook.Tab', background='#3d3d3d', foreground='white', padding=[20, 10])
        style.map('TNotebook.Tab', background=[('selected', '#4d4d4d')])
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#1e1e1e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        header_frame = tk.Frame(main_frame, bg='#1e1e1e')
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(header_frame, text="NGXSMK GameNet Optimizer", 
                              font=('Arial', 24, 'bold'), fg='#00ff88', bg='#1e1e1e')
        title_label.pack(side=tk.LEFT)
        
        status_label = tk.Label(header_frame, text="Ready", 
                              font=('Arial', 12), fg='#888888', bg='#1e1e1e')
        status_label.pack(side=tk.RIGHT)
        self.status_label = status_label
        
        # Control buttons
        control_frame = tk.Frame(main_frame, bg='#1e1e1e')
        control_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.optimize_btn = tk.Button(control_frame, text="Start Optimization", 
                                    command=self.toggle_optimization,
                                    bg='#00ff88', fg='black', font=('Arial', 12, 'bold'),
                                    padx=20, pady=10, relief=tk.FLAT)
        self.optimize_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        settings_btn = tk.Button(control_frame, text="Settings", 
                               command=self.open_settings,
                               bg='#4d4d4d', fg='white', font=('Arial', 12),
                               padx=20, pady=10, relief=tk.FLAT)
        settings_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Main notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_fps_boost_tab()
        self.create_network_analyzer_tab()
        self.create_multi_internet_tab()
        self.create_traffic_shaper_tab()
        self.create_ram_cleaner_tab()
        self.create_lol_optimizer_tab()
        
    def create_fps_boost_tab(self):
        """Create FPS Boost tab"""
        fps_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(fps_frame, text="FPS Boost")
        
        # FPS Boost content
        fps_title = tk.Label(fps_frame, text="FPS Boost & Game Optimization", 
                            font=('Arial', 16, 'bold'), fg='#00ff88', bg='#1e1e1e')
        fps_title.pack(pady=20)
        
        # Game selection
        game_frame = tk.Frame(fps_frame, bg='#1e1e1e')
        game_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(game_frame, text="Select Game:", font=('Arial', 12), 
                fg='white', bg='#1e1e1e').pack(side=tk.LEFT)
        
        self.game_var = tk.StringVar(value="Auto-detect")
        game_combo = ttk.Combobox(game_frame, textvariable=self.game_var, 
                                 values=["Auto-detect", "Valorant", "CS2", "Fortnite", "Apex Legends", "Call of Duty", "League of Legends"])
        game_combo.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)
        
        # Optimization options
        options_frame = tk.Frame(fps_frame, bg='#1e1e1e')
        options_frame.pack(fill=tk.X, padx=20, pady=20)
        
        self.priority_boost = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="High Priority Process", variable=self.priority_boost,
                      fg='white', bg='#1e1e1e', selectcolor='#00ff88').pack(anchor=tk.W)
        
        self.cpu_optimization = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="CPU Optimization", variable=self.cpu_optimization,
                      fg='white', bg='#1e1e1e', selectcolor='#00ff88').pack(anchor=tk.W)
        
        self.gpu_optimization = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="GPU Optimization", variable=self.gpu_optimization,
                      fg='white', bg='#1e1e1e', selectcolor='#00ff88').pack(anchor=tk.W)
        
        # Status display
        status_frame = tk.Frame(fps_frame, bg='#2d2d2d', relief=tk.RAISED, bd=1)
        status_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(status_frame, text="Optimization Status:", font=('Arial', 12, 'bold'),
                fg='white', bg='#2d2d2d').pack(anchor=tk.W, padx=10, pady=5)
        
        self.fps_status = tk.Text(status_frame, height=8, bg='#1e1e1e', fg='#00ff88',
                                 font=('Consolas', 10), state=tk.DISABLED)
        self.fps_status.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
    def create_network_analyzer_tab(self):
        """Create Network Analyzer tab"""
        net_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(net_frame, text="Network Analyzer")
        
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
        """Create Multi Internet tab"""
        multi_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(multi_frame, text="Multi Internet")
        
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
        """Create Traffic Shaper tab"""
        traffic_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(traffic_frame, text="Traffic Shaper")
        
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
        """Create RAM Cleaner tab"""
        ram_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(ram_frame, text="RAM Cleaner")
        
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
        """Create League of Legends Optimizer tab"""
        lol_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(lol_frame, text="LoL Optimizer")
        
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
        
    def toggle_optimization(self):
        """Toggle optimization on/off"""
        if not self.is_optimizing:
            self.start_optimization()
        else:
            self.stop_optimization()
            
    def start_optimization(self):
        """Start all optimization modules"""
        self.is_optimizing = True
        self.optimize_btn.config(text="Stop Optimization", bg='#ff4444')
        self.status_label.config(text="Optimizing...", fg='#00ff88')
        
        # Start optimization in separate thread
        threading.Thread(target=self.run_optimization, daemon=True).start()
        
    def stop_optimization(self):
        """Stop all optimization modules"""
        self.is_optimizing = False
        self.optimize_btn.config(text="Start Optimization", bg='#00ff88')
        self.status_label.config(text="Ready", fg='#888888')
        
    def run_optimization(self):
        """Run optimization modules"""
        try:
            # FPS Boost
            if self.priority_boost.get() or self.cpu_optimization.get() or self.gpu_optimization.get():
                self.fps_boost.optimize_game_performance(
                    priority_boost=self.priority_boost.get(),
                    cpu_optimization=self.cpu_optimization.get(),
                    gpu_optimization=self.gpu_optimization.get()
                )
                
            # RAM Cleaner
            if self.auto_clean.get():
                self.ram_cleaner.clean_memory()
                
            # Traffic Shaper
            if self.prioritize_gaming.get() or self.limit_background.get():
                self.traffic_shaper.optimize_traffic(
                    prioritize_gaming=self.prioritize_gaming.get(),
                    limit_background=self.limit_background.get()
                )
                
        except Exception as e:
            messagebox.showerror("Error", f"Optimization failed: {str(e)}")
            
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
        """Run network analysis"""
        try:
            results = self.network_analyzer.analyze_network()
            self.network_results.config(state=tk.NORMAL)
            self.network_results.delete(1.0, tk.END)
            self.network_results.insert(tk.END, results)
            self.network_results.config(state=tk.DISABLED)
        except Exception as e:
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
            
    def run(self):
        """Run the application"""
        try:
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()
        except KeyboardInterrupt:
            self.on_closing()
            
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
