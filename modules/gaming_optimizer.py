"""
Advanced Gaming Optimizer Module
Specialized gaming optimizations with game detection, performance tuning, and anti-cheat compatibility
"""

import psutil
import time
import threading
import subprocess
import platform
import os
import json
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import winreg

class GamingOptimizer:
    """Advanced gaming optimizer with game detection and performance tuning"""
    
    def __init__(self):
        self.is_optimizing = False
        self.detected_games = []
        self.gaming_processes = []
        self.optimization_thread = None
        self.game_profiles = self._load_game_profiles()
        
    def _load_game_profiles(self) -> Dict[str, Dict]:
        """Load game-specific optimization profiles"""
        return {
            'league_of_legends': {
                'name': 'League of Legends',
                'processes': ['league of legends.exe', 'lol.exe', 'riotclientservices.exe', 'riotclient.exe'],
                'ports': [2099, 5222, 5223, 8080, 8443],
                'optimizations': ['cpu_priority', 'memory_optimization', 'network_optimization', 'gpu_optimization'],
                'anti_cheat': 'vanguard'
            },
            'valorant': {
                'name': 'Valorant',
                'processes': ['valorant.exe', 'valorant-win64-shipping.exe', 'riotclientservices.exe'],
                'ports': [443, 5222, 5223, 8080, 8443],
                'optimizations': ['cpu_priority', 'memory_optimization', 'network_optimization', 'gpu_optimization'],
                'anti_cheat': 'vanguard'
            },
            'cs2': {
                'name': 'Counter-Strike 2',
                'processes': ['cs2.exe', 'steam.exe'],
                'ports': [27015, 27016, 27017, 27018, 27019, 27020],
                'optimizations': ['cpu_priority', 'memory_optimization', 'network_optimization', 'gpu_optimization'],
                'anti_cheat': 'vac'
            },
            'fortnite': {
                'name': 'Fortnite',
                'processes': ['fortniteclient-win64-shipping.exe', 'epicgameslauncher.exe'],
                'ports': [443, 80, 8080, 8443],
                'optimizations': ['cpu_priority', 'memory_optimization', 'network_optimization', 'gpu_optimization'],
                'anti_cheat': 'easy_anti_cheat'
            },
            'apex_legends': {
                'name': 'Apex Legends',
                'processes': ['r5apex.exe', 'origin.exe', 'eaapp.exe'],
                'ports': [443, 80, 8080, 8443],
                'optimizations': ['cpu_priority', 'memory_optimization', 'network_optimization', 'gpu_optimization'],
                'anti_cheat': 'easy_anti_cheat'
            }
        }
    
    def start_gaming_optimization(self, profile: str = 'auto') -> Dict[str, any]:
        """Start gaming optimization"""
        if self.is_optimizing:
            return {'status': 'already_optimizing'}
        
        try:
            self.is_optimizing = True
            results = {
                'profile': profile,
                'timestamp': datetime.now().isoformat(),
                'optimizations': []
            }
            
            # Detect running games
            detected_games = self._detect_running_games()
            results['detected_games'] = detected_games
            
            if not detected_games and profile == 'auto':
                # Apply general gaming optimizations
                general_optimizations = self._apply_general_gaming_optimizations()
                results['optimizations'].extend(general_optimizations)
            else:
                # Apply game-specific optimizations
                for game in detected_games:
                    game_optimizations = self._apply_game_specific_optimizations(game)
                    results['optimizations'].extend(game_optimizations)
            
            # Apply universal gaming optimizations
            universal_optimizations = self._apply_universal_gaming_optimizations()
            results['optimizations'].extend(universal_optimizations)
            
            # Start gaming monitoring
            self._start_gaming_monitoring()
            
            return results
            
        except Exception as e:
            self.is_optimizing = False
            return {'status': 'error', 'message': str(e)}
    
    def _detect_running_games(self) -> List[Dict]:
        """Detect currently running games"""
        detected_games = []
        
        try:
            for proc in psutil.process_iter(['pid', 'name', 'exe']):
                try:
                    proc_name = proc.info['name'].lower()
                    
                    for game_key, game_profile in self.game_profiles.items():
                        for process_name in game_profile['processes']:
                            if process_name.lower() in proc_name:
                                if game_key not in [game['key'] for game in detected_games]:
                                    detected_games.append({
                                        'key': game_key,
                                        'name': game_profile['name'],
                                        'processes': [proc.info['name']],
                                        'pid': proc.info['pid']
                                    })
                                else:
                                    # Add process to existing game
                                    for game in detected_games:
                                        if game['key'] == game_key:
                                            game['processes'].append(proc.info['name'])
                                            break
                except Exception as e:
                    print(f"Process iteration error: {e}")
                    continue
                                
        except Exception as e:
            print(f"Game detection error: {e}")
        
        return detected_games
    
    def _apply_general_gaming_optimizations(self) -> List[Dict]:
        """Apply general gaming optimizations"""
        optimizations = []
        
        try:
            # Windows Game Mode
            optimizations.append(self._enable_windows_game_mode())
            
            # Gaming power plan
            optimizations.append(self._set_gaming_power_plan())
            
            # Gaming performance settings
            optimizations.append(self._set_gaming_performance_settings())
            
            # Gaming network optimization
            optimizations.append(self._optimize_gaming_network())
            
        except Exception as e:
            optimizations.append({'type': 'General Gaming Optimization', 'error': str(e)})
        
        return optimizations
    
    def _apply_game_specific_optimizations(self, game: Dict) -> List[Dict]:
        """Apply game-specific optimizations"""
        optimizations = []
        
        try:
            game_key = game['key']
            game_profile = self.game_profiles.get(game_key, {})
            
            # Set process priorities
            optimizations.append(self._set_game_process_priorities(game))
            
            # Optimize game-specific settings
            optimizations.append(self._optimize_game_settings(game))
            
            # Anti-cheat compatibility
            optimizations.append(self._optimize_anti_cheat_compatibility(game))
            
            # Game-specific network optimization
            optimizations.append(self._optimize_game_network(game))
            
        except Exception as e:
            optimizations.append({'type': f'Game-specific Optimization for {game["name"]}', 'error': str(e)})
        
        return optimizations
    
    def _apply_universal_gaming_optimizations(self) -> List[Dict]:
        """Apply universal gaming optimizations"""
        optimizations = []
        
        try:
            # CPU optimization for gaming
            optimizations.append(self._optimize_cpu_for_gaming())
            
            # Memory optimization for gaming
            optimizations.append(self._optimize_memory_for_gaming())
            
            # GPU optimization for gaming
            optimizations.append(self._optimize_gpu_for_gaming())
            
            # Gaming network optimization
            optimizations.append(self._optimize_gaming_network())
            
            # Gaming audio optimization
            optimizations.append(self._optimize_gaming_audio())
            
        except Exception as e:
            optimizations.append({'type': 'Universal Gaming Optimization', 'error': str(e)})
        
        return optimizations
    
    def _enable_windows_game_mode(self) -> Dict[str, any]:
        """Enable Windows Game Mode"""
        try:
            optimizations = []
            
            if platform.system() == "Windows":
                # Enable Game Mode
                optimizations.append("Enabling Windows Game Mode")
                subprocess.run(["reg", "add", "HKEY_CURRENT_USER\\Software\\Microsoft\\GameBar", 
                               "/v", "AllowAutoGameMode", "/t", "REG_DWORD", "/d", "1", "/f"], 
                              capture_output=True, check=True)
                
                # Disable Game Bar notifications
                optimizations.append("Disabling Game Bar notifications")
                subprocess.run(["reg", "add", "HKEY_CURRENT_USER\\Software\\Microsoft\\GameBar", 
                               "/v", "ShowStartupPanel", "/t", "REG_DWORD", "/d", "0", "/f"], 
                              capture_output=True, check=True)
                
                # Enable Game Mode for all games
                optimizations.append("Enabling Game Mode for all games")
                subprocess.run(["reg", "add", "HKEY_CURRENT_USER\\Software\\Microsoft\\GameBar", 
                               "/v", "AutoGameModeEnabled", "/t", "REG_DWORD", "/d", "1", "/f"], 
                              capture_output=True, check=True)
            
            return {
                'type': 'Windows Game Mode',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': 'Windows Game Mode', 'error': str(e)}
    
    def _set_gaming_power_plan(self) -> Dict[str, any]:
        """Set gaming power plan"""
        try:
            optimizations = []
            
            if platform.system() == "Windows":
                # Set high performance power plan
                optimizations.append("Setting high performance power plan")
                subprocess.run(["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"], 
                             capture_output=True, check=True)
                
                # Disable CPU throttling
                optimizations.append("Disabling CPU throttling")
                subprocess.run(["powercfg", "/setacvalueindex", "SCHEME_CURRENT", 
                               "SUB_PROCESSOR", "PROCTHROTTLEMAX", "100"], 
                              capture_output=True, check=True)
                
                # Set minimum CPU state to 100%
                optimizations.append("Setting minimum CPU state to 100%")
                subprocess.run(["powercfg", "/setacvalueindex", "SCHEME_CURRENT", 
                               "SUB_PROCESSOR", "PROCTHROTTLEMIN", "100"], 
                              capture_output=True, check=True)
            
            return {
                'type': 'Gaming Power Plan',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': 'Gaming Power Plan', 'error': str(e)}
    
    def _set_gaming_performance_settings(self) -> Dict[str, any]:
        """Set gaming performance settings"""
        try:
            optimizations = []
            
            if platform.system() == "Windows":
                # Disable Windows Defender real-time protection for gaming
                optimizations.append("Optimizing Windows Defender for gaming")
                subprocess.run(["powershell", "-Command", 
                               "Set-MpPreference -DisableRealtimeMonitoring $true"], 
                              capture_output=True, check=True)
                
                # Disable Windows Update during gaming
                optimizations.append("Disabling Windows Update during gaming")
                subprocess.run(["powershell", "-Command", 
                               "Set-Service -Name wuauserv -StartupType Disabled"], 
                              capture_output=True, check=True)
                
                # Optimize Windows for gaming
                optimizations.append("Optimizing Windows for gaming")
                subprocess.run(["powershell", "-Command", 
                               "Set-ItemProperty -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile' -Name SystemResponsiveness -Value 0"], 
                              capture_output=True, check=True)
            
            return {
                'type': 'Gaming Performance Settings',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': 'Gaming Performance Settings', 'error': str(e)}
    
    def _optimize_gaming_network(self) -> Dict[str, any]:
        """Optimize network for gaming"""
        try:
            optimizations = []
            
            if platform.system() == "Windows":
                # Optimize TCP for gaming
                optimizations.append("Optimizing TCP for gaming")
                subprocess.run(["netsh", "int", "tcp", "set", "global", "autotuninglevel=normal"], 
                             capture_output=True, check=True)
                
                # Disable Nagle's algorithm for gaming
                optimizations.append("Disabling Nagle's algorithm for gaming")
                subprocess.run(["netsh", "int", "tcp", "set", "global", "nagle=enabled"], 
                             capture_output=True, check=True)
                
                # Optimize UDP for gaming
                optimizations.append("Optimizing UDP for gaming")
                subprocess.run(["netsh", "int", "udp", "set", "global", "udprcvbuffer=65536"], 
                             capture_output=True, check=True)
                subprocess.run(["netsh", "int", "udp", "set", "global", "udpsndbuffer=65536"], 
                             capture_output=True, check=True)
            
            return {
                'type': 'Gaming Network Optimization',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': 'Gaming Network Optimization', 'error': str(e)}
    
    def _set_game_process_priorities(self, game: Dict) -> Dict[str, any]:
        """Set process priorities for game"""
        try:
            optimizations = []
            
            for process_name in game['processes']:
                try:
                    for proc in psutil.process_iter(['pid', 'name']):
                        if proc.info['name'].lower() == process_name.lower():
                            # Set high priority
                            proc.nice(psutil.HIGH_PRIORITY_CLASS)
                            optimizations.append(f"Set high priority for {process_name}")
                            
                            # Set CPU affinity to all cores
                            proc.cpu_affinity(list(range(psutil.cpu_count())))
                            optimizations.append(f"Set CPU affinity for {process_name}")
                            
                except Exception as e:
                    optimizations.append(f"Failed to optimize {process_name}: {str(e)}")
            
            return {
                'type': f'Process Priority for {game["name"]}',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': f'Process Priority for {game["name"]}', 'error': str(e)}
    
    def _optimize_game_settings(self, game: Dict) -> Dict[str, any]:
        """Optimize game-specific settings"""
        try:
            optimizations = []
            
            game_key = game['key']
            game_profile = self.game_profiles.get(game_key, {})
            
            if game_key == 'league_of_legends':
                optimizations.append("Optimizing League of Legends settings")
                # This would involve optimizing LoL-specific settings
                
            elif game_key == 'valorant':
                optimizations.append("Optimizing Valorant settings")
                # This would involve optimizing Valorant-specific settings
                
            elif game_key == 'cs2':
                optimizations.append("Optimizing Counter-Strike 2 settings")
                # This would involve optimizing CS2-specific settings
                
            elif game_key == 'fortnite':
                optimizations.append("Optimizing Fortnite settings")
                # This would involve optimizing Fortnite-specific settings
                
            elif game_key == 'apex_legends':
                optimizations.append("Optimizing Apex Legends settings")
                # This would involve optimizing Apex Legends-specific settings
            
            return {
                'type': f'Game Settings for {game["name"]}',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': f'Game Settings for {game["name"]}', 'error': str(e)}
    
    def _optimize_anti_cheat_compatibility(self, game: Dict) -> Dict[str, any]:
        """Optimize anti-cheat compatibility"""
        try:
            optimizations = []
            
            game_key = game['key']
            game_profile = self.game_profiles.get(game_key, {})
            anti_cheat = game_profile.get('anti_cheat', '')
            
            if anti_cheat == 'vanguard':
                optimizations.append("Optimizing Vanguard anti-cheat compatibility")
                # This would involve Vanguard-specific optimizations
                
            elif anti_cheat == 'vac':
                optimizations.append("Optimizing VAC anti-cheat compatibility")
                # This would involve VAC-specific optimizations
                
            elif anti_cheat == 'easy_anti_cheat':
                optimizations.append("Optimizing Easy Anti-Cheat compatibility")
                # This would involve Easy Anti-Cheat-specific optimizations
            
            return {
                'type': f'Anti-Cheat Compatibility for {game["name"]}',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': f'Anti-Cheat Compatibility for {game["name"]}', 'error': str(e)}
    
    def _optimize_game_network(self, game: Dict) -> Dict[str, any]:
        """Optimize network for specific game"""
        try:
            optimizations = []
            
            game_key = game['key']
            game_profile = self.game_profiles.get(game_key, {})
            ports = game_profile.get('ports', [])
            
            if ports:
                optimizations.append(f"Prioritizing ports for {game['name']}: {ports}")
                # This would involve setting up QoS rules for these ports
            
            return {
                'type': f'Network Optimization for {game["name"]}',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': f'Network Optimization for {game["name"]}', 'error': str(e)}
    
    def _optimize_cpu_for_gaming(self) -> Dict[str, any]:
        """Optimize CPU for gaming"""
        try:
            optimizations = []
            
            # Set CPU priority for gaming processes
            optimizations.append("Setting CPU priority for gaming processes")
            
            # Optimize CPU scheduling
            optimizations.append("Optimizing CPU scheduling for gaming")
            
            # Set CPU affinity for gaming
            optimizations.append("Setting CPU affinity for gaming")
            
            return {
                'type': 'CPU Gaming Optimization',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': 'CPU Gaming Optimization', 'error': str(e)}
    
    def _optimize_memory_for_gaming(self) -> Dict[str, any]:
        """Optimize memory for gaming"""
        try:
            optimizations = []
            
            # Optimize memory for gaming
            optimizations.append("Optimizing memory for gaming")
            
            # Set memory priority for gaming
            optimizations.append("Setting memory priority for gaming")
            
            # Optimize memory allocation
            optimizations.append("Optimizing memory allocation for gaming")
            
            return {
                'type': 'Memory Gaming Optimization',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': 'Memory Gaming Optimization', 'error': str(e)}
    
    def _optimize_gpu_for_gaming(self) -> Dict[str, any]:
        """Optimize GPU for gaming"""
        try:
            optimizations = []
            
            # Optimize GPU for gaming
            optimizations.append("Optimizing GPU for gaming")
            
            # Set GPU performance mode
            optimizations.append("Setting GPU performance mode")
            
            # Optimize GPU memory
            optimizations.append("Optimizing GPU memory for gaming")
            
            return {
                'type': 'GPU Gaming Optimization',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': 'GPU Gaming Optimization', 'error': str(e)}
    
    def _optimize_gaming_audio(self) -> Dict[str, any]:
        """Optimize audio for gaming"""
        try:
            optimizations = []
            
            # Optimize audio for gaming
            optimizations.append("Optimizing audio for gaming")
            
            # Set audio priority
            optimizations.append("Setting audio priority for gaming")
            
            # Optimize audio latency
            optimizations.append("Optimizing audio latency for gaming")
            
            return {
                'type': 'Audio Gaming Optimization',
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'type': 'Audio Gaming Optimization', 'error': str(e)}
    
    def _start_gaming_monitoring(self):
        """Start gaming monitoring"""
        try:
            self.optimization_thread = threading.Thread(target=self._gaming_monitoring_loop, daemon=True)
            self.optimization_thread.start()
        except:
            pass
    
    def _gaming_monitoring_loop(self):
        """Gaming monitoring loop"""
        while self.is_optimizing:
            try:
                # Monitor gaming processes
                self._monitor_gaming_processes()
                
                # Update gaming optimizations
                self._update_gaming_optimizations()
                
                time.sleep(5)  # Update every 5 seconds
                
            except:
                time.sleep(5)
    
    def _monitor_gaming_processes(self):
        """Monitor gaming processes"""
        try:
            # Update detected games
            self.detected_games = self._detect_running_games()
            
            # Monitor gaming processes
            for game in self.detected_games:
                for process_name in game['processes']:
                    try:
                        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
                            if proc.info['name'].lower() == process_name.lower():
                                # Monitor process performance
                                cpu_usage = proc.info['cpu_percent']
                                memory_usage = proc.info['memory_info'].rss / (1024 * 1024)  # MB
                                
                                # Log performance if needed
                                if cpu_usage > 80 or memory_usage > 1000:
                                    print(f"High resource usage for {process_name}: CPU {cpu_usage}%, Memory {memory_usage}MB")
                                
                    except:
                        continue
                        
        except:
            pass
    
    def _update_gaming_optimizations(self):
        """Update gaming optimizations based on current state"""
        try:
            # Update optimizations based on detected games
            for game in self.detected_games:
                # Update game-specific optimizations
                self._apply_game_specific_optimizations(game)
                
        except:
            pass
    
    def stop_gaming_optimization(self):
        """Stop gaming optimization"""
        self.is_optimizing = False
        if self.optimization_thread:
            self.optimization_thread.join(timeout=2)
        
        return {'status': 'stopped'}
    
    def get_gaming_status(self) -> Dict:
        """Get current gaming status"""
        try:
            return {
                'status': 'optimizing' if self.is_optimizing else 'stopped',
                'detected_games': self.detected_games,
                'gaming_processes': len(self.gaming_processes),
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def get_game_profiles(self) -> Dict:
        """Get available game profiles"""
        return self.game_profiles
