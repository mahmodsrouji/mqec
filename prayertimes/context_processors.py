# prayertimes/context_processors.py
import requests
from django.core.cache import cache

def prayer_times(request):
    # محاولة الحصول على البيانات من الكاش لتفادي الاتصال المتكرر بالـ API
    times = cache.get('prayer_times')
    
    if times is None:
        # إذا لم توجد البيانات في الكاش، نقوم بالاتصال بالـ API
        url = "http://api.aladhan.com/v1/timingsByCity"
        params = {
            "city": "Sheffield",
            "country": "United Kingdom",
            "method": 2  # طريقة الحساب
        }
        try:
            response = requests.get(url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                times = data.get('data', {}).get('timings', {})
                # تخزين البيانات في الكاش لمدة 10 دقائق (600 ثانية)
                cache.set('prayer_times', times, 600)
            else:
                times = {}
        except Exception as e:
            # في حال حدوث خطأ، يمكن تسجيله أو التعامل معه بطريقة مناسبة
            times = {}

    # نعيد القاموس الذي سيصبح جزءًا من السياق العام لكل القوالب
    return {"prayer_times": times}
