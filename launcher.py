#!/usr/bin/env python3
"""
NGXSMK GameNet Optimizer Launcher
Simple launcher script with error handling and dependency checking
"""

import sys
import os
import subprocess
import importlib.util

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'psutil',
        'tkinter',
        'threading',
        'socket',
        'time',
        'json',
        'subprocess',
        'platform'
    ]
    
    optional_packages = [
        'ping3',
        'speedtest',
        'netifaces',
        'matplotlib',
        'numpy'
    ]
    
    missing_required = []
    missing_optional = []
    
    for package in required_packages:
        try:
            if package == 'tkinter':
                import tkinter
            else:
                importlib.import_module(package)
        except ImportError:
            missing_required.append(package)
    
    for package in optional_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            missing_optional.append(package)
    
    if missing_required:
        print("❌ Missing required dependencies:")
        for package in missing_required:
            print(f"   - {package}")
        print("\nPlease install missing dependencies:")
        print("pip install -r requirements.txt")
        return False
    
    if missing_optional:
        print("⚠️  Missing optional dependencies (some features may not work):")
        for package in missing_optional:
            print(f"   - {package}")
        print("\nFor full functionality, install optional dependencies:")
        print("pip install ping3 speedtest-cli netifaces matplotlib numpy")
    
    return True

def check_permissions():
    """Check if running with sufficient permissions"""
    try:
        import psutil
        # Try to access system information
        psutil.cpu_percent()
        return True
    except Exception:
        print("⚠️  Some features may require administrator privileges")
        return False

def main():
    """Main launcher function"""
    print("🚀 NGXSMK GameNet Optimizer Launcher")
    print("=" * 40)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✅ Python version: {sys.version.split()[0]}")
    
    # Check dependencies
    print("\n🔍 Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    
    print("✅ All required dependencies found")
    
    # Check permissions
    print("\n🔐 Checking permissions...")
    check_permissions()
    
    # Check if main.py exists
    if not os.path.exists('main.py'):
        print("❌ main.py not found in current directory")
        sys.exit(1)
    
    print("✅ Application files found")
    
    # Launch application
    print("\n🎮 Launching NGXSMK GameNet Optimizer...")
    print("=" * 40)
    
    try:
        # Import and run the main application
        from main import NetworkOptimizerApp
        
        app = NetworkOptimizerApp()
        app.run()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all modules are in the correct location")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Application error: {e}")
        print("Check the error message above for details")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Application interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
