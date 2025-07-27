#!/usr/bin/env python3
"""
Demo script để test chức năng buff like
"""

import asyncio
import aiohttp
import json
from datetime import datetime

async def demo_buff_like():
    """Demo buff like với UID và key mẫu"""
    print("🚀 Demo Buff Like Free Fire")
    print("=" * 40)
    
    # Test data
    test_uid = "8784017287"
    test_key = "ch9ayfa-l7away"
    
    print(f"📝 Test Data:")
    print(f"   UID: {test_uid}")
    print(f"   Key: ch9ayfa-l7away (mặc định)")
    print()
    
    # Test API call
    print("🔍 Testing API call...")
    try:
        url = f"https://likes-ch9ayfa-free.vercel.app/like?uid={test_uid}&key={test_key}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    print("✅ API call successful!")
                    print(f"📊 Response: {json.dumps(data, indent=2)}")
                    
                    # Parse response
                    for item in data:
                        if "Status" in item:
                            print(f"🎯 Status: {item['Status']}")
                        if "Current Likes" in item:
                            print(f"❤️ Current Likes: {item['Current Likes']}")
                        if "remaining limit" in item:
                            print(f"📈 Remaining Limit: {item['remaining limit']}")
                        if "message" in item:
                            print(f"💬 Message: {item['message']}")
                    
                    return True
                else:
                    print(f"❌ API call failed with status: {response.status}")
                    return False
    except Exception as e:
        print(f"❌ API call error: {e}")
        return False

async def demo_local_app():
    """Demo ứng dụng local"""
    print("\n🌐 Testing local application...")
    
    try:
        # Test stats endpoint
        async with aiohttp.ClientSession() as session:
            async with session.get("http://localhost:8000/api/stats") as response:
                if response.status == 200:
                    data = await response.json()
                    print("✅ Local app working!")
                    print(f"📊 Stats: {json.dumps(data, indent=2)}")
                    return True
                else:
                    print(f"❌ Local app failed with status: {response.status}")
                    return False
    except Exception as e:
        print(f"❌ Local app error: {e}")
        print("💡 Make sure the app is running on http://localhost:8000")
        return False

async def demo_buff_via_local():
    """Demo buff via local app"""
    print("\n🎯 Testing buff via local app...")
    
    try:
        # Test buff endpoint
        test_uid = "8784017287"
        # Key sẽ được sử dụng mặc định từ server
        
        async with aiohttp.ClientSession() as session:
            # Create form data
            form_data = aiohttp.FormData()
            form_data.add_field('uid', test_uid)
            form_data.add_field('key', 'ch9ayfa-l7away')  # Gửi key mặc định
            
            async with session.post("http://localhost:8000/api/buff", data=form_data) as response:
                if response.status == 200:
                    data = await response.json()
                    print("✅ Buff via local app successful!")
                    print(f"📊 Response: {json.dumps(data, indent=2)}")
                    return True
                else:
                    print(f"❌ Buff via local app failed with status: {response.status}")
                    return False
    except Exception as e:
        print(f"❌ Buff via local app error: {e}")
        return False

async def main():
    """Main demo function"""
    print("🔥 Free Fire Buff Like Tool Demo")
    print("=" * 50)
    
    # Test 1: Direct API call
    api_ok = await demo_buff_like()
    
    # Test 2: Local app stats
    local_ok = await demo_local_app()
    
    # Test 3: Buff via local app
    buff_ok = await demo_buff_via_local()
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 Demo Summary:")
    print(f"   Direct API: {'✅' if api_ok else '❌'}")
    print(f"   Local App: {'✅' if local_ok else '❌'}")
    print(f"   Buff via Local: {'✅' if buff_ok else '❌'}")
    
    if all([api_ok, local_ok, buff_ok]):
        print("\n🎉 All demos passed! The tool is working perfectly.")
        print("\n💡 You can now:")
        print("   1. Open http://localhost:8000 in your browser")
        print("   2. Enter UID and Key to buff like")
        print("   3. Check history at http://localhost:8000/history")
    else:
        print("\n⚠️ Some demos failed. Please check the issues above.")
    
    print("\n🔗 Access the web interface:")
    print("   http://localhost:8000")

if __name__ == "__main__":
    asyncio.run(main()) 