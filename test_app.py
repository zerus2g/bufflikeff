#!/usr/bin/env python3
"""
Test script cho Free Fire Buff Like Tool
"""

import asyncio
import aiohttp
import json
from datetime import datetime

# Test API URL
TEST_API_URL = "https://likes-ch9ayfa-free.vercel.app/like"

async def test_api_connection():
    """Test kết nối đến API"""
    print("🔍 Testing API connection...")
    
    try:
        # Test với UID và key mẫu
        test_uid = "8784017287"
        test_key = "ch9ayfa-l7away"
        
        url = f"{TEST_API_URL}?uid={test_uid}&key={test_key}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    print("✅ API connection successful!")
                    print(f"📊 Response data: {json.dumps(data, indent=2)}")
                    return True
                else:
                    print(f"❌ API connection failed with status: {response.status}")
                    return False
    except Exception as e:
        print(f"❌ API connection error: {e}")
        return False

async def test_local_app():
    """Test ứng dụng local"""
    print("\n🔍 Testing local application...")
    
    try:
        # Test stats endpoint
        async with aiohttp.ClientSession() as session:
            async with session.get("http://localhost:8000/api/stats") as response:
                if response.status == 200:
                    data = await response.json()
                    print("✅ Local app stats endpoint working!")
                    print(f"📊 Stats: {json.dumps(data, indent=2)}")
                    return True
                else:
                    print(f"❌ Local app test failed with status: {response.status}")
                    return False
    except Exception as e:
        print(f"❌ Local app test error: {e}")
        print("💡 Make sure the app is running on http://localhost:8000")
        return False

def test_database_connection():
    """Test kết nối database"""
    print("\n🔍 Testing database connection...")
    
    try:
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        
        # Test database connection
        engine = create_engine("sqlite:///./buff_like.db", connect_args={"check_same_thread": False})
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
        # Test session
        db = SessionLocal()
        from sqlalchemy import text
        db.execute(text("SELECT 1"))
        db.close()
        
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        return False

def test_dependencies():
    """Test các dependencies"""
    print("\n🔍 Testing dependencies...")
    
    required_packages = [
        "fastapi",
        "uvicorn", 
        "sqlalchemy",
        "aiohttp",
        "jinja2"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} - OK")
        except ImportError:
            print(f"❌ {package} - Missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️ Missing packages: {', '.join(missing_packages)}")
        print("💡 Run: pip install -r requirements.txt")
        return False
    else:
        print("✅ All dependencies installed!")
        return True

async def main():
    """Main test function"""
    print("🚀 Starting Free Fire Buff Like Tool Tests")
    print("=" * 50)
    
    # Test dependencies
    deps_ok = test_dependencies()
    
    # Test database
    db_ok = test_database_connection()
    
    # Test API connection
    api_ok = await test_api_connection()
    
    # Test local app (if running)
    local_ok = await test_local_app()
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 Test Summary:")
    print(f"   Dependencies: {'✅' if deps_ok else '❌'}")
    print(f"   Database: {'✅' if db_ok else '❌'}")
    print(f"   API Connection: {'✅' if api_ok else '❌'}")
    print(f"   Local App: {'✅' if local_ok else '❌'}")
    
    if all([deps_ok, db_ok, api_ok]):
        print("\n🎉 All critical tests passed! The tool should work correctly.")
    else:
        print("\n⚠️ Some tests failed. Please check the issues above.")
    
    print("\n💡 To start the app:")
    print("   python main.py")
    print("   # or")
    print("   docker build -t free-fire-buff-tool .")
    print("   docker run -p 8000:8000 free-fire-buff-tool")

if __name__ == "__main__":
    asyncio.run(main()) 