from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import aiohttp
import asyncio
import json
import os

# Khởi tạo FastAPI app
app = FastAPI(title="Free Fire Buff Like Tool", version="1.0.0")

# Cấu hình database
SQLALCHEMY_DATABASE_URL = "sqlite:///./buff_like.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Model
class BuffHistory(Base):
    __tablename__ = "buff_history"
    
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, index=True)
    key = Column(String)
    status = Column(String)
    message = Column(Text)
    likes_count = Column(Integer, default=0)
    remaining_limit = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Tạo database tables
Base.metadata.create_all(bind=engine)

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
    """Trang lịch sử buff"""
    db = SessionLocal()
    try:
        history = db.query(BuffHistory).order_by(BuffHistory.created_at.desc()).limit(50).all()
        return templates.TemplateResponse("history.html", {"request": request, "history": history})
    finally:
        db.close()

@app.post("/api/buff")
async def buff_like_api(uid: str = Form(...), key: str = Form("")):
    """API endpoint để buff like"""
    # Sử dụng key mặc định nếu không có key được cung cấp
    if not key:
        key = DEFAULT_KEY
    
    # Gọi service buff like
    result = await BuffLikeService.buff_like(uid, key)
    
    # Lưu vào database
    db = SessionLocal()
    try:
        if result["success"]:
            data = result["data"]
            # Tìm thông tin từ response
            status = "Success"
            message = "Buff like thành công"
            likes_count = 0
            remaining_limit = "Unknown"
            
            for item in data:
                if "Status" in item:
                    status = item["Status"]
                if "Current Likes" in item:
                    likes_count = item["Current Likes"]
                if "remaining limit" in item:
                    remaining_limit = item["remaining limit"]
                if "message" in item:
                    message = item["message"]
            
            # Lưu vào database
            buff_record = BuffHistory(
                uid=uid,
                key=key,
                status=status,
                message=message,
                likes_count=likes_count,
                remaining_limit=remaining_limit
            )
            db.add(buff_record)
            db.commit()
            
            return {
                "success": True,
                "data": data,
                "message": "Buff like thành công"
            }
        else:
            # Lưu lỗi vào database
            buff_record = BuffHistory(
                uid=uid,
                key=key,
                status="Error",
                message=result["error"],
                likes_count=0,
                remaining_limit="0"
            )
            db.add(buff_record)
            db.commit()
            
            return {
                "success": False,
                "error": result["error"]
            }
    finally:
        db.close()

@app.get("/api/stats")
async def get_stats():
    """API để lấy thống kê"""
    db = SessionLocal()
    try:
        total_buffs = db.query(BuffHistory).count()
        successful_buffs = db.query(BuffHistory).filter(BuffHistory.status.like("%Success%")).count()
        today_buffs = db.query(BuffHistory).filter(
            BuffHistory.created_at >= datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        ).count()
        
        return {
            "total_buffs": total_buffs,
            "successful_buffs": successful_buffs,
            "today_buffs": today_buffs,
            "success_rate": round((successful_buffs / total_buffs * 100) if total_buffs > 0 else 0, 2)
        }
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 