# -*- coding: utf-8 -*-
HTML = r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>جنان برو — تسجيل الدخول</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#0b1120;--bg2:#111828;--bg3:#1a2235;--text:#f1f5f9;--muted:#94a3b8;--border:rgba(255,255,255,.09);--accent:#6366f1;--accent2:#4f46e5}
body{font-family:'Tajawal',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;display:flex;overflow:hidden}
.left-panel{flex:1;min-width:0;height:100vh;overflow:hidden;position:relative;background:linear-gradient(160deg,#0b0f1e 0%,#131b35 40%,#0f1829 100%);display:flex;flex-direction:column;padding:1.75rem 2rem;gap:1.2rem}
.left-panel::before{content:'';position:absolute;top:-120px;right:-120px;width:420px;height:420px;border-radius:50%;background:radial-gradient(circle,rgba(99,102,241,.18) 0%,transparent 70%);pointer-events:none}
.left-panel::after{content:'';position:absolute;bottom:-80px;left:-80px;width:320px;height:320px;border-radius:50%;background:radial-gradient(circle,rgba(139,92,246,.12) 0%,transparent 70%);pointer-events:none}
.dot-grid{position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(circle,rgba(99,102,241,.08) 1px,transparent 1px);background-size:28px 28px}
.lp-logo{display:flex;align-items:center;gap:.85rem;position:relative;z-index:1}
.lp-logo-icon{width:46px;height:46px;border-radius:13px;background:linear-gradient(135deg,#4f46e5,#7c3aed);display:flex;align-items:center;justify-content:center;font-size:1.25rem;color:#fff;box-shadow:0 4px 18px rgba(99,102,241,.45);flex-shrink:0}
.lp-name{font-size:1.2rem;font-weight:900;color:#fff;line-height:1}
.lp-sub{font-size:.6rem;color:rgba(255,255,255,.35);letter-spacing:1.5px;font-weight:600;margin-top:.15rem}
.product-card{position:relative;z-index:1;background:linear-gradient(135deg,rgba(99,102,241,.13),rgba(79,70,229,.06));border:1.5px solid rgba(99,102,241,.3);border-radius:16px;padding:1.2rem 1.3rem;overflow:hidden;flex-shrink:0}
.product-card::before{content:'';position:absolute;top:0;right:0;left:0;height:2px;background:linear-gradient(90deg,#6366f1,#a855f7)}
.pc-badge{display:inline-flex;align-items:center;gap:.35rem;background:rgba(34,197,94,.12);border:1px solid rgba(34,197,94,.25);border-radius:20px;padding:.2rem .65rem;font-size:.62rem;font-weight:800;color:#86efac;margin-bottom:.55rem}
.pc-name{font-size:1.25rem;font-weight:900;color:#fff;line-height:1.2;margin-bottom:.35rem}
.pc-name span{background:linear-gradient(135deg,#818cf8,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.pc-desc{font-size:.76rem;color:rgba(199,210,254,.65);line-height:1.75;margin-bottom:.8rem}
.tags{display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:.8rem}
.tag{border-radius:7px;padding:.18rem .55rem;font-size:.63rem;font-weight:700}
.stats-row{display:flex;gap:1rem;padding-top:.7rem;border-top:1px solid rgba(255,255,255,.07)}
.stat-num{font-size:1.05rem;font-weight:900;background:linear-gradient(135deg,#818cf8,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stat-lbl{font-size:.58rem;color:rgba(255,255,255,.35);margin-top:.08rem}
.features-list{position:relative;z-index:1;display:flex;flex-direction:column;gap:.55rem}
.feat-card{background:rgba(255,255,255,.035);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:.68rem .9rem;display:flex;align-items:center;gap:.8rem;transition:background .2s,border-color .2s;cursor:default}
.feat-card:hover{background:rgba(99,102,241,.09);border-color:rgba(99,102,241,.25)}
.feat-icon{width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:.88rem;flex-shrink:0}
.feat-title{font-size:.82rem;font-weight:800;color:#fff}
.feat-desc{font-size:.67rem;color:rgba(255,255,255,.4);margin-top:.07rem}
.feat-check{margin-right:auto;width:20px;height:20px;border-radius:50%;background:rgba(34,197,94,.12);border:1px solid rgba(34,197,94,.25);display:flex;align-items:center;justify-content:center;font-size:.55rem;color:#86efac;flex-shrink:0}
.zatca-bar{position:relative;z-index:1;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:11px;padding:.62rem .9rem;display:flex;align-items:center;gap:.7rem}
.zatca-badge{background:linear-gradient(135deg,#16a34a,#15803d);border-radius:7px;padding:.2rem .6rem;font-size:.62rem;font-weight:900;color:#fff;letter-spacing:.5px;flex-shrink:0}
.zatca-text{font-size:.69rem;color:rgba(255,255,255,.45)}
.zatca-text strong{color:rgba(255,255,255,.8)}
.lp-footer{position:relative;z-index:1;margin-top:auto;text-align:center;font-size:.6rem;color:rgba(255,255,255,.18)}
.right-panel{width:100%;max-width:470px;min-width:320px;height:100vh;flex-shrink:0;background:#fff;display:flex;flex-direction:column;overflow:hidden}
.rp-top{display:flex;align-items:center;justify-content:space-between;padding:.78rem 1.6rem;border-bottom:1px solid #f1f5f9;flex-shrink:0}
.rp-back{display:flex;align-items:center;gap:.4rem;font-size:.78rem;color:#64748b;text-decoration:none;transition:color .2s}
.rp-back:hover{color:#6366f1}
.rp-tabs{display:flex;gap:.2rem;background:#f8fafc;border-radius:10px;padding:.2rem}
.rp-tab{padding:.36rem .9rem;border-radius:8px;border:none;font-family:'Tajawal',sans-serif;font-size:.78rem;font-weight:700;cursor:pointer;transition:background .2s,color .2s;background:transparent;color:#94a3b8}
.rp-tab.active{background:#fff;color:#6366f1;box-shadow:0 1px 4px rgba(0,0,0,.08)}
.rp-body{flex:1;overflow-y:auto;padding:1.5rem 1.75rem;display:flex;flex-direction:column;gap:.9rem}
.form-panel{display:none}
.form-panel.active{display:flex;flex-direction:column;gap:.9rem;animation:fadeUp .3s ease}
@keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.form-head h2{font-size:1.45rem;font-weight:900;color:#0f172a;line-height:1.2}
.form-head p{font-size:.78rem;color:#64748b;margin-top:.25rem}
.field-group{display:flex;flex-direction:column;gap:.28rem}
.field-label{font-size:.78rem;font-weight:700;color:#374151}
.field-wrap{position:relative}
.field-wrap input,.field-wrap select{width:100%;padding:.65rem 2.3rem .65rem .85rem;border:1.5px solid #e2e8f0;border-radius:11px;font-family:'Tajawal',sans-serif;font-size:.85rem;color:#0f172a;background:#fff;outline:none;transition:border-color .2s,box-shadow .2s;appearance:none}
.field-wrap input:focus,.field-wrap select:focus{border-color:#6366f1;box-shadow:0 0 0 3px rgba(99,102,241,.1)}
.field-wrap input.error,.field-wrap select.error{border-color:#ef4444}
.field-ico{position:absolute;top:50%;transform:translateY(-50%);right:.75rem;font-size:.78rem;color:#94a3b8;pointer-events:none}
.field-eye{position:absolute;top:50%;transform:translateY(-50%);left:.75rem;font-size:.78rem;color:#94a3b8;cursor:pointer}
.field-err{font-size:.68rem;color:#ef4444;display:none}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:.6rem}
.submit-btn{width:100%;padding:.75rem;border:none;border-radius:12px;background:linear-gradient(135deg,#6366f1,#4f46e5);color:#fff;font-family:'Tajawal',sans-serif;font-size:.9rem;font-weight:800;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:.45rem;box-shadow:0 4px 16px rgba(99,102,241,.28);transition:opacity .2s,transform .2s}
.submit-btn:hover{opacity:.9;transform:translateY(-1px)}
.submit-btn:disabled{opacity:.6;cursor:not-allowed;transform:none}
.divider{display:flex;align-items:center;gap:.6rem}
.divider::before,.divider::after{content:'';flex:1;height:1px;background:#e2e8f0}
.divider span{font-size:.7rem;color:#94a3b8;white-space:nowrap}
.social-btn{width:100%;padding:.65rem;border:1.5px solid #e2e8f0;border-radius:11px;background:#fff;color:#374151;font-family:'Tajawal',sans-serif;font-size:.83rem;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:.5rem;transition:border-color .2s,background .2s}
.social-btn:hover{border-color:#6366f1;background:#fafafa}
.form-link{text-align:center;font-size:.77rem;color:#64748b}
.form-link a{color:#6366f1;font-weight:700;cursor:pointer;text-decoration:none}
.form-link a:hover{text-decoration:underline}
.pw-strength{display:flex;gap:.3rem;margin-top:.28rem}
.pw-bar{height:3px;flex:1;border-radius:2px;background:#e2e8f0;transition:.3s}
.str-1 .pw-bar:nth-child(1){background:#ef4444}
.str-2 .pw-bar:nth-child(-n+2){background:#f97316}
.str-3 .pw-bar:nth-child(-n+3){background:#eab308}
.str-4 .pw-bar{background:#22c55e}
.steps-bar{display:flex;align-items:center;gap:.3rem;justify-content:center;margin-bottom:.3rem}
.step-dot{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:800;border:2px solid #e2e8f0;color:#94a3b8;background:#fff;transition:.3s}
.step-dot.active{background:linear-gradient(135deg,#6366f1,#4f46e5);border-color:transparent;color:#fff;box-shadow:0 3px 10px rgba(99,102,241,.35)}
.step-dot.done{background:#0f172a;border-color:transparent;color:#fff}
.step-line{flex:1;height:2px;background:#e2e8f0;max-width:40px}
.step-line.done{background:#6366f1}
.spinner{display:none;width:17px;height:17px;border:2.5px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .65s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.alert-err{background:#fef2f2;border:1px solid #fecaca;border-radius:10px;padding:.58rem .88rem;font-size:.77rem;color:#dc2626;display:flex;align-items:center;gap:.45rem}
.alert-err.hidden{display:none!important}
.success-screen{display:none;flex-direction:column;align-items:center;justify-content:center;gap:.85rem;text-align:center;padding:2rem}
.success-icon{width:68px;height:68px;border-radius:50%;background:rgba(34,197,94,.1);border:2px solid rgba(34,197,94,.25);display:flex;align-items:center;justify-content:center;font-size:1.85rem;animation:popIn .5s ease}
@keyframes popIn{0%{transform:scale(0)}80%{transform:scale(1.1)}100%{transform:scale(1)}}
.back-btn{flex:1;padding:.65rem;border:1.5px solid #e2e8f0;border-radius:11px;background:#fff;color:#374151;font-family:'Tajawal',sans-serif;font-size:.83rem;font-weight:700;cursor:pointer;transition:border-color .2s}
.back-btn:hover{border-color:#6366f1}
.rp-footer{padding:.7rem 1.75rem;border-top:1px solid #f1f5f9;text-align:center;font-size:.68rem;color:#94a3b8;flex-shrink:0}
.rp-footer a{color:#6366f1;text-decoration:none;font-weight:600}
@media(max-width:768px){.left-panel{display:none}.right-panel{max-width:100%}}
</style>
</head>
<body>

<div class="left-panel">
  <div class="dot-grid"></div>
  <div class="lp-logo">
    <div class="lp-logo-icon"><i class="fa-solid fa-rocket"></i></div>
    <div>
      <div class="lp-name">جنان <span style="background:linear-gradient(135deg,#818cf8,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent">برو</span></div>
      <div class="lp-sub">JENAN PRO · ERP PLATFORM</div>
    </div>
    <div style="margin-right:auto;background:rgba(134,239,172,.1);border:1px solid rgba(134,239,172,.22);border-radius:20px;padding:.16rem .65rem;font-size:.58rem;color:#86efac;font-weight:800">v2.0 مجاني</div>
  </div>

  <div class="product-card">
    <div class="pc-badge"><i class="fa-solid fa-calculator"></i> محاسبة احترافية · مدمجة ومجانية</div>
    <div class="pc-name">محاسبة <span>بلا تعقيد</span></div>
    <div class="pc-desc">نظام محاسبي ذكي مدمج مع الكاشير — لا تحتاج خبرة مسبقة. فواتير وتقارير مالية بضغطة واحدة.</div>
    <div class="tags">
      <span class="tag" style="background:rgba(99,102,241,.15);border:1px solid rgba(99,102,241,.25);color:#a5b4fc">ZATCA ✓</span>
      <span class="tag" style="background:rgba(16,185,129,.1);border:1px solid rgba(16,185,129,.2);color:#6ee7b7">P&L لحظي</span>
      <span class="tag" style="background:rgba(234,179,8,.1);border:1px solid rgba(234,179,8,.2);color:#fde68a">تدفقات نقدية</span>
      <span class="tag" style="background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.2);color:#fca5a5">فاتورة إلكترونية</span>
    </div>
    <div class="stats-row">
      <div><div class="stat-num">مجاني</div><div class="stat-lbl">ومدمج 100%</div></div>
      <div><div class="stat-num">ZATCA</div><div class="stat-lbl">متوافق تماماً</div></div>
      <div><div class="stat-num">3</div><div class="stat-lbl">أنشطة تجارية</div></div>
    </div>
  </div>

  <div class="features-list">
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(99,102,241,.15);border:1px solid rgba(99,102,241,.25)"><i class="fa-solid fa-chart-pie" style="color:#818cf8"></i></div>
      <div><div class="feat-title">تقرير أرباح وخسائر P&L</div><div class="feat-desc">رؤية مالية كاملة — شهري، ربعي، وسنوي</div></div>
      <div class="feat-check"><i class="fa-solid fa-check"></i></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(234,179,8,.1);border:1px solid rgba(234,179,8,.2)"><i class="fa-solid fa-receipt" style="color:#fbbf24"></i></div>
      <div><div class="feat-title">تسجيل المصروفات اليومية</div><div class="feat-desc">صنّف وتابع مصروفاتك بكل سهولة</div></div>
      <div class="feat-check"><i class="fa-solid fa-check"></i></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(16,185,129,.1);border:1px solid rgba(16,185,129,.2)"><i class="fa-solid fa-file-invoice" style="color:#34d399"></i></div>
      <div><div class="feat-title">فاتورة إلكترونية ZATCA</div><div class="feat-desc">متوافقة مع هيئة الزكاة بضغطة واحدة</div></div>
      <div class="feat-check"><i class="fa-solid fa-check"></i></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.2)"><i class="fa-solid fa-link" style="color:#f87171"></i></div>
      <div><div class="feat-title">ربط مباشر مع الكاشير</div><div class="feat-desc">كل بيعة تُسجَّل تلقائياً بدون إدخال يدوي</div></div>
      <div class="feat-check"><i class="fa-solid fa-check"></i></div>
    </div>
  </div>

  <div class="zatca-bar">
    <div class="zatca-badge">ZATCA 2026</div>
    <div class="zatca-text"><strong>متوافق مع الفوترة الإلكترونية الإصدار الثاني</strong> · هيئة الزكاة والضريبة والجمارك</div>
    <i class="fa-solid fa-shield-check" style="color:#22c55e;margin-right:auto;flex-shrink:0;font-size:1.05rem"></i>
  </div>

  <div class="lp-footer">&#169; 2026 جنان برو &middot; جميع الحقوق محفوظة</div>
</div>


<div class="right-panel">
  <div class="rp-top">
    <a href="dashboard.html" class="rp-back"><i class="fa-solid fa-arrow-right"></i> الرئيسية</a>
    <div class="rp-tabs">
      <button class="rp-tab active" id="tab-login" onclick="switchTab('login')">دخول</button>
      <button class="rp-tab" id="tab-register" onclick="switchTab('register')">حساب جديد</button>
    </div>
  </div>

  <div class="rp-body">

    <div class="form-panel active" id="panel-login">
      <div class="form-head"><h2>مرحباً بعودتك 👋</h2><p>سجّل دخولك للوصول إلى نظام جنان برو</p></div>
      <div class="alert-err hidden" id="login-alert"><i class="fa-solid fa-circle-exclamation"></i><span id="login-alert-msg">بيانات الدخول غير صحيحة</span></div>
      <form novalidate onsubmit="doLogin(event)">
        <div class="field-group" style="margin-bottom:.65rem">
          <label class="field-label">البريد الإلكتروني أو اسم المستخدم</label>
          <div class="field-wrap"><input type="text" id="l-user" placeholder="example@email.com" dir="ltr" autocomplete="username"><i class="fa-solid fa-user field-ico"></i></div>
          <span class="field-err" id="l-user-err">يرجى إدخال البريد الإلكتروني</span>
        </div>
        <div class="field-group" style="margin-bottom:.65rem">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:.28rem">
            <label class="field-label" style="margin:0">كلمة المرور</label>
            <a onclick="switchTo('reset')" style="font-size:.72rem;color:#6366f1;cursor:pointer;font-weight:700">نسيت كلمة المرور؟</a>
          </div>
          <div class="field-wrap"><input type="password" id="l-pass" placeholder="••••••••" autocomplete="current-password"><i class="fa-solid fa-lock field-ico"></i><i class="fa-solid fa-eye field-eye" id="eye-l" onclick="toggleEye('l-pass','eye-l')"></i></div>
          <span class="field-err" id="l-pass-err">يرجى إدخال كلمة المرور</span>
        </div>
        <div style="display:flex;align-items:center;gap:.45rem;margin-bottom:.75rem">
          <input type="checkbox" id="remember" style="width:15px;height:15px;accent-color:#6366f1;cursor:pointer">
          <label for="remember" style="font-size:.78rem;color:#64748b;cursor:pointer">تذكّرني لـ 30 يوم</label>
        </div>
        <button type="submit" class="submit-btn" id="login-btn">
          <span id="login-txt">تسجيل الدخول</span><div class="spinner" id="login-spin"></div><i class="fa-solid fa-arrow-left" id="login-ico"></i>
        </button>
      </form>
      <div class="divider"><span>أو تابع بـ</span></div>
      <button class="social-btn" onclick="showToast('تسجيل جوجل قريباً!')">
        <svg width="17" height="17" viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>
        المتابعة بحساب Google
      </button>
      <div class="form-link">ليس لديك حساب؟ <a onclick="switchTab('register')">أنشئ حسابك مجاناً</a></div>
    </div>


    <div class="form-panel" id="panel-register">
      <div class="steps-bar">
        <div class="step-dot active" id="sdot-1">1</div>
        <div class="step-line" id="sline-1"></div>
        <div class="step-dot" id="sdot-2">2</div>
        <div class="step-line" id="sline-2"></div>
        <div class="step-dot" id="sdot-3">3</div>
      </div>

      <div id="reg-step-1">
        <div class="form-head" style="margin-bottom:.75rem"><h2>أنشئ حسابك 🚀</h2><p>الخطوة 1 — معلوماتك الشخصية</p></div>
        <div class="field-row" style="margin-bottom:.6rem">
          <div class="field-group">
            <label class="field-label">الاسم الأول</label>
            <div class="field-wrap"><input type="text" id="r-fname" placeholder="سارة"><i class="fa-solid fa-user field-ico"></i></div>
            <span class="field-err" id="r-fname-err">مطلوب</span>
          </div>
          <div class="field-group">
            <label class="field-label">الاسم الأخير</label>
            <div class="field-wrap"><input type="text" id="r-lname" placeholder="العتيبي"><i class="fa-solid fa-user field-ico"></i></div>
            <span class="field-err" id="r-lname-err">مطلوب</span>
          </div>
        </div>
        <div class="field-group" style="margin-bottom:.6rem">
          <label class="field-label">البريد الإلكتروني</label>
          <div class="field-wrap"><input type="email" id="r-email" placeholder="sara@example.com" dir="ltr" autocomplete="email"><i class="fa-solid fa-envelope field-ico"></i></div>
          <span class="field-err" id="r-email-err">بريد إلكتروني غير صحيح</span>
        </div>
        <div class="field-group" style="margin-bottom:.75rem">
          <label class="field-label">رقم الجوال</label>
          <div class="field-wrap"><input type="tel" id="r-phone" placeholder="05xxxxxxxx" dir="ltr" maxlength="10"><i class="fa-solid fa-mobile-screen field-ico"></i></div>
          <span class="field-err" id="r-phone-err">رقم جوال سعودي غير صحيح (05xxxxxxxx)</span>
        </div>
        <button type="button" class="submit-btn" onclick="regNext(1)">التالي <i class="fa-solid fa-arrow-left"></i></button>
      </div>

      <div id="reg-step-2" style="display:none">
        <div class="form-head" style="margin-bottom:.75rem"><h2>منشأتك التجارية 🏪</h2><p>الخطوة 2 — معلومات مشروعك</p></div>
        <div class="field-group" style="margin-bottom:.6rem">
          <label class="field-label">اسم المنشأة</label>
          <div class="field-wrap"><input type="text" id="r-biz" placeholder="سوبرماركت الأمل"><i class="fa-solid fa-store field-ico"></i></div>
          <span class="field-err" id="r-biz-err">مطلوب</span>
        </div>
        <div class="field-group" style="margin-bottom:.6rem">
          <label class="field-label">نوع النشاط</label>
          <div class="field-wrap">
            <select id="r-activity">
              <option value="">اختر نوع النشاط</option>
              <option value="supermarket">🛒 سوبرماركت وتموين</option>
              <option value="restaurant">🍽️ مطعم أو كافيه</option>
              <option value="salon">💄 صالون نسائي وتجميل</option>
            </select>
            <i class="fa-solid fa-chevron-down field-ico"></i>
          </div>
          <span class="field-err" id="r-activity-err">يرجى اختيار نوع النشاط</span>
        </div>
        <div class="field-group" style="margin-bottom:.75rem">
          <label class="field-label">المدينة</label>
          <div class="field-wrap">
            <select id="r-city">
              <option value="">اختر المدينة</option>
              <option>الرياض</option><option>جدة</option><option>مكة المكرمة</option>
              <option>المدينة المنورة</option><option>الدمام</option><option>الخبر</option>
              <option>الطائف</option><option>بريدة</option><option>تبوك</option><option>أخرى</option>
            </select>
            <i class="fa-solid fa-chevron-down field-ico"></i>
          </div>
        </div>
        <div style="display:flex;gap:.55rem">
          <button type="button" class="back-btn" onclick="regBack(2)"><i class="fa-solid fa-arrow-right"></i> السابق</button>
          <button type="button" class="submit-btn" style="flex:2" onclick="regNext(2)">التالي <i class="fa-solid fa-arrow-left"></i></button>
        </div>
      </div>

      <div id="reg-step-3" style="display:none">
        <div class="form-head" style="margin-bottom:.75rem"><h2>كلمة مرورك 🔐</h2><p>الخطوة 3 — أنشئ كلمة مرور قوية</p></div>
        <div class="field-group" style="margin-bottom:.6rem">
          <label class="field-label">كلمة المرور</label>
          <div class="field-wrap"><input type="password" id="r-pass" placeholder="8 أحرف على الأقل" oninput="checkPwStrength(this.value)" autocomplete="new-password"><i class="fa-solid fa-lock field-ico"></i><i class="fa-solid fa-eye field-eye" id="eye-r" onclick="toggleEye('r-pass','eye-r')"></i></div>
          <div class="pw-strength" id="pw-bars"><div class="pw-bar"></div><div class="pw-bar"></div><div class="pw-bar"></div><div class="pw-bar"></div></div>
          <span class="field-err" id="r-pass-err">كلمة المرور قصيرة (8 أحرف على الأقل)</span>
        </div>
        <div class="field-group" style="margin-bottom:.6rem">
          <label class="field-label">تأكيد كلمة المرور</label>
          <div class="field-wrap"><input type="password" id="r-pass2" placeholder="أعد الكتابة" autocomplete="new-password"><i class="fa-solid fa-lock field-ico"></i><i class="fa-solid fa-eye field-eye" id="eye-r2" onclick="toggleEye('r-pass2','eye-r2')"></i></div>
          <span class="field-err" id="r-pass2-err">كلمتا المرور غير متطابقتان</span>
        </div>
        <div style="display:flex;align-items:flex-start;gap:.42rem;margin-bottom:.6rem">
          <input type="checkbox" id="terms" style="width:15px;height:15px;accent-color:#6366f1;cursor:pointer;margin-top:.15rem;flex-shrink:0">
          <label for="terms" style="font-size:.73rem;color:#64748b;cursor:pointer;line-height:1.6">أوافق على <a href="#" style="color:#6366f1;font-weight:700">شروط الاستخدام</a> و<a href="#" style="color:#6366f1;font-weight:700">سياسة الخصوصية</a></label>
        </div>
        <span class="field-err" id="r-terms-err">يجب الموافقة على الشروط أولاً</span>
        <div style="display:flex;gap:.55rem;margin-top:.4rem">
          <button type="button" class="back-btn" onclick="regBack(3)"><i class="fa-solid fa-arrow-right"></i> السابق</button>
          <button type="button" class="submit-btn" style="flex:2" id="reg-btn" onclick="doRegister()">
            <span id="reg-txt">إنشاء الحساب</span><div class="spinner" id="reg-spin"></div><i class="fa-solid fa-check" id="reg-ico"></i>
          </button>
        </div>
      </div>

      <div class="success-screen" id="reg-success">
        <div class="success-icon">🎉</div>
        <h3 style="font-size:1.3rem;font-weight:900;color:#0f172a" id="success-title">تم إنشاء حسابك!</h3>
        <p style="font-size:.8rem;color:#64748b;max-width:265px;line-height:1.7">نظامك المحاسبي جاهز — ابدأ الآن مجاناً!</p>
        <button onclick="window.location.href='jenan-erp.html'" class="submit-btn" style="max-width:255px"><i class="fa-solid fa-rocket" style="margin-left:.3rem"></i> ابدأ استخدام النظام</button>
      </div>

      <div class="form-link" id="reg-login-link">لديك حساب بالفعل؟ <a onclick="switchTab('login')">سجّل دخولك</a></div>
    </div>


    <div class="form-panel" id="panel-reset">
      <div class="form-head"><h2>استعادة كلمة المرور 🔑</h2><p>أدخل بريدك الإلكتروني وسنرسل لك رابط الاستعادة</p></div>
      <div class="field-group">
        <label class="field-label">البريد الإلكتروني</label>
        <div class="field-wrap"><input type="email" id="reset-email" placeholder="sara@example.com" dir="ltr"><i class="fa-solid fa-envelope field-ico"></i></div>
        <span class="field-err" id="reset-email-err">بريد إلكتروني غير صحيح</span>
      </div>
      <button type="button" class="submit-btn" onclick="doReset()"><i class="fa-solid fa-paper-plane" style="margin-left:.3rem"></i> إرسال رابط الاستعادة</button>
      <div class="form-link"><a onclick="switchTab('login')"><i class="fa-solid fa-arrow-right" style="margin-left:.22rem"></i>العودة لتسجيل الدخول</a></div>
    </div>

  </div>

  <div class="rp-footer">بحاجة إلى مساعدة؟ <a href="#">تواصل معنا</a> &middot; &#169; 2026 جنان برو</div>
</div>


<script>
function switchTab(t){
  document.querySelectorAll('.rp-tab').forEach(x=>x.classList.remove('active'));
  document.querySelectorAll('.form-panel').forEach(x=>x.classList.remove('active'));
  document.getElementById('tab-'+t).classList.add('active');
  document.getElementById('panel-'+t).classList.add('active');
  clearErrors();
}
function switchTo(p){
  document.querySelectorAll('.form-panel').forEach(x=>x.classList.remove('active'));
  document.getElementById('panel-'+p).classList.add('active');
}
function toggleEye(i,e){
  const inp=document.getElementById(i),eye=document.getElementById(e);
  if(inp.type==='password'){inp.type='text';eye.className=eye.className.replace('fa-eye','fa-eye-slash');}
  else{inp.type='password';eye.className=eye.className.replace('fa-eye-slash','fa-eye');}
}
function checkPwStrength(v){
  let s=0;if(v.length>=8)s++;if(/[A-Z]/.test(v))s++;if(/[0-9]/.test(v))s++;if(/[^A-Za-z0-9]/.test(v))s++;
  document.getElementById('pw-bars').className='pw-strength str-'+s;
}
function clearErrors(){
  document.querySelectorAll('.field-err').forEach(e=>e.style.display='none');
  document.querySelectorAll('input,select').forEach(i=>i.classList.remove('error'));
  const al=document.getElementById('login-alert');if(al)al.classList.add('hidden');
}
function showErr(id,msg){const el=document.getElementById(id);if(!el)return;if(msg)el.textContent=msg;el.style.display='block';}
function doLogin(e){
  e.preventDefault();clearErrors();
  const user=document.getElementById('l-user').value.trim();
  const pass=document.getElementById('l-pass').value;
  let ok=true;
  if(!user){showErr('l-user-err');document.getElementById('l-user').classList.add('error');ok=false;}
  if(!pass){showErr('l-pass-err');document.getElementById('l-pass').classList.add('error');ok=false;}
  if(!ok)return;
  setLoad('login-btn','login-txt','login-spin','login-ico',true,'جارٍ الدخول...');
  setTimeout(()=>window.location.href='jenan-erp.html',1400);
}
let regData={};
function regNext(step){
  clearErrors();
  if(step===1){
    const fn=document.getElementById('r-fname').value.trim(),ln=document.getElementById('r-lname').value.trim();
    const em=document.getElementById('r-email').value.trim(),ph=document.getElementById('r-phone').value.trim();
    let ok=true;
    if(!fn){showErr('r-fname-err');ok=false;}if(!ln){showErr('r-lname-err');ok=false;}
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em)){showErr('r-email-err');ok=false;}
    if(!/^05\d{8}$/.test(ph)){showErr('r-phone-err');ok=false;}
    if(!ok)return;regData={fn,ln,em,ph};goStep(2);
  }else if(step===2){
    const biz=document.getElementById('r-biz').value.trim();
    const act=document.getElementById('r-activity').value;
    let ok=true;
    if(!biz){showErr('r-biz-err');ok=false;}if(!act){showErr('r-activity-err');ok=false;}
    if(!ok)return;
    regData.biz=biz;regData.activity=act;regData.city=document.getElementById('r-city').value;
    goStep(3);
  }
}
function regBack(step){clearErrors();goStep(step-1);}
function goStep(n){
  [1,2,3].forEach(i=>{
    document.getElementById('reg-step-'+i).style.display=(i===n)?'block':'none';
    const d=document.getElementById('sdot-'+i);
    if(i<n){d.className='step-dot done';d.innerHTML='<i class="fa-solid fa-check" style="font-size:.52rem"></i>';}
    else if(i===n){d.className='step-dot active';d.textContent=i;}
    else{d.className='step-dot';d.textContent=i;}
    if(i<3){const l=document.getElementById('sline-'+i);l.className='step-line'+(i<n?' done':'');}
  });
}
function doRegister(){
  clearErrors();
  const pass=document.getElementById('r-pass').value;
  const pass2=document.getElementById('r-pass2').value;
  const terms=document.getElementById('terms').checked;
  let ok=true;
  if(pass.length<8){showErr('r-pass-err');ok=false;}
  if(pass!==pass2){showErr('r-pass2-err');ok=false;}
  if(!terms){showErr('r-terms-err');ok=false;}
  if(!ok)return;
  regData.pass=pass;
  setLoad('reg-btn','reg-txt','reg-spin','reg-ico',true,'جارٍ الإنشاء...');
  setTimeout(()=>{
    document.getElementById('reg-step-3').style.display='none';
    document.getElementById('reg-login-link').style.display='none';
    const sc=document.getElementById('reg-success');sc.style.display='flex';sc.style.flexDirection='column';
    document.getElementById('success-title').textContent='مرحباً '+(regData.fn||'')+'! 🎉';
  },1600);
}
function doReset(){
  clearErrors();
  const email=document.getElementById('reset-email').value.trim();
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)){showErr('reset-email-err');return;}
  showToast('تم إرسال رابط الاستعادة إلى بريدك الإلكتروني');
  setTimeout(()=>switchTab('login'),2200);
}
function setLoad(btnId,txtId,spinId,icoId,on,msg){
  const btn=document.getElementById(btnId),txt=document.getElementById(txtId),
        sp=document.getElementById(spinId),ic=document.getElementById(icoId);
  if(btn)btn.disabled=on;if(txt&&msg&&on)txt.textContent=msg;
  if(sp)sp.style.display=on?'block':'none';if(ic)ic.style.display=on?'none':'';
}
function showToast(msg){
  let t=document.getElementById('_toast');
  if(!t){t=document.createElement('div');t.id='_toast';
    Object.assign(t.style,{position:'fixed',bottom:'1.5rem',left:'50%',transform:'translateX(-50%) translateY(20px)',
      background:'#0f172a',color:'#f1f5f9',padding:'.58rem 1.2rem',borderRadius:'30px',fontSize:'.78rem',
      fontWeight:'700',boxShadow:'0 8px 28px rgba(0,0,0,.3)',zIndex:'9999',opacity:'0',
      transition:'all .3s',whiteSpace:'nowrap'});document.body.appendChild(t);}
  t.textContent=msg;t.style.opacity='1';t.style.transform='translateX(-50%) translateY(0)';
  setTimeout(()=>{t.style.opacity='0';t.style.transform='translateX(-50%) translateY(20px)';},2800);
}
</script>
</body>
</html>"""

with open(r'c:\Users\JEN21\OneDrive\سطح المكتب\بايثون\jenan-biz\auth.html','w',encoding='utf-8') as f:
    f.write(HTML)
print('Done. Length:', len(HTML))

