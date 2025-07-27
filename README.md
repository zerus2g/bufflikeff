# 🔥 Free Fire Buff Like Tool

Tool tự động hóa buff like Free Fire với giao diện web đẹp mắt và tính năng theo dõi lịch sử.

## ✨ Tính năng

- 🚀 **Buff like tự động**: Gọi API buff like Free Fire
- 📊 **Thống kê real-time**: Hiển thị số liệu buff thành công/thất bại
- 📋 **Lịch sử chi tiết**: Theo dõi tất cả các lần buff
- 📤 **Xuất dữ liệu**: Export lịch sử ra CSV/JSON
- 🎨 **Giao diện đẹp**: Sử dụng Tailwind CSS
- 🐳 **Docker ready**: Triển khai dễ dàng với Docker

## 🛠️ Công nghệ sử dụng

- **Backend**: Python FastAPI
- **Database**: SQLite
- **Frontend**: HTML, JavaScript, Tailwind CSS, Alpine.js
- **Container**: Docker
- **API**: aiohttp cho HTTP requests

## 🚀 Cài đặt và chạy

### Cách 1: Sử dụng Docker (Khuyến nghị)

```bash
# Clone repository
git clone <repository-url>
cd free-fire-buff-tool

# Build và chạy với Docker
docker build -t free-fire-buff-tool .
docker run -p 8000:8000 free-fire-buff-tool
```

### Cách 2: Chạy trực tiếp

```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python main.py
```

## 📖 Hướng dẫn sử dụng

### 1. Truy cập ứng dụng
Mở trình duyệt và truy cập: `http://localhost:8000`

### 2. Buff like
- Nhập **UID Free Fire** của bạn
- Nhập **Key buff** hợp lệ
- Nhấn "🚀 Buff Like Ngay"
- Kiểm tra kết quả

### 3. Xem lịch sử
- Chuyển sang tab "📊 Lịch sử"
- Xem chi tiết các lần buff
- Xuất dữ liệu ra CSV/JSON

## 📊 API Endpoints

### POST `/api/buff`
Buff like cho UID và Key được cung cấp

**Parameters:**
- `uid` (string): UID Free Fire
- `key` (string): Key buff

**Response:**
```json
{
  "success": true,
  "data": [...],
  "message": "Buff like thành công"
}
```

### GET `/api/stats`
Lấy thống kê buff

**Response:**
```json
{
  "total_buffs": 10,
  "successful_buffs": 8,
  "today_buffs": 3,
  "success_rate": 80.0
}
```

## 🗄️ Database Schema

```sql
CREATE TABLE buff_history (
    id INTEGER PRIMARY KEY,
    uid VARCHAR,
    key VARCHAR,
    status VARCHAR,
    message TEXT,
    likes_count INTEGER DEFAULT 0,
    remaining_limit VARCHAR,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## 🔧 Cấu hình

### Environment Variables
- `PORT`: Port để chạy ứng dụng (mặc định: 8000)
- `DATABASE_URL`: URL database (mặc định: SQLite local)

### API Configuration
API URL được cấu hình trong `main.py`:
```python
BUFF_API_URL = "https://likes-ch9ayfa-free.vercel.app/like"
```

## 📁 Cấu trúc dự án

```
free-fire-buff-tool/
├── main.py              # FastAPI application
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── README.md           # Documentation
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   └── history.html   # History page
└── buff_like.db       # SQLite database (auto-generated)
```

## 🐛 Troubleshooting

### Lỗi kết nối API
- Kiểm tra kết nối internet
- Xác minh API URL có hoạt động
- Kiểm tra UID và Key có hợp lệ

### Lỗi database
- Xóa file `buff_like.db` để tạo lại database
- Kiểm tra quyền ghi file

### Lỗi Docker
- Đảm bảo Docker đã cài đặt
- Kiểm tra port 8000 không bị sử dụng
- Chạy `docker logs <container-id>` để xem logs

## 🔒 Bảo mật

- Không lưu trữ thông tin nhạy cảm
- Sử dụng HTTPS trong production
- Validate input data
- Rate limiting cho API calls

## 📈 Monitoring

- Health check endpoint: `/health`
- Logs được ghi ra console
- Database backup định kỳ

## 🤝 Đóng góp

1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Tạo Pull Request

## 📄 License

MIT License - Xem file LICENSE để biết thêm chi tiết.

## 📞 Hỗ trợ

Nếu gặp vấn đề, vui lòng:
1. Kiểm tra documentation
2. Xem issues đã có
3. Tạo issue mới với thông tin chi tiết

---

**Lưu ý**: Tool này chỉ dành cho mục đích giáo dục và nghiên cứu. Hãy sử dụng có trách nhiệm và tuân thủ điều khoản sử dụng của Free Fire. 