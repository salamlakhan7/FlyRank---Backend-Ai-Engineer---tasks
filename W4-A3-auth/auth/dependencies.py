from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from supabase_client import supabase

# HTTPBearer is what makes the "Authorize" padlock appear in Swagger UI (/docs)
# auto_error=False lets us control the exact 401 message ourselves instead of FastAPI's default.
bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    """
    The single reusable guard (Stage 4). Apply this to any route via Depends(get_current_user).

    - No header / malformed header / no token -> 401 "Access token required"
    - Token present but invalid, expired, or tampered -> 401 "Invalid or expired token"
    - Token verified -> returns the Supabase user object, injected into the route
    """
    if credentials is None or not credentials.credentials:
        raise HTTPException(status_code=401, detail="Access token required")

    token = credentials.credentials

    try:
        user_response = supabase.auth.get_user(token)
    except Exception:
        # Supabase SDK raises on invalid/expired/tampered tokens
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    if not user_response or not user_response.user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return user_response.user