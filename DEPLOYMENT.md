# 🚀 Deploy Free Fire Buff Like Tool lên Vercel

## 📋 Yêu Cầu

- Tài khoản [Vercel](https://vercel.com) (miễn phí)
- Tài khoản [GitHub](https://github.com) để lưu code
- Node.js (để cài đặt Vercel CLI)

## 🔧 Cài Đặt Vercel CLI

```bash
npm install -g vercel
```

## 📁 Chuẩn Bị Dự Án

### 1. Tạo Repository GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/free-fire-buff-tool.git
git push -u origin main
```

### 2. Cấu Trúc Files
```
free-fire-buff-tool/
├── main.py                 # FastAPI app
├── requirements.txt        # Dependencies
├── vercel.json            # Vercel config
├── api/
│   └── index.py          # Vercel handler
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   └── history.html
└── README.md
```

## 🚀 Deploy Lên Vercel

### Cách 1: Sử dụng Vercel CLI

```bash
# Login vào Vercel
vercel login

# Deploy
vercel

# Follow the prompts:
# - Set up and deploy? Y
# - Which scope? [your-account]
# - Link to existing project? N
# - What's your project's name? free-fire-buff-tool
# - In which directory is your code located? ./
# - Want to override the settings? N
```

### Cách 2: Deploy qua GitHub

1. **Push code lên GitHub**
```bash
git add .
git commit -m "Ready for Vercel deployment"
git push
```

2. **Import vào Vercel**
   - Truy cập [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import từ GitHub repository
   - Vercel sẽ tự động detect và deploy

## ⚙️ Cấu Hình Environment Variables

Trong Vercel Dashboard:
1. Vào project settings
2. Tab "Environment Variables"
3. Thêm các biến môi trường:

```
DATABASE_URL=sqlite:///./buff_like.db
DEFAULT_KEY=ch9ayfa-l7away
```

## 🔧 Troubleshooting

### Lỗi thường gặp:

1. **Module not found**
   - Kiểm tra `requirements.txt` có đầy đủ dependencies
   - Đảm bảo tất cả imports đều có trong requirements

2. **Database issues**
   - Vercel không hỗ trợ SQLite persistent
   - Cần chuyển sang PostgreSQL hoặc MongoDB
   - Hoặc sử dụng Vercel KV (Redis)

3. **Template not found**
   - Đảm bảo thư mục `templates/` được include
   - Kiểm tra đường dẫn templates trong code

## 📊 Monitoring

Sau khi deploy:
- **URL**: `https://your-project.vercel.app`
- **Logs**: Vercel Dashboard > Functions
- **Analytics**: Vercel Analytics (tự động)

## 🔄 Auto Deploy

Vercel sẽ tự động deploy khi:
- Push code lên GitHub
- Merge pull request
- Thay đổi branch

## 💡 Tối Ưu Hóa

1. **Cold Start**: Sử dụng Vercel Pro để giảm cold start
2. **Database**: Chuyển sang PostgreSQL cho production
3. **Caching**: Sử dụng Vercel KV cho cache
4. **CDN**: Vercel tự động optimize static files

## 🎯 Kết Quả

Sau khi deploy thành công:
- ✅ Tool hoạt động online 24/7
- ✅ Tự động scale theo traffic
- ✅ SSL certificate tự động
- ✅ Global CDN
- ✅ Analytics và monitoring

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra Vercel logs
2. Test locally trước khi deploy
3. Đảm bảo tất cả dependencies đúng version
4. Kiểm tra environment variables 