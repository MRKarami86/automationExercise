from zapv2 import ZAPv2

BASE_URL = 'https://petstore.swagger.io/v2'
ZAP_PROXY = 'http://localhost:8080'  # آدرس ZAP Proxy خود را وارد کنید


# متد برای اتصال به ZAP
def connect_to_zap():
    api_key = None  # در صورت نیاز به احراز هویت، کلید API خود را وارد کنید
    return ZAPv2(apikey=api_key, proxies={'http': ZAP_PROXY, 'https': ZAP_PROXY})


# تست SQL Injection با OWASP ZAP
def test_sql_injection_with_zap():
    zap = connect_to_zap()

    # اسکنر ZAP را برای URL مورد نظر فعال کنید
    zap.urlopen(BASE_URL)
    scan_id = zap.ascan.scan(BASE_URL)

    # منتظر ماندن برای اتمام اسکن
    while int(zap.ascan.status(scan_id)) < 100:
        print(f'Scan progress: {zap.ascan.status(scan_id)}%')
        

    # بررسی گزارش‌های اسکن
    alerts = zap.core.alerts(baseurl=BASE_URL)
    sql_injection_alerts = [alert for alert in alerts if
                            alert.get('risk') == 'High' and alert.get('alert') == 'SQL Injection']

    assert not sql_injection_alerts, f"SQL Injection vulnerability detected: {sql_injection_alerts}"


# تست XSS با OWASP ZAP
def test_xss_with_zap():
    zap = connect_to_zap()

    # اسکنر ZAP را برای URL مورد نظر فعال کنید
    zap.urlopen(BASE_URL)
    scan_id = zap.ascan.scan(BASE_URL)

    # منتظر ماندن برای اتمام اسکن
    while int(zap.ascan.status(scan_id)) < 100:
        print(f'Scan progress: {zap.ascan.status(scan_id)}%')


    # بررسی گزارش‌های اسکن
    alerts = zap.core.alerts(baseurl=BASE_URL)
    xss_alerts = [alert for alert in alerts if
                  alert.get('risk') == 'High' and alert.get('alert') == 'Cross Site Scripting (Reflected)']

    assert not xss_alerts, f"XSS vulnerability detected: {xss_alerts}"


if __name__ == "__main__":
    test_sql_injection_with_zap()
    test_xss_with_zap()
