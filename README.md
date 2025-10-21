# NGXSMK GameNet Optimizer

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen.svg)](https://github.com)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11-lightgrey.svg)](https://github.com)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/actions)
[![GitHub stars](https://img.shields.io/github/stars/toozuuu/ngxsmk-gamenet-optimizer.svg)](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/toozuuu/ngxsmk-gamenet-optimizer.svg)](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/network)
[![Downloads](https://img.shields.io/badge/Downloads-Latest-blue.svg)](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/releases)

> **A powerful, open-source gaming optimization suite that enhances your gaming experience through advanced network optimization, system tuning, and performance monitoring.**

## 🚀 Quick Start

### Download Pre-built Executable (Recommended)
1. **Download** the latest release from [Releases](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/releases)
2. **Extract** the executable from the zip file
3. **Run** `NGXSMK_GameNet_Optimizer_Advanced.exe`
4. **Enjoy** optimized gaming performance!

### Build from Source
```bash
# Clone the repository
git clone https://github.com/toozuuu/ngxsmk-gamenet-optimizer.git
cd ngxsmk-gamenet-optimizer

# Install dependencies
pip install -r requirements.txt

# Build executable
python build_simple_advanced.py

# Run the application
python main.py
```

## ✨ What is NGXSMK GameNet Optimizer?

NGXSMK GameNet Optimizer is a comprehensive, open-source gaming optimization tool designed to enhance your gaming experience through intelligent system and network optimization. Unlike commercial alternatives, it's completely free, open-source, and respects your privacy.

### 🎯 Key Benefits

- **🚀 Boost FPS** - Optimize system performance for higher frame rates
- **🌐 Reduce Latency** - Advanced network optimization for lower ping
- **🧹 Clean Memory** - Intelligent RAM management and cleanup
- **⚡ Smart Traffic** - Prioritize gaming traffic over background apps
- **🎮 Game-Specific** - Tailored optimizations for popular games
- **🔒 Privacy-First** - No data collection, everything runs locally

## 🌟 Features

### 🎮 FPS Boost & Game Optimization
- **Intelligent Game Detection** - Automatically detects and optimizes running games
- **Process Priority Management** - Sets high priority for gaming applications
- **CPU & GPU Optimization** - Advanced system tuning for maximum performance
- **Real-time Monitoring** - Live FPS and system metrics display

### 🌐 Network Analyzer
- **Multi-Server Testing** - Test latency to gaming servers worldwide
- **Bandwidth Analysis** - Comprehensive speed testing and analysis
- **Gaming Server Optimization** - Specialized testing for popular games
- **Connection Quality Assessment** - Detailed network quality scoring

### 🔄 Multi-Connection Manager
- **Load Balancing** - Distribute traffic across multiple connections
- **Automatic Failover** - Seamless switching to backup connections
- **Quality Monitoring** - Real-time connection performance tracking
- **Smart Routing** - Optimize traffic paths for gaming

### 🚦 Traffic Shaper
- **Bandwidth Control** - Set limits and prioritize gaming traffic
- **QoS Management** - Quality of Service for optimal gaming
- **Background App Limiting** - Reduce interference from other applications
- **Real-time Monitoring** - Live bandwidth usage tracking

### 🧹 Memory Optimizer
- **Smart RAM Cleaning** - Intelligent memory management
- **Process Optimization** - Close unnecessary background applications
- **Auto-cleanup** - Automatic memory optimization
- **Gaming-Specific Tuning** - Optimized for gaming workloads

### 🎯 League of Legends Optimizer
- **Dedicated LoL Support** - Specialized optimizations for League of Legends
- **Server Latency Testing** - Test ping to all major LoL servers (NA, EUW, EUNE, KR, BR, SG)
- **Best Server Selection** - Automatically find your optimal server
- **Real-time Performance** - Monitor LoL-specific metrics

## 🎮 Supported Games

- **League of Legends** (with server testing)
- **Valorant**
- **Counter-Strike 2**
- **Fortnite**
- **Apex Legends**
- **Call of Duty**
- **Overwatch**
- **Dota 2**
- **PUBG**
- **Rust**
- **Minecraft**
- And many more!

## 🛠️ Installation

### Prerequisites
- Python 3.13+ (for building from source)
- Windows 10/11 (primary support)
- Administrator privileges (for full functionality)

### Automated Builds
This project uses GitHub Actions for automated building and testing:

- **🔄 Automatic Builds** - Every push triggers a new build
- **📦 Pre-built Executables** - Download ready-to-use executables
- **🧪 Automated Testing** - Continuous integration testing
- **📋 Build Status** - Real-time build status monitoring

### Download Latest Build
Visit the [Actions](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/actions) page to download the latest automated build artifacts.

### Method 1: Quick Install
```bash
git clone https://github.com/toozuuu/ngxsmk-gamenet-optimizer.git
cd ngxsmk-gamenet-optimizer
pip install -r requirements.txt
python launcher.py
```

### Method 2: Simple Installer
```bash
python install_simple.py
```

### Method 3: Platform-Specific

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
./run.sh
```

## 📖 Usage

### Basic Usage
1. **Launch** the application using `python launcher.py`
2. **Click "Start Optimization"** for automatic optimization
3. **Use individual tabs** to configure specific features
4. **Monitor performance** in real-time

### Advanced Configuration
- **FPS Boost**: Configure game-specific optimizations
- **Network Analyzer**: Test and optimize your connection
- **Multi Internet**: Manage multiple connections
- **Traffic Shaper**: Control bandwidth allocation
- **RAM Cleaner**: Optimize memory usage
- **LoL Optimizer**: Specialized League of Legends features

## 🏗️ Project Structure

```
ngxsmk-gamenet-optimizer/
├── main.py                    # Main application
├── build_simple_advanced.py   # Build script
├── build_local.py             # Local development build
├── requirements.txt           # Python dependencies
├── requirements_minimal.txt   # Minimal dependencies
├── modules/                   # Core optimization modules
│   ├── fps_boost.py          # FPS optimization
│   ├── network_analyzer.py   # Network analysis
│   ├── multi_internet.py     # Multi-connection management
│   ├── traffic_shaper.py     # Traffic shaping
│   ├── ram_cleaner.py        # Memory optimization
│   ├── lol_optimizer.py      # League of Legends specific
│   ├── config_manager.py     # Configuration management
│   ├── settings_dialog.py    # Settings interface
│   ├── advanced_optimizer.py # Advanced optimization
│   ├── system_monitor.py     # System monitoring
│   ├── network_optimizer.py # Network optimization
│   └── gaming_optimizer.py   # Gaming optimization
├── .github/workflows/         # CI/CD pipelines
│   ├── build.yml             # Main build workflow
│   ├── dev-build.yml         # Development builds
│   ├── release.yml           # Release workflow
│   └── test.yml              # Testing workflow
├── dist/                     # Built executables
├── LICENSE                   # MIT License
├── CONTRIBUTING.md           # Contributing guidelines
├── CODE_OF_CONDUCT.md       # Code of conduct
├── CHANGELOG.md              # Version history
└── README.md                 # This file
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Development Setup
```bash
git clone https://github.com/toozuuu/ngxsmk-gamenet-optimizer.git
cd ngxsmk-gamenet-optimizer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Local Building
```bash
# Quick local build
python build_local.py

# Or use the existing build script
python build_simple_advanced.py
```

## 🔄 CI/CD Pipeline

This project uses GitHub Actions for automated building, testing, and deployment:

### 🏗️ Build Workflows
- **Main Build** (`build.yml`) - Builds on push to main/develop branches
- **Development Build** (`dev-build.yml`) - Quick builds for feature branches
- **Release Build** (`release.yml`) - Creates releases with executables
- **Test Suite** (`test.yml`) - Automated testing and validation

### 📦 Automated Features
- **🔄 Auto Build** - Every push triggers a new build
- **🧪 Auto Test** - Comprehensive testing on multiple Python versions
- **📦 Auto Release** - Automatic release creation on version tags
- **📋 Build Status** - Real-time build status monitoring
- **🔍 Security Scan** - Basic security checks on builds

### 🚀 Release Process
1. **Tag Creation** - Create a version tag (e.g., `v2.0.0`)
2. **Auto Build** - GitHub Actions automatically builds the executable
3. **Auto Release** - Release is created with downloadable executables
4. **Artifact Upload** - Build artifacts are uploaded to releases

### 📊 Build Artifacts
- **Executable** - Ready-to-run Windows executable
- **Archive** - Complete package with documentation
- **Build Info** - Detailed build information and changelog

## 📊 Performance Benefits

- **Reduced Latency** - Optimize network routing for lower ping
- **Higher FPS** - System optimization for better frame rates
- **Less Lag** - Traffic shaping and priority management
- **Better Stability** - Memory optimization and process management
- **Optimal Server Selection** - Find the best gaming servers

## 🔒 Privacy & Security

- **100% Local Processing** - No data sent to external servers
- **No Telemetry** - Complete privacy protection
- **Open Source** - Full transparency and auditability
- **No Ads** - Completely ad-free experience
- **No Data Collection** - Your data stays on your device

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 10/11 (64-bit)
- **RAM**: 4GB minimum, 8GB recommended
- **CPU**: Dual-core processor (2.0 GHz+)
- **Storage**: 100MB free space
- **Network**: Active internet connection
- **Permissions**: Administrator privileges for full functionality

### Recommended Requirements
- **OS**: Windows 11 (latest updates)
- **RAM**: 16GB or more
- **CPU**: Quad-core processor (3.0 GHz+)
- **Storage**: 500MB free space (SSD recommended)
- **Network**: High-speed internet connection
- **GPU**: Dedicated graphics card for gaming

### Build Requirements (for developers)
- **Python**: 3.13+ with pip
- **PyInstaller**: For building executables
- **Git**: For version control
- **Visual Studio Build Tools**: For compiling dependencies (Windows)

## 🐛 Troubleshooting

### Common Issues
1. **Permission Errors**: Run as administrator
2. **Network Analysis Fails**: Check firewall settings
3. **Memory Cleanup Issues**: Ensure sufficient system resources

### Getting Help
- **GitHub Issues**: [Report bugs and request features](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/issues)
- **Discussions**: [Community discussions](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/discussions)
- **Email**: sachindilshan040@gmail.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the gaming community's need for accessible optimization tools
- Built with open source principles and community feedback
- Special thanks to all contributors and testers

## 🔮 Roadmap

- [ ] macOS support
- [ ] Additional game support
- [ ] Advanced network protocols
- [ ] Machine learning optimization
- [ ] Plugin system
- [ ] Mobile companion app

## 📞 Support

- **GitHub Issues**: [Report bugs and request features](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/issues)
- **Discussions**: [Community discussions](https://github.com/toozuuu/ngxsmk-gamenet-optimizer/discussions)
- **Email**: sachindilshan040@gmail.com
- **Maintainer**: [@toozuuu](https://github.com/toozuuu)

---

**Made with ❤️ for the gaming community**

*NGXSMK GameNet Optimizer - Optimize your gaming experience, open source and free!*