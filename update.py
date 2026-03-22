with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. اصلاح اسماء المستخدمين
c = c.replace(
    "const userName   = tgUser?.first_name || 'User';",
    "const userName = tgUser?.first_name || null;"
)

c = c.replace(
    "        userId, name:userName, level:1, balance:0,",
    "        const newCode2 = generateUserCode();\n        userId, name: userName || ('#' + newCode2), level:1, balance:0,"
)

# 2. منع الاحالة المكررة
c = c.replace(
    "async function registerReferral(referrerId){\n  try {\n    const referrerRef  = doc(db,'users',referrerId);",
    """async function registerReferral(referrerId){
  try {
    const existingRef = doc(db,'referrals',referrerId,'list',userId);
    const existingSnap = await getDoc(existingRef);
    if(existingSnap.exists()) return;
    const referrerRef  = doc(db,'users',referrerId);"""
)

# 3. البانر الاعلاني
banner = '''
  <!-- PROMO BANNER -->
  <div onclick="openInfoModal()" style="margin:0 0 14px 0;background:linear-gradient(135deg,#1a1200,#0d1120,#0a1a10);border:1px solid rgba(240,180,41,0.35);border-radius:18px;padding:16px 18px;display:flex;align-items:center;gap:14px;cursor:pointer;position:relative;overflow:hidden;animation:promoPulse 3s ease-in-out infinite;">
    <div style="font-size:36px;animation:catBounce 2s ease-in-out infinite;">🐱</div>
    <div style="flex:1;">
      <div style="font-size:13px;font-weight:900;color:#f0b429;">🚀 شارك GOLDCAT واربح أكثر!</div>
      <div style="font-size:11px;color:rgba(255,255,255,0.55);">ادعُ أصدقاءك واحصل على TON حقيقي</div>
    </div>
    <div style="background:linear-gradient(135deg,#f0b429,#ff8c00);border-radius:50%;width:34px;height:34px;display:flex;align-items:center;justify-content:center;font-size:16px;">📤</div>
  </div>
  <style>
    @keyframes promoPulse{0%,100%{border-color:rgba(240,180,41,0.25);}50%{border-color:rgba(240,180,41,0.6);}}
    @keyframes catBounce{0%,100%{transform:translateY(0);}50%{transform:translateY(-4px);}}
  </style>
'''

c = c.replace(
    '  <div class="section">\n    <button class="withdraw-btn" onclick="openWithdraw()">',
    banner + '  <div class="section">\n    <button class="withdraw-btn" onclick="openWithdraw()">'
)

# 4. صفحة الشرح
info_modal = '''
<!-- INFO MODAL -->
<div class="modal-overlay" id="info-modal" onclick="if(event.target===this)this.classList.remove('open')" style="z-index:9999;">
  <div class="modal" style="max-height:88vh;overflow-y:auto;">
    <div class="modal-handle"></div>
    <div style="text-align:center;padding:10px 0 18px;">
      <div style="font-size:48px;">🐱</div>
      <div style="font-size:22px;font-weight:900;color:#f0b429;margin:8px 0 4px;">GOLDCAT</div>
      <div style="font-size:13px;color:rgba(255,255,255,0.5);">دليل استخدام التطبيق</div>
    </div>
    <div style="height:1px;background:linear-gradient(90deg,transparent,rgba(240,180,41,0.4),transparent);margin-bottom:20px;"></div>
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(240,180,41,0.12);border-radius:16px;padding:16px;margin-bottom:12px;">
      <div style="font-size:15px;font-weight:700;color:#fff;margin-bottom:8px;">1️⃣ سجّل وابدأ مجاناً</div>
      <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.7;">افتح التطبيق عبر تيليغرام وسيُنشأ حسابك تلقائياً بدون تسجيل.</div>
    </div>
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(240,180,41,0.12);border-radius:16px;padding:16px;margin-bottom:12px;">
      <div style="font-size:15px;font-weight:700;color:#fff;margin-bottom:8px;">2️⃣ ادعُ أصدقاءك</div>
      <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.7;">شارك رابط الإحالة واحصل على TON فوري. 5 إحالات = تعدين مجاني!</div>
    </div>
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(240,180,41,0.12);border-radius:16px;padding:16px;margin-bottom:12px;">
      <div style="font-size:15px;font-weight:700;color:#fff;margin-bottom:8px;">3️⃣ التعدين التلقائي ⛏️</div>
      <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.7;">يعمل 24/7 حتى وأنت نائم أو الهاتف مغلق.</div>
    </div>
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(240,180,41,0.12);border-radius:16px;padding:16px;margin-bottom:12px;">
      <div style="font-size:15px;font-weight:700;color:#fff;margin-bottom:8px;">4️⃣ المستويات 🚀</div>
      <div style="display:flex;justify-content:space-around;margin-top:10px;">
        <div style="text-align:center;"><div>⚪</div><div style="font-size:10px;color:rgba(255,255,255,0.4);">0.05</div></div>
        <div style="text-align:center;"><div>🥉</div><div style="font-size:10px;color:rgba(255,255,255,0.4);">0.10</div></div>
        <div style="text-align:center;"><div>🥈</div><div style="font-size:10px;color:rgba(255,255,255,0.4);">0.15</div></div>
        <div style="text-align:center;"><div>🥇</div><div style="font-size:10px;color:rgba(255,255,255,0.4);">0.20</div></div>
        <div style="text-align:center;"><div>💎</div><div style="font-size:10px;color:rgba(255,255,255,0.4);">0.25</div></div>
      </div>
    </div>
    <div style="background:rgba(0,136,204,0.08);border:1px solid rgba(0,136,204,0.25);border-radius:16px;padding:16px;margin-bottom:20px;">
      <div style="font-size:15px;font-weight:700;color:#fff;margin-bottom:8px;">5️⃣ اسحب أرباحك 💎</div>
      <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.7;">اربط محفظة TON واسحب متى شئت. الحد الأدنى 0.5 TON.</div>
    </div>
    <button onclick="document.getElementById('info-modal').classList.remove('open');shareLink();" style="width:100%;background:linear-gradient(135deg,#f0b429,#ff8c00);color:#000;font-weight:900;font-size:16px;border:none;border-radius:50px;padding:16px;cursor:pointer;">📤 شارك الآن</button>
  </div>
</div>
<script>window.openInfoModal=function(){document.getElementById('info-modal').classList.add('open');}</script>
'''

c = c.replace('</body>\n</html>', info_modal + '\n</body>\n</html>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Done! All updates applied.")
