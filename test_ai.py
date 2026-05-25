from ai_service import analyze_with_ai

logs = """
[2026-05-23 10:12:01] ERROR db-service: query timeout after 30s (query=SELECT * FROM users)
[2026-05-23 10:12:03] WARN  api-gateway: memory usage at 92% (heap=1.8GB/2GB)
[2026-05-23 10:12:05] ERROR auth-service: failed login attempt (reason=token expired)
[2026-05-23 10:12:07] ERROR db-service: query timeout after 30s (query=SELECT orders)
"""

response = analyze_with_ai(logs)

print(response)