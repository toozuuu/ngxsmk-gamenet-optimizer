"""
Configuration Manager Module
Handles application settings and configuration
"""

import json
import os
import time
from typing import Dict, Any, Optional
import threading

class ConfigManager:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config = {}
        self.lock = threading.Lock()
        self.load_settings()
    
    def load_settings(self) -> Dict[str, Any]:
        """Load settings from configuration file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                # Create default configuration
                self.config = self._get_default_config()
                self.save_settings(self.config)
        except Exception as e:
            print(f"Failed to load settings: {e}")
            self.config = self._get_default_config()
        
        return self.config
    
    def save_settings(self, settings: Dict[str, Any]) -> bool:
        """Save settings to configuration file"""
        try:
            with self.lock:
                self.config.update(settings)
                
                with open(self.config_file, 'w') as f:
                    json.dump(self.config, f, indent=2)
                
                return True
        except Exception as e:
            print(f"Failed to save settings: {e}")
            return False
    
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a specific setting value"""
        try:
            return self.config.get(key, default)
        except Exception:
            return default
    
    def set_setting(self, key: str, value: Any) -> bool:
        """Set a specific setting value"""
        try:
            with self.lock:
                self.config[key] = value
                return self.save_settings({})
        except Exception:
            return False
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            "version": "1.0.0",
            "last_updated": time.time(),
            "fps_boost": {
                "enabled": True,
                "priority_boost": True,
                "cpu_optimization": True,
                "gpu_optimization": True,
                "auto_detect_games": True,
                "target_fps": 144
            },
            "network_analyzer": {
                "enabled": True,
                "auto_analysis": False,
                "analysis_interval": 30,
                "test_servers": ["8.8.8.8", "1.1.1.1", "208.67.222.222"],
                "gaming_servers": {
                    "Valorant": ["104.18.0.0", "104.18.1.0"],
                    "CS2": ["162.254.196.0", "162.254.197.0"],
                    "Fortnite": ["3.208.0.0", "3.208.1.0"]
                }
            },
            "multi_internet": {
                "enabled": True,
                "auto_failover": True,
                "load_balancing": False,
                "monitoring_interval": 30,
                "quality_threshold": 50.0
            },
            "traffic_shaper": {
                "enabled": True,
                "prioritize_gaming": True,
                "limit_background": True,
                "bandwidth_limit": None,
                "gaming_ports": {
                    "Valorant": [7000, 7001, 7002, 7003, 7004, 7005],
                    "CS2": [27015, 27016, 27017, 27018, 27019, 27020],
                    "Fortnite": [5222, 5223, 5224, 5225, 5226, 5227]
                }
            },
            "ram_cleaner": {
                "enabled": True,
                "auto_clean": False,
                "cleanup_interval": 300,
                "memory_threshold": 80.0,
                "aggressive_cleanup": False
            },
            "ui": {
                "theme": "dark",
                "window_size": [1200, 800],
                "auto_start": False,
                "minimize_to_tray": True,
                "show_notifications": True
            },
            "advanced": {
                "debug_mode": False,
                "log_level": "INFO",
                "backup_config": True,
                "update_check": True
            }
        }
    
    def get_fps_boost_config(self) -> Dict[str, Any]:
        """Get FPS Boost configuration"""
        return self.get_setting("fps_boost", {})
    
    def set_fps_boost_config(self, config: Dict[str, Any]) -> bool:
        """Set FPS Boost configuration"""
        return self.set_setting("fps_boost", config)
    
    def get_network_analyzer_config(self) -> Dict[str, Any]:
        """Get Network Analyzer configuration"""
        return self.get_setting("network_analyzer", {})
    
    def set_network_analyzer_config(self, config: Dict[str, Any]) -> bool:
        """Set Network Analyzer configuration"""
        return self.set_setting("network_analyzer", config)
    
    def get_multi_internet_config(self) -> Dict[str, Any]:
        """Get Multi Internet configuration"""
        return self.get_setting("multi_internet", {})
    
    def set_multi_internet_config(self, config: Dict[str, Any]) -> bool:
        """Set Multi Internet configuration"""
        return self.set_setting("multi_internet", config)
    
    def get_traffic_shaper_config(self) -> Dict[str, Any]:
        """Get Traffic Shaper configuration"""
        return self.get_setting("traffic_shaper", {})
    
    def set_traffic_shaper_config(self, config: Dict[str, Any]) -> bool:
        """Set Traffic Shaper configuration"""
        return self.set_setting("traffic_shaper", config)
    
    def get_ram_cleaner_config(self) -> Dict[str, Any]:
        """Get RAM Cleaner configuration"""
        return self.get_setting("ram_cleaner", {})
    
    def set_ram_cleaner_config(self, config: Dict[str, Any]) -> bool:
        """Set RAM Cleaner configuration"""
        return self.set_setting("ram_cleaner", config)
    
    def get_ui_config(self) -> Dict[str, Any]:
        """Get UI configuration"""
        return self.get_setting("ui", {})
    
    def set_ui_config(self, config: Dict[str, Any]) -> bool:
        """Set UI configuration"""
        return self.set_setting("ui", config)
    
    def get_advanced_config(self) -> Dict[str, Any]:
        """Get advanced configuration"""
        return self.get_setting("advanced", {})
    
    def set_advanced_config(self, config: Dict[str, Any]) -> bool:
        """Set advanced configuration"""
        return self.set_setting("advanced", config)
    
    def reset_to_defaults(self) -> bool:
        """Reset all settings to defaults"""
        try:
            self.config = self._get_default_config()
            return self.save_settings({})
        except Exception:
            return False
    
    def export_config(self, file_path: str) -> bool:
        """Export configuration to a file"""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception:
            return False
    
    def import_config(self, file_path: str) -> bool:
        """Import configuration from a file"""
        try:
            with open(file_path, 'r') as f:
                imported_config = json.load(f)
            
            # Validate configuration
            if self._validate_config(imported_config):
                self.config = imported_config
                return self.save_settings({})
            else:
                return False
        except Exception:
            return False
    
    def _validate_config(self, config: Dict[str, Any]) -> bool:
        """Validate configuration structure"""
        try:
            required_keys = [
                "fps_boost", "network_analyzer", "multi_internet",
                "traffic_shaper", "ram_cleaner", "ui", "advanced"
            ]
            
            for key in required_keys:
                if key not in config:
                    return False
            
            return True
        except Exception:
            return False
    
    def get_config_summary(self) -> Dict[str, Any]:
        """Get configuration summary"""
        return {
            "version": self.get_setting("version", "1.0.0"),
            "last_updated": self.get_setting("last_updated", time.time()),
            "modules_enabled": {
                "fps_boost": self.get_setting("fps_boost.enabled", True),
                "network_analyzer": self.get_setting("network_analyzer.enabled", True),
                "multi_internet": self.get_setting("multi_internet.enabled", True),
                "traffic_shaper": self.get_setting("traffic_shaper.enabled", True),
                "ram_cleaner": self.get_setting("ram_cleaner.enabled", True)
            },
            "auto_features": {
                "auto_clean": self.get_setting("ram_cleaner.auto_clean", False),
                "auto_analysis": self.get_setting("network_analyzer.auto_analysis", False),
                "auto_failover": self.get_setting("multi_internet.auto_failover", True)
            }
        }
    
    def backup_config(self) -> bool:
        """Create a backup of the current configuration"""
        try:
            backup_file = f"config_backup_{int(time.time())}.json"
            return self.export_config(backup_file)
        except Exception:
            return False
    
    def restore_config(self, backup_file: str) -> bool:
        """Restore configuration from backup"""
        try:
            return self.import_config(backup_file)
        except Exception:
            return False
    
    def get_recent_backups(self) -> list:
        """Get list of recent configuration backups"""
        try:
            backup_files = []
            for file in os.listdir("."):
                if file.startswith("config_backup_") and file.endswith(".json"):
                    backup_files.append(file)
            
            # Sort by modification time (newest first)
            backup_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
            return backup_files[:10]  # Last 10 backups
        except Exception:
            return []
    
    def cleanup_old_backups(self, keep_count: int = 5) -> bool:
        """Clean up old configuration backups"""
        try:
            backup_files = self.get_recent_backups()
            
            # Remove old backups
            for backup_file in backup_files[keep_count:]:
                try:
                    os.remove(backup_file)
                except OSError:
                    continue
            
            return True
        except Exception:
            return False
