"""
Verify your Python environment is set up correctly
Run: python3 check_setup.py
"""

import sys
import subprocess


def check_python_version():
    """Verify Python version"""
    version = sys.version_info
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print("⚠️  Warning: Python 3.10+ recommended (you have older version)")
        return False
    return True


def check_standard_library():
    """Check standard library modules"""
    modules = ['json', 'asyncio', 'typing', 'dataclasses']
    
    print(f"\n📦 Checking standard library modules...")
    all_good = True
    for module in modules:
        try:
            __import__(module)
            print(f"  ✅ {module}")
        except ImportError:
            print(f"  ❌ {module} (MISSING)")
            all_good = False
    
    return all_good


def check_optional_packages():
    """Check optional packages (needed for later weeks)"""
    packages = {
        'requests': 'HTTP library (Week 2)',
        'pydantic': 'Data validation (Week 1-4)',
        'anthropic': 'Claude API (Week 3)',
        'python-dotenv': 'Environment variables (Week 3)'
    }
    
    print(f"\n📦 Checking optional packages...")
    missing = []
    
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"  ✅ {package:20} - {description}")
        except ImportError:
            print(f"  ⚠️  {package:20} - {description} (not installed)")
            missing.append(package)
    
    if missing:
        print(f"\n💡 Install missing packages:")
        print(f"   pip3 install {' '.join(missing)}")
    
    return len(missing) == 0


def main():
    print("="*70)
    print("🔍 PYTHON ENVIRONMENT CHECK")
    print("="*70)
    
    print("\n1. Python Version")
    print("-" * 70)
    py_ok = check_python_version()
    
    print("\n2. Standard Library")
    print("-" * 70)
    stdlib_ok = check_standard_library()
    
    print("\n3. Optional Packages (for future exercises)")
    print("-" * 70)
    optional_ok = check_optional_packages()
    
    print("\n" + "="*70)
    if py_ok and stdlib_ok:
        print("✅ YOUR ENVIRONMENT IS READY FOR WEEK 1!")
        print("="*70)
        print("""
Next steps:
1. Run: python3 00_START_HERE.py
2. Start with Exercise 1: python3 01_syntax_comparison.py
3. Follow the learning path
""")
    else:
        print("⚠️  SOME CHECKS FAILED - See above for details")
        print("="*70)


if __name__ == "__main__":
    main()
