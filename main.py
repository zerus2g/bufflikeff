from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import aiohttp
import json
import os

# Khởi tạo FastAPI app
app = FastAPI(title="Free Fire Buff Like Tool", version="1.0.0")

# Cấu hình templates
templates = Jinja2Templates(directory="templates")

# API URL và Key mặc định
BUFF_API_URL = "https://likes-ch9ayfa-free.vercel.app/like"
DEFAULT_KEY = "ch9ayfa-l7away"

class BuffLikeService:
    """Service để xử lý buff like Free Fire"""
    
    @staticmethod
    async def buff_like(uid: str, key: str) -> dict:
        """Gọi API buff like"""
        try:
            url = f"{BUFF_API_URL}?uid={uid}&key={key}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        return {
                            "success": True,
                            "data": data,
                            "status_code": response.status
                        }
                    else:
                        return {
                            "success": False,
                            "error": f"API error: {response.status}",
                            "status_code": response.status
                        }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "status_code": 500
            }

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Trang chủ với form buff like"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/history", response_class=HTMLResponse)
async def history(request: Request):
    """Trang lịch sử buff (đơn giản hóa)"""
    return templates.TemplateResponse("history.html", {"request": request, "history": []})

@app.post("/api/buff")
async def buff_like_api(uid: str = Form(...), key: str = Form("")):
    """API endpoint để buff like"""
    # Sử dụng key mặc định nếu không có key được cung cấp
    if not key:
        key = DEFAULT_KEY
    
    # Gọi service buff like
    result = await BuffLikeService.buff_like(uid, key)
    
    return result

@app.get("/api/stats")
async def get_stats():
    """API endpoint để lấy thống kê"""
    return {
        "total_buffs": 0,
        "successful_buffs": 0,
        "failed_buffs": 0
    }

# Vercel serverless handler
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 